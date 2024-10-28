__version__ = "0.1.17"

import os

from .repr_str import *
from .repr_rgb import *
from .repr_plt import *
from .repr_chans import *
from .patch import *
from .utils import *

if os.environ.get("LOVELY_TENSORS", "") == "upon_import":
    monkey_patch()
