from _pytest.tmpdir import tmp_path_factory
import logging
import pytest
from unittest.mock import MagicMock, patch
from jorkieserver.configurator import Configurator
from jorkieserver.logger import LogWriter
from jorkieserver.types import Configuration


@pytest.fixture(scope="session")
def temporary_log_dir(tmpdir_factory):
    log_dir = tmpdir_factory.mktemp("logs")
    yield log_dir


@pytest.fixture(scope="session")
def log_writer(temporary_log_dir):
    log_writer = LogWriter(0, f"{temporary_log_dir}/test.log", temporary_log_dir)
    yield log_writer


@pytest.fixture(scope="session")
def get_fake_config_no_exist(temporary_log_dir):
    return f"{temporary_log_dir}/test_config_no_exist.yaml"


@pytest.fixture(scope="session")
def get_fake_config_valid(temporary_log_dir):
    test_yaml_data = """api:
  api_host: 127.0.0.1
  api_key: SECRET_KEY
  api_port: 8000
config_version: alpha-one
database:
  db_host: 127.0.0.1
  db_name: jorkieserver
  db_password: TestPassword123
  db_port: 3306
  db_user: jorkie
"""
    fake_config_file_valid = f"{temporary_log_dir}/test_config_valid.yaml"
    with open(fake_config_file_valid, "w") as f:
        f.write(test_yaml_data)
    return fake_config_file_valid


def test_config_does_not_exist(log_writer, get_fake_config_no_exist, caplog):
    with pytest.raises(SystemExit) as e:
        with caplog.at_level(logging.INFO):
            caplog.set_level(logging.INFO)
            configurator = Configurator(log_writer, get_fake_config_no_exist)
            configurator.get_configuration(get_fake_config_no_exist)
            assert "Configuration file generated. Please edit" in caplog.text
            assert e.type is SystemExit
            assert e.value.code == 0


def test_config_file_valid(log_writer, get_fake_config_valid, caplog):
    with caplog.at_level(logging.DEBUG):
        caplog.set_level(logging.DEBUG)
        configurator = Configurator(log_writer, get_fake_config_valid)
        configuration = configurator.get_configuration(get_fake_config_valid)
        assert configuration.api_host == "127.0.0.1"
        assert "Config file is valid" in caplog.text
        assert "Config file is of the latest version" in caplog.text


@pytest.fixture(scope="session")
def get_fake_config_valid_and_old(temporary_log_dir):
    test_yaml_data = """api:
  api_host: 127.0.0.1
  api_key: SECRET_KEY
  api_port: 8000
config_version: alpha-zero
database:
  db_host: 127.0.0.1
  db_name: jorkieserver
  db_password: TestPassword123
  db_port: 3306
  db_user: jorkie
"""
    fake_config_file_valid = f"{temporary_log_dir}/test_config_valid.yaml"
    with open(fake_config_file_valid, "w") as f:
        f.write(test_yaml_data)
    return fake_config_file_valid


def test_config_file_valid_and_old(log_writer, get_fake_config_valid_and_old, caplog):
    with caplog.at_level(logging.INFO):
        caplog.set_level(logging.INFO)
        configurator = Configurator(log_writer, get_fake_config_valid_and_old)
        configuration = configurator.get_configuration(get_fake_config_valid_and_old)
        assert "Configuration migrated to alpha-one" in caplog.text
        assert configuration.config_version == "alpha-one"
