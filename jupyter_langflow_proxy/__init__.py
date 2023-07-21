"""
Return config on servers to start for langflow

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_langflow():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "langflow.svg"
        )

    # Make sure executable is in $PATH
    def _get_langflow_command(port):
        executable = "make"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find make executable in $PATH")
        return ["langflow", "--port", f"{port}"]

    return {
        "command": _get_langflow_command,
        "timeout": 20,
        "launcher_entry": {
            "title": "langflow",
            "icon_path": _get_icon_path()
        },
        "absolute_url": True,
        "new_browser_tab": True,
    }
