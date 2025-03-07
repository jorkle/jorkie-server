import sys

from datetime import datetime
from appdirs import user_config_dir, user_log_dir, user_data_dir

APPLICATION_NAME = "Jorkie Server"
APPLICATION_DESCRIPTION = (
    "The server component of the Jorkie automated reconnaissance solution."
)
APPLICATION_USAGE = f"{sys.argv[0]} --help"

LAUNCH_TIMESTAMP = f"{datetime.now():%Y-%m-%dT%H-%M-%S}"

DEFAULT_CONFIG_DIR = user_config_dir("jorkie-server", "jorkle")
DEFAULT_LOG_DIR = user_log_dir("jorkie-server", "jorkle")
DEFAULT_DATA_DIR = user_data_dir("jorkie-server", "jorkle")
DEFAULT_LOG_LEVEL = 1  # 1=INFO
DEFAULT_LOG_FILE = f"{DEFAULT_LOG_DIR}/{LAUNCH_TIMESTAMP}.log"
DEFAULT_CONFIG_FILE = f"{DEFAULT_CONFIG_DIR}/config.yaml"

LATEST_CONFIG_VERSION = "alpha-one"
