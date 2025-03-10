import pytest
from unittest.mock import patch
from argparse import Namespace

from jorkieserver.server import Server


@pytest.fixture
def mock_parse_args():
    with patch("argparse.ArgumentParser.parse_args") as mock:
        yield mock


def test_default_arguments(mock_parse_args):
    args = Namespace()
    args.log_level = 1
    args.log_file = "default.log"
    args.config_file = "default.conf"
    mock_parse_args.return_value = args
    server = Server()
    assert server.cmd_opts.log_level == 1
    assert server.cmd_opts.log_file == "default.log"
    assert server.cmd_opts.config_file == "default.conf"


def test_custom_arguments(mock_parse_args):
    args = Namespace()
    args.log_level = 2
    args.log_file = "custom.log"
    args.config_file = "custom.conf"
    mock_parse_args.return_value = args
    server = Server()
    assert server.cmd_opts.log_level == 2
    assert server.cmd_opts.log_file == "custom.log"
    assert server.cmd_opts.config_file == "custom.conf"
