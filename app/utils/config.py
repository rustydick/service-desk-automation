"""Configuration module."""

import configparser

from .logger import logger

_configparser = configparser.ConfigParser()

_configparser.read(".env", encoding="utf-8")

config = _configparser["default"]

logger.info(f"Loaded config: {[{key: value} for key, value in config.items()]}")
