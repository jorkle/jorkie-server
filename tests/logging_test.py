import pytest
from unittest.mock import patch
from argparse import Namespace

from jorkieserver.server import Server


@pytest.fixture
def mock_parse_args():
    with patch("argparse.ArgumentParser.parse_args") as mock:
        yield mock


@pytest.fixture
def mock_log_dir():
    with patch("appdirs.user_log_dir") as mock:
        yield mock


@pytest.fixture(scope="session")
def temporary_log_dir(tmpdir_factory):
    log_dir = tmpdir_factory.mktemp("logs")
    yield log_dir


def test_logging_initialization(mock_parse_args, temporary_log_dir):
    mock_log_dir.return_value = temporary_log_dir
    args = Namespace()
    args.log_level = 1
    args.log_file = "default.log"
    args.config_file = "default.conf"
    mock_parse_args.return_value = args
    server = Server()
    assert server.cmd_opts.log_level == 1
    assert server.cmd_opts.log_file == "default.log"
    assert server.cmd_opts.config_file == "default.conf"
