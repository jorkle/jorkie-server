#!/usr/bin/env python3

import sys
import argparse

from jorkieserver.types import CommandOptions, Configuration, Components
from jorkieserver.logging import LogWriter
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

        self.cli_args = self.__parse_args()
        self.config = self.__load_config()
        self.log_writer = self.__init_logging()
        self.components = self.__init_components()

    def __parse_args(self) -> CommandOptions:
        cli_arg_parser = argparse.ArgumentParser(
            prog=APPLICATION_NAME,
            usage=APPLICATION_USAGE,
            description=APPLICATION_DESCRIPTION,
        )

        cli_arg_parser.add_argument(
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

        cli_arg_parser.add_argument(
            "--log-file",
            "-lf",
            default=DEFAULT_LOG_FILE,
            required=False,
            action="store",
            help="Log file path",
            dest="log_file",
        )

        cli_arg_parser.add_argument(
            "--config",
            "-c",
            default=DEFAULT_CONFIG_FILE,
            required=False,
            action="store",
            help="Configuration file path",
            dest="config_file",
        )

        parsed_cli_args = cli_arg_parser.parse_args()

        cli_args = CommandOptions(
            parsed_cli_args.log_level,
            parsed_cli_args.log_file,
            parsed_cli_args.config_file,
        )

        return cli_args

    def __load_config(self) -> Configuration:
        config: Configuration = Configurator(self.log_writer, self.cli_args.config_file)
        return config

    def __init_logging(self) -> LogWriter:
        log_writer = LogWriter(
            self.cmd_opts.log_level, self.cmd_opts.log_file, DEFAULT_LOG_DIR
        )
        log_writer.debug("Logging initialized", "MAIN")
        return log_writer

    def __init_components(self) -> Components:
        return Components()  # TODO: Implement component initialization functionality


def main() -> None:
    Server()
    sys.exit(0)


if __name__ == "__main__":
    main()
