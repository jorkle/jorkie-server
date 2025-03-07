import pytest
from unittest.mock import patch
from argparse import Namespace

from jorkieserver.server import Server


@pytest.fixture
def mock_parse_args():
    with patch("argparse.ArgumentParser.parse_args") as mock:
        yield mock


@patch.object(Server, "_Server__load_config", return_value="test")
@patch.object(Server, "_Server__init_components", return_value="test")
def test_default_arguments(load_config, init_components, mock_parse_args):
    args = Namespace()
    args.log_level = 1
    args.log_file = "default.log"
    args.config_file = "default.conf"
    mock_parse_args.return_value = args
    server = Server()
    assert server.cli_args.log_level == 1
    assert server.cli_args.log_file == "default.log"
    assert server.cli_args.config_file == "default.conf"


@patch.object(Server, "_Server__load_config", return_value="test")
@patch.object(Server, "_Server__init_components", return_value="test")
def test_custom_arguments(load_config, init_components, mock_parse_args):
    args = Namespace()
    args.log_level = 2
    args.log_file = "custom.log"
    args.config_file = "custom.conf"
    mock_parse_args.return_value = args
    server = Server()
    assert server.cli_args.log_level == 2
    assert server.cli_args.log_file == "custom.log"
    assert server.cli_args.config_file == "custom.conf"
