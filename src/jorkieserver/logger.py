import sys

import logging
from jorkieserver.utils import base64_encode, create_directory


class LogWriter:
    """
    Contains several merthods to log messages at different log levels.
    """

    def __init__(self, log_level: int, log_file: str, log_dir: str) -> None:
        self.level = log_level
        self.file = log_file
        self.__log_dir = create_directory(log_dir, "LOGGING")
        self.logger = self.__init_logger()

    def __init_logger(self):
        """
        Initializes the logger with the specified log level and log file.

        Raises:
            FileNotFoundError: The log file could not be found
            PermissionError: If there are insufficient permissions to write to the log file
            ValueError: If the log level is invalid
            Exception: Unkown error occurred while initializing the logger

        Returns:
        --------
            Logger: Instance of the logger which can be used to log messages
        """
        try:
            log_level = self.__get_log_level(self.level)
            logging.basicConfig(
                filename=self.file,
                level=log_level,
                format="%(asctime)s - %(message)s",
            )
        except FileNotFoundError:
            print(
                f"FATAL: [COMPONENT: LOGGING] The log file '{self.file}' could not be found.",
                file=sys.stderr,
            )
            sys.exit(1)
        except PermissionError:
            print(
                f"FATAL: [COMPONENT: LOGGING] Insufficient permissions to write to the log file '{self.file}'.",
                file=sys.stderr,
            )
            sys.exit(1)
        except ValueError:
            print(
                f"FATAL: [COMPONENT: LOGGING] Invalid log level '{self.level}'.",
                file=sys.stderr,
            )
            sys.exit(1)
        except Exception as e:
            print(
                "FATAL: [COMPONENT: LOGGING] Unknown error occurred while initializing the logger.",
                file=sys.stderr,
            )
            print(
                f"FATAL: [COMPONENT: LOGGING] Exception Details (base64 encoded): {str(e)}",
                file=sys.stderr,
            )
            print(
                "CRIITCAL: [COMPONENT: LOGGING] Consider opening a GitHub issue with the above details."
            )
            sys.exit(1)

        return logging.getLogger()

    def debug(self, message: str, component: str) -> None:
        """Verifies that the log level is equal to 0 (DEBUG).
        If the current log level is equal to 0 (DEBUG), then a log entry is written to the log file and a message is printed to STDOUT.


        Args:
        -----
            message (str): debug message
            component (str): The component that called `debug()` function
        """
        if self.level == 0:
            message = f"DEBUG: [COMPONENT: {component}] {message}"
            self.logger.debug(message)
            print(message, file=sys.stdout)

    def info(self, message: str, component: str) -> None:
        """Verifies that the log level is less than or equal to 1 (INFO).
        If the current log level is less than or equal to 1 (INFO), then a log entry is written to the log file and a message is printed to STDOUT.


        Args:
        -----
            message: info message
            component (str): The component that called `info()` function
        """
        if self.level <= 1:
            message = f"INFO: [COMPONENT: {component}] {message}"
            self.logger.info(message)
            print(message, file=sys.stdout)

    def error(self, message: str, component: str):
        """Verifies that the log level is less than or equal to 2 (ERROR).
        If the current log level is less than or equal to 2 (ERROR), then a log entry is written to the log file and a message is printed to STDERR.


        Args:
        -----
            message: error message
            component (str): The component that called `error()` function
        """
        if self.level <= 2:
            message = f"ERROR: [COMPONENT: {component}] {message}"
            self.logger.error(message)
            print(message, file=sys.stderr)

    def critical(self, message: str, component: str):
        """Verifies that the log level is less than or equal to 3 (CRITICAL).
        If the current log level is less than or equal to 3 (CRITICAL), then a log entry is written to the log file, a message is printed to STDERR, and the application exits with an exit status of 1.


        Args:
        -----
            message: critical message
            component (str): The component that called `critical()` function
        """
        if self.level <= 3:
            message = f"CRITICAL: [COMPONENT: {component}] {message} - Exiting."
            print(message, file=sys.stderr)
            self.logger.critical(message)
            sys.exit(1)

    def __get_log_level(self, log_level: int):
        match log_level:
            case 0:
                return logging.DEBUG
            case 1:
                return logging.INFO
            case 2:
                return logging.ERROR
            case 3:
                return logging.CRITICAL
            case _:
                return logging.DEBUG
