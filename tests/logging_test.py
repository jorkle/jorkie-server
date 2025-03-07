import pytest
from unittest.mock import patch
from argparse import Namespace
from jorkieserver.server import Server
from jorkieserver import server


@pytest.fixture(scope="session")
def mock_parse_args():
    with patch("argparse.ArgumentParser.parse_args") as mock:
        mock.return_value.log_level = 1
        mock.return_value.log_file = "default.log"
        mock.return_value.config_file = "default.conf"
        yield mock


@pytest.fixture(scope="session")
def mock_log_dir():
    with patch("appdirs.user_log_dir") as mock:
        yield mock


@pytest.fixture(scope="session")
def temporary_log_dir(tmpdir_factory):
    log_dir = tmpdir_factory.mktemp("logs")
    yield log_dir


@patch.object(Server, "_Server__load_config", return_value="test")
@patch.object(Server, "_Server__init_components", return_value="test")
def test_logging_initialization(
    load_config,
    init_components,
    mock_parse_args,
    mock_log_dir,
    temporary_log_dir,
):
    mock_parse_args.return_value.log_level = 1
    mock_parse_args.return_value.log_file = "default.log"
    mock_parse_args.return_value.config_file = "default.conf"
    mock_log_dir.return_value = temporary_log_dir
    server = Server()
    assert server.cli_args.log_level == 1
    assert server.cli_args.log_file == "default.log"
    assert server.cli_args.config_file == "default.conf"
