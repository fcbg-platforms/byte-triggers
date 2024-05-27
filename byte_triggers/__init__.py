from . import io, lsl, mock, parallel, utils
from ._version import __version__
from .lsl import LSLTrigger
from .mock import MockTrigger
from .parallel import ParallelPortTrigger
from .utils.config import sys_info
from .utils.logs import add_file_handler, set_log_level
