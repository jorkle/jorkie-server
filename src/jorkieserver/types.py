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

    def __init__(
        self,
        db_host: str,
        db_port: int,
        db_name: str,
        db_user: str,
        db_password: str,
        api_host: str,
        api_port: int,
        api_key: str,
        config_file_path: str,
        config_version: str,
    ):
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.api_host = api_host
        self.api_port = api_port
        self.api_key = api_key
        self.config_file_path = config_file_path
        self.config_version = config_version


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
