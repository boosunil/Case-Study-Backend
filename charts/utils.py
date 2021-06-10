import json
import re
from rest_framework.response import Response as DjangoResponse
from django.utils import six
from rest_framework.serializers import Serializer
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


class DictionaryAsAttributes(dict):
    """This converts the nested dictionary
    items into callable attributes i.e.
    dictionary = {
        'a': 'b',
        'c': {
            'd': {
                'e': 'f'
                }
            }
        }
    dictionary = DictionaryAsAttributes(dictionary)
    dictionary.c.d.e will returns 'f'
    """

    def __init__(self, dictionary={}):
        super(DictionaryAsAttributes, self).__init__(dictionary)

    def __call__(self, *args, **kwargs):
        return DictionaryAsAttributes(*args, **kwargs)

    def __getattr__(self, name):
        if isinstance(self.__getitem__(name), dict):
            return self(self.__getitem__(name))
        return self.__getitem__(name)

    def __setattr__(self, name, value):
        self.__setitem__(name, value)


def try_or(fn, default):
    try:
        return fn()
    except Exception:
        return default


def multipart_viewset_parser(request):
    request.data._mutable = True
    request._full_data = request.data.dict()
    for key, value in request.data.items():
        if isinstance(value, str) and re.match(r'^\[(.*?)\]$', value):
            request.data[key] = json.loads(value)
    return request


class Response(DjangoResponse):
    """
    An HttpResponse that allows its data to be rendered into
    arbitrary media types.
    """

    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        """
        Alters the init arguments slightly.
        For example, drop 'template_name', and instead use 'data'.

        Setting 'renderer' and 'media_type' will typically be deferred,
        For example being set automatically by the `APIView`.
        """
        super(Response, self).__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        if exception is not None:
            exception = {"success": False, "data": exception}

        if isinstance(data, dict) or isinstance(data, list):
            data = {"success": True, "data": data}

        elif isinstance(data, ReturnList) or isinstance(data, ReturnDict):
            data = {"success": True, "data": data}

        else:
            data = {"success": True, "data": data}

        self.data = data
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value
