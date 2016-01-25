from __future__ import unicode_literals
from six import PY3

import chardet
import logging
logger = logging.getLogger(__name__)

if PY3:
    def str_encode(value='', encoding=None, errors='strict'):
        encoding = chardet.detect(value)['encoding']
        logger.debug("Encode str {} with and errors {}".format(value, encoding, errors))
        return str(value, encoding, errors)

    def str_decode(value='', encoding=None, errors='strict'):
        try:
            encoding = chardet.detect(value)['encoding']
        except ValueError:
            encoding = 'utf-8'

        if isinstance(value, str):
            return bytes(value, encoding, errors).decode('utf-8')
        elif isinstance(value, bytes):
            return value.decode(encoding, errors=errors)
        else:
            raise TypeError( "Cannot decode '{}' object".format(value.__class__) )
else:
    def str_encode(string='', encoding=None, errors='strict'):
        encoding = chardet.detect(string)['encoding']
        return unicode(string, encoding, errors)

    def str_decode(value='', encoding=None, errors='strict'):
        encoding = chardet.detect(value)['encoding']
        return value.decode(encoding, errors)