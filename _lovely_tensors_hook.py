"""
This file should never be imported or executed by the user.

It gets called by the site hook `_lovely_tensors_hook.pth` which in turn gets
called automatically by python upon startup (https://docs.python.org/3/library/site.html)
if the package lovely-tensors is installed.

If the LOVEY_TENSORS environment variable is set to a "truthy" value, import and monkey patch.
"""
import os
import sys


if os.environ.get("LOVELY_TENSORS", "").lower() in {"1", "true", "yes"}:
    try:
        import lovely_tensors
        lovely_tensors.monkey_patch()
    except Exception as e:
        ERROR_MESSAGE = """\
Error: lovely_tensors.monkey_patch() failed with:

{}

If you uninstalled lovely_tensors, you should delete any '_lovely_tensors_hook.pth'
file on your system and unset your 'LOVELY_TENSORS' environment variable.
"""
        print(ERROR_MESSAGE.format(e), file=sys.stderr)
        raise
