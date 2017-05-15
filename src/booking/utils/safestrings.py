#-*- coding: utf-8 -*-

import logging
import re

from datetime import date
from os.path import splitext


logger = logging.getLogger('sigma.utils.log')


def sanitize_string(unsafe_string, lower=False):
    """Removes all non-word characters from a string
    Returns a string with only [a-zA-Z0-9_] characters
    """
    safe = re.sub(r'\W+', '_', unsafe_string).strip('_')
    safe = re.sub(r'_+', '_', safe)
    if lower:
        return safe.lower()
    else:
        return safe


def sanitize_basename(unsafe_basename, lower=False):
    """Requires a string like 'filename.extension'"""
    filename, extension = splitext(unsafe_basename)
    sanitized_filename = sanitize_string(filename, lower)
    logger.info("sanitized \"%s\" to \"%s\"" % (unsafe_basename,
        sanitized_filename + extension))
    return sanitized_filename + extension


def sanitized_upload_to(instance, unsafe_basename, lower=False):
    """To be used as function in ImageField 'upload_to'. The second argument is
    in the form 'filename.extension', no path is available.
    """
    model_name = sanitize_string(instance.__class__.__name__, True)
    anno = date.today().year
    filename = sanitize_basename(unsafe_basename, lower)
    return u'%s/%d/%s' % (model_name, anno, filename)
