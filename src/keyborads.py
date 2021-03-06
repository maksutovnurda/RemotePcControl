from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand

vup = InlineKeyboardButton('đ âŦī¸', callback_data='vup')
vdown = InlineKeyboardButton('đ âŦī¸', callback_data='vdown')
vmute = InlineKeyboardButton('đ', callback_data='vmute')

screen = InlineKeyboardButton('đē', callback_data='screen')
clip = InlineKeyboardButton('đ', callback_data='clip')
getlink = InlineKeyboardButton('đ', callback_data='getlink')
close = InlineKeyboardButton('âī¸', callback_data='close')
status = InlineKeyboardButton('âšī¸', callback_data='status')

controller_kb = InlineKeyboardMarkup(row_width=3).row(vup, vdown, vmute)
controller_kb.row(screen, clip, getlink, status)
controller_kb.row(close)

start_text = "âĸ *Remote PC*\n \
/controller - _Control with buttons_\n\n \
/shutdown - _Shutdown_\n \
/restart - _Restart PC_\n\n\
âĸ *Search*\n \
/youtube <query> - _Search in youtube_\n \
/google <query> - _Search in google_\n\n \
âĸ *Write*\n \
/write <text> - _Write text_\n \
/url <query> - _Open url_\n \
/alert <text> - _Show alert_\n\n\
/start - _Get this text_"

control_text = "âĸ *Controller*\n \
đ âŦī¸ - _Volume Up_\n \
đ âŦī¸ - _Volume Down_\n \
đ - _Volume Mute_\n \
đē - _Get screenshot_\n \
đ - _Get clipboard_\n \
đ - _Get browser page link_\n \
âī¸ - Close current app\n\n \
/start - Start message"

commands = '[\
{"command":"start", "description":"Basic commands"},\
{"command":"controller", "description":"Bot\'s controller"},\
{"command":"youtube", "description":"Start youtube"},\
{"command":"write", "description":"Write text"},\
{"command":"url", "description":"Open url"},\
{"command":"alert", "description":"Show alert"}\
]'