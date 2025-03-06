import binascii
import base64
import sys
import os


def file_exists(file_path: str) -> bool:
    """Determines if a file exists.

    Args:
    -----
        file_path (str): The file path to check for existence.

    Returns:
    --------
        bool: True if the file exists, false otherwise.
    """
    try:
        return os.path.exists(file_path)
    except Exception:
        return False


def file_writable(file_path: str) -> bool:
    """Determines if the file location `file_path` is writable.

    Args:
    -----
        file_path (str): The file path to check for writability.

    Returns:
    --------
        bool: True if the file is writable, false otherwise.
    """
    try:
        with open(file_path, "a"):
            return True
    except Exception:
        return False


def get_file_contents(file_path: str) -> str | bool:
    """Reads the contents of the file at the given path.
    Returns the contnets of the file if it exists, otherwise returns False.

    Args:
    -----
        file_path (str): The path to the file to read.

    Returns:
    --------
        bool | str: The contents of the file if it exists. If an error occurs, returns False.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception:
        return False


def base64_encode(data: str, component: str) -> str:
    """
    Transforms a string (`data`) into a base64 encoded string

    Args:
    -----
        data (str): Input string to be base64 encoded
        component (str): The component that called the function

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
            f"CRITICAL: [COMPONENT: {component}] Failed to encode the string to bytes.",
            file=sys.stderr,
        )
        sys.exit(1)
    except binascii.Error:
        print(
            f"CRITICAL: [COMPONENT: {component}] Failed to encode bytes to base64.",
            file=sys.stderr,
        )
        sys.exit(1)
    except UnicodeDecodeError:
        print(
            f"CRITICAL: [COMPONENT: {component}] Failed to decode base64 bytes to string.",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(
            f"CRIITCAL: [COMPONENT: {component}] An unknown exception has occurred while encoding the string to base64.",
            file=sys.stderr,
        )
        print(
            f"CRIITCAL: [COMPONENT: {component}] Exception Details: {e}",
            file=sys.stderr,
        )
        print(
            f"CRIITCAL: [COMPONENT: {component}] Consider opening a GitHub issue with the above details.",
            file=sys.stderr,
        )
        sys.exit(1)

    return base64_string


def create_directory(dir: str, component: str) -> str:
    """
    Creates a directory if it does not exist.

    Args:
    -----
        dir (str): path to the directory to be created
        component (str): name of the component that is creating the directory

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
            f"CRITICAL: [COMPONENT: {component}] Insufficient permissions to create directory '{dir}'.",
            file=sys.stderr,
        )
        sys.exit(1)
    except OSError:
        print(
            f"CRITICAL: [COMPONENT: {component}] OS error occurred while creating directory '{dir}'.",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(
            f"CRITICAL: [COMPONENT: {component}] Unexpected error occurred while creating directory '{dir}'.",
            file=sys.stderr,
        )
        print(
            f"CRITICAL: [COMPONENT: {component}] Exception information (base64 encoded): {base64_encode(str(e), component)}",
            file=sys.stderr,
        )
        print(
            f"CRIITCAL: [COMPONENT: {component}] Consider opening a GitHub issue with the above details.",
            file=sys.stderr,
        )
        sys.exit(1)
    return dir
