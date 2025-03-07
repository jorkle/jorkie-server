import cerberus
import yaml
import sys

from jorkieserver.utils import (
    file_exists,
    file_writable,
    get_file_contents,
    prompt_user,
)
from jorkieserver.types import Configuration
from jorkieserver.constants import LATEST_CONFIG_VERSION
from jorkieserver.logging import LogWriter


class Configurator:
    def __init__(self, log_writer: LogWriter, config_file_path: str):
        self.__log_writer = log_writer
        self.__config = None

    def get_configuration(self, config_file_path: str) -> Configuration:
        """Attempts to read the configuration file and return a Configuration object.
        Logic:
        ------
            If the configuration file does not exist, a default configuration file is generated.
            If the configuration file is not writable, a critical error is logged and the program exits.
            If the configuration file is not valid, a critical error is logged and the program exits.
            if the configuration is old, it is migrated to the new configuration format.
                If user input is required for the migration, the program exits.
                if user input is not required for the migratiom, the configuration is saved and the program continues.
            if the configuration file is valid, the configuration is loaded and the `Configuration` object is returned.

        Args:
        -----
            config_file_path (str): The path to the configuration file.

        Returns:
        --------
            Configuration: The configuration object containing the configuration values.
        """
        config_file_exists: bool = file_exists(config_file_path)

        if config_file_exists:
            self.__log_writer.debug("Config file exists.", component="CONFIGURATOR")
            config_file_contents: str = get_file_contents(
                config_file_path, log_writer=self.__log_writer
            )

            config_is_valid: bool = self.__validate_config(config_file_contents)
            if config_is_valid:
                self.__log_writer.debug(
                    "Config file is valid.", component="CONFIGURATOR"
                )
                # Get version of config
                config_version: str = self.__get_config_version(config_file_contents)
                if config_version == LATEST_CONFIG_VERSION:
                    self.__log_writer.debug(
                        "Config file is of the latest version.",
                        component="CONFIGURATOR",
                    )
                    configuration: Configuration = self.__load_config(
                        config_file_contents
                    )
                    self.__log_writer.info(
                        "Configuration loaded successfully.", component="CONFIGURATOR"
                    )
                    return configuration
                else:
                    # Config is of an older version. Migrates the current configuration to the latest version.
                    self.__log_writer.info(
                        "Config file contains an older configuration version.",
                        component="CONFIGURATOR",
                    )
                    # If manual intervention is required, the program exits.
                    self.__migrate_config(config_file_contents, config_file_path)
                    configuration: Configuration = self.__load_config(
                        config_file_contents
                    )
                    return configuration
            else:
                # Configuration file exists, but is invalid.
                self.__log_writer.error(
                    f"Config file '{config_file_path}' is not valid",
                    component="CONFIGURATOR",
                )

                # Prompt user to regenerate the configuration file. if user agrees, generate default config.
                # If user doesn't agree or 30 second timeout occurrs, log critical error and exit.
                question: str = """Config file exists, but is not valid.
                Do you want the current configuration file ({config_file_path}) regenerated?"""
                do_regenerate: bool = prompt_user(question=question)
                if do_regenerate:
                    self.__generate_config_file(config_file_path)
                    sys.exit(1)
                else:
                    self.__log_writer.critical(
                        f"Config file '{config_file_path}' is not valid and user chose not to regenerate.",
                        component="CONFIGURATOR",
                    )
                    sys.exit(1)

        else:
            # Config file doesn't exist at `config_file_path`. Generate default config.
            self.__generate_config_file(config_file_path)
            sys.exit(1)

    def __validate_config(self, config_file_contents: str) -> bool:
        try:
            yaml_data = yaml.safe_load(config_file_contents)
            schema = Schema()
            schema = schema.get_alpha_zero()
            v = cerberus.Validator()
            v.validate(yaml_data, schema)
            # TODO: Implement configuration validation logic.
            return True
        except Exception:
            return False

    def __get_config_version(self, config_file_contents: str) -> str:
        # TODO: Implement configuration version extraction logic.
        return "implement"

    def __load_config(self, config_file_contents: str) -> Configuration:
        # TODO: Implement configuration loading logic.
        yaml_data = yaml.safe_load(config_file_contents)
        return Configuration()

    def __migrate_config(self, file_contents: str, file_path: str) -> None:
        # TODO: Implement config migration logic.
        pass

    def __generate_config_file(self, config_file_path: str) -> None:
        pass


class Schema:
    def __init__(self):
        self.__schema = {}

    def get_alpha_zero(self) -> dict:
        alpha_zero_schema = {
            "schema_version": {
                "type": "string",
                "required": True,
                "database": {
                    "type": "dict",
                    "required": True,
                    "schema": {
                        "db_host": {
                            "type": "string",
                            "required": True,
                        },
                        "db_port": {
                            "type": "string",
                            "required": True,
                        },
                        "db_name": {
                            "type": "string",
                            "required": True,
                        },
                        "db_user": {
                            "type": "string",
                            "required": True,
                        },
                        "db_password": {
                            "type": "string",
                            "required": True,
                        },
                    },
                },
                "api": {
                    "type": "dict",
                    "required": True,
                    "schema": {
                        "api_host": {
                            "type": "string",
                            "required": True,
                        },
                        "api_port": {
                            "type": "string",
                            "required": True,
                        },
                        "api_key": {
                            "type": "string",
                            "required": True,
                        },
                    },
                },
            }
        }

        return alpha_zero_schema
