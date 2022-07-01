import ctypes
import types

from libs.libslist import *
from database.basesqlite3 import *
from keyboards.keyboardd import *

API_TOKEN = '5065205436:AAETTxHahgYC0k1xwR4hxuoEOt-A8BQ6FHQ'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)