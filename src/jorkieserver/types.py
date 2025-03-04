#!/usr/bin/env python3


class CommandOptions:
    """
    Holds command line options that were specified at command execution.
    """

    def __init__(self, log_level: int, log_file: str, config_file: str):
        self.log_level = log_level
        self.log_file = log_file
        self.config_file = config_file


class Configuration:
    """
    A placeholder for configuration until a configuration module is implemented.
    """

    def __init__(self):
        self.api_host = None
        self.api_port = None
        self.api_version = None
        self.api_key = None
        self.api_secret = None
        self.api_timeout = None
        self.log_level = None
        self.log_file = None
        self.config_file = None


class Components:
    """
    A placeholder for components until a compoennts initiaization module is implemented.
    """

    def __init__(self):
        self.api = None
        self.db = None
        self.scheduler = None


class Log:
    """
    A placeholder for log configuration until a log module is implemented.
    """

    def __init__(self):
        self.log_level = None
        self.log_file = None
