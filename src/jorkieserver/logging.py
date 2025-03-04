import logging
import sys
import os
import base64
from logging import Logger
import binascii


class Log:
    """
    Contains several merthods to log messages at different log levels.
    """

    def __init__(self, log_level: int, log_file: str, log_dir: str) -> None:
        self.level = log_level
        self.file = log_file
        self.__dir = self.__create_dir(log_dir)
        self.logger = self.__init_logger()

    def __init_logger(self) -> Logger:
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
                f"FATAL: [COMPONENT: LOGGING] Exception Details (base64 encoded): {self.__base64_encode(str(e))}",
                file=sys.stderr,
            )
            print(
                "CRIITCAL: [COMPONENT: LOGGING] Consider opening a GitHub issue with the above details."
            )
            sys.exit(1)

        return logging.getLogger()

    def __base64_encode(self, data: str) -> str:
        """
        Transforms a string (`data`) into a base64 encoded string

        Args:
        -----
            data (str): Input string to be base64 encoded

        Raises:
        -------
            UnicodeEncodeError: If the string cannot be encoded to bytes
            binascii.Error: If the bytes cannot be encoded to base64
            UnicodeDecodeError: If the base64 bytes cannot be decoded to string
            Exception: If an unknown error occurs

        Returns:
        --------
            str: base64 encoded string
        """
        try:
            string_bytes = data.encode("utf-8")
            base64_bytes = base64.b64encode(string_bytes)
            base64_string = base64_bytes.decode("utf-8")
        except UnicodeEncodeError:
            print(
                "CRITICAL: [COMPONENT: LOGGING] Failed to encode the string to bytes.",
                file=sys.stderr,
            )
            sys.exit(1)
        except binascii.Error:
            print(
                "CRITICAL: [COMPONENT: LOGGING] Failed to encode bytes to base64.",
                file=sys.stderr,
            )
            sys.exit(1)
        except UnicodeDecodeError:
            print(
                "CRITICAL: [COMPONENT: LOGGING] Failed to decode base64 bytes to string.",
                file=sys.stderr,
            )
            sys.exit(1)
        except Exception as e:
            print(
                "CRIITCAL: [COMPONENT: LOGGING] An unknown exception has occurred while encoding the string to base64.",
                file=sys.stderr,
            )
            print(
                f"CRIITCAL: [COMPONENT: LOGGING] Exception Details: {e}",
                file=sys.stderr,
            )
            print(
                "CRIITCAL: [COMPONENT: LOGGING] Consider opening a GitHub issue with the above details.",
                file=sys.stderr,
            )
            sys.exit(1)

        return base64_string

    def __create_dir(self, dir: str) -> str:
        """
        Creates a directory if it does not exist.

        Args:
        -----
            dir (str): path to the directory to be created

        Raises:
        -------
            PermissionError: If the user does not have permission to create the directory
            OSError: If the directory cannot be created
            Exception: If an unexpected error occurs

        Returns:
        --------
            str: The directory path that was created
        """
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)

        except PermissionError:
            print(
                f"CRITICAL: [COMPONENT: LOGGING] Insufficient permissions to create directory '{self.__dir}'.",
                file=sys.stderr,
            )
            sys.exit(1)
        except OSError:
            print(
                f"CRITICAL: [COMPONENT: LOGGING] OS error occurred while creating directory '{self.__dir}'.",
                file=sys.stderr,
            )
            sys.exit(1)
        except Exception as e:
            print(
                f"CRITICAL: [COMPONENT: LOGGING] Unexpected error occurred while creating directory '{self.__dir}'.",
                file=sys.stderr,
            )
            print(
                f"CRITICAL: [COMPONENT: LOGGING] Exception information (base64 encoded): {self.__base64_encode(str(e))}",
                file=sys.stderr,
            )
            print(
                "CRIITCAL: [COMPONENT: LOGGING] Consider opening a GitHub issue with the above details.",
                file=sys.stderr,
            )
            sys.exit(1)
        return dir

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
            message = f"CRITICAL: [COMPONENT: {component}] {message}"
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
