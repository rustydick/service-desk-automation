"""Logger module for the project."""

import logging

from logging import Formatter
from colorlog import LevelFormatter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = LevelFormatter(
    log_colors={
        "DEBUG": "light_black",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
    fmt={
        "DEBUG": "%(log_color)sDEBUG:    %(light_black)s[%(module)s:%(lineno)s] %(msg)s",  # noqa: E501
        "INFO": "%(log_color)sINFO%(white)s:     %(light_black)s[%(module)s:%(lineno)s] %(white)s%(msg)s",  # noqa: E501
        "WARNING": "%(log_color)sWARNING%(white)s:  %(light_black)s[%(module)s:%(lineno)s] %(white)s%(msg)s",  # noqa: E501
        "ERROR": "%(log_color)sERROR%(white)s:    %(light_black)s[%(module)s:%(lineno)s] %(white)s%(msg)s",  # noqa: E501
        "CRITICAL": "%(log_color)sCRITICAL%(light_white)s: %(light_black)s[%(module)s:%(lineno)s] %(white)s%(msg)s",  # noqa: E501
    },
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)  # type: ignore

logger.addHandler(stream_handler)
