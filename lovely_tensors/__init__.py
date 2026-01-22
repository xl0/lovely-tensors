__version__ = "0.1.21"

from .repr_str import *
from .repr_rgb import *
from .repr_plt import *
from .repr_chans import *
from .patch import *
from .utils import *

import os
if os.environ.get("LOVELY_TENSORS", "").strip().lower() in {"1", "true", "yes"}:
    monkey_patch()