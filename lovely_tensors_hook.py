import os

ERROR_MESSAGE = """\
An error occurred while automatically hooking lovely_tensors.
If you uninstalled lovely_tensors, you should probably delete any 'lovely_tensors_hook.pth'
file on your system or unset your 'LOVELY_TENSORS' environment variable.
"""

try:
    if os.environ.get("LOVELY_TENSORS", "") not in {"", "0"}:
        import lovely_tensors
        lovely_tensors.monkey_patch()
except Exception as e:
    print(ERROR_MESSAGE)
    print(e)
    raise
