#!/usr/bin/env python3

import sys
import argparse

from jorkieserver.types import CommandOptions, Configuration, Components, Log
from jorkieserver.logging import Log
from jorkieserver.constants import (
    APPLICATION_NAME,
    APPLICATION_DESCRIPTION,
    APPLICATION_USAGE,
    DEFAULT_LOG_DIR,
    DEFAULT_LOG_LEVEL,
    DEFAULT_LOG_FILE,
    DEFAULT_CONFIG_FILE,
)


class Server:
    """
    Server class that handles parsing command-line option,
    initiating the configuration-related logic,
    and initializing the asynchranous sub-components.
    """

    def __init__(self):
        """
        Initialize the Server object,
        parses cmd-line arguments by calling the `__parse_args()` method,
        loads (or initializes) the configuration by calling the `__load_config()` method,
        initializes the logging by calling the `__init_logging()` method,
        and initializes the asynchranous sub-components by calling `__init_components()`.
        """

        self.cmd_opts = self.__parse_args()
        self.config = self.__load_config()
        self.log = self.__init_logging()
        self.components = self.__init_components()

    def __parse_args(self) -> CommandOptions:
        """
        Parse command line arguments and return a CommandOptions object.

        Returns:
            CommandOptions: Parsed command line options.
        """
        parser = argparse.ArgumentParser(
            prog=APPLICATION_NAME,
            usage=APPLICATION_USAGE,
            description=APPLICATION_DESCRIPTION,
        )

        parser.add_argument(
            "--log-level",
            "-ll",
            default=DEFAULT_LOG_LEVEL,
            choices=[0, 1, 2, 3],
            required=False,
            action="store",
            type=int,
            help="(0=DEBUG, 1=INFO, 2=WARNING, 3=ERROR)",
            dest="log_level",
        )

        parser.add_argument(
            "--log-file",
            "-lf",
            default=DEFAULT_LOG_FILE,
            required=False,
            action="store",
            help="Log file path",
            dest="log_file",
        )

        parser.add_argument(
            "--config",
            "-c",
            default=DEFAULT_CONFIG_FILE,
            required=False,
            action="store",
            help="Configuration file path",
            dest="config_file",
        )

        args = parser.parse_args()

        cmd_opts = CommandOptions(args.log_level, args.log_file, args.config_file)

        return cmd_opts

    def __load_config(self) -> Configuration:
        """
        Load configuration from a file or initialize default configuration.

        Returns:
            Configuration: Configuration Object containing the configuration.
        """

        return Configuration()  # TODO: Implement configuration functionality

    def __init_logging(self) -> Log:
        """
        Initialize logging.

        Returns:
            Log: Log object that can be used for logging.
        """
        logger = Log(self.cmd_opts.log_level, self.cmd_opts.log_file, DEFAULT_LOG_DIR)
        logger.debug("Logging initialized", "MAIN")
        return logger

    def __init_components(self) -> Components:
        """
        Initialize the asynchranous sub-components.

        Returns:
        --------
            Components: Components object that contains the initialized components.
        """
        return Components()  # TODO: Implement component initialization functionality


def run() -> None:
    server = Server()
    sys.exit(0)
