__version__ = "1.0"
__author__ = "SenuGamerBoy"
__license__ = "LGPLv3"


# External api
from .kafy import new
from .kafy import set_api_key
from .kafy import load_cache, dump_cache
from .kafy import get_categoryname
from .kafy import backend
from .util import GdataError, call_gdata
from .playlist import get_playlist, get_playlist2
from .channel import get_channel
