from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand

vup = InlineKeyboardButton('🔈 ⬆️', callback_data='vup')
vdown = InlineKeyboardButton('🔈 ⬇️', callback_data='vdown')
vmute = InlineKeyboardButton('🔇', callback_data='vmute')

screen = InlineKeyboardButton('📺', callback_data='screen')
clip = InlineKeyboardButton('📋', callback_data='clip')
getlink = InlineKeyboardButton('🔗', callback_data='getlink')
close = InlineKeyboardButton('⛔️', callback_data='close')
status = InlineKeyboardButton('ℹ️', callback_data='status')

controller_kb = InlineKeyboardMarkup(row_width=3).row(vup, vdown, vmute)
controller_kb.row(screen, clip, getlink, status)
controller_kb.row(close)

start_text = "• *Remote PC*\n \
/controller - _Control with buttons_\n\n \
/shutdown - _Shutdown_\n \
/restart - _Restart PC_\n\n\
• *Search*\n \
/youtube <query> - _Search in youtube_\n \
/google <query> - _Search in google_\n\n \
• *Write*\n \
/write <text> - _Write text_\n \
/url <query> - _Open url_\n \
/alert <text> - _Show alert_\n\n\
/start - _Get this text_"

control_text = "• *Controller*\n \
🔈 ⬆️ - _Volume Up_\n \
🔈 ⬇️ - _Volume Down_\n \
🔇 - _Volume Mute_\n \
📺 - _Get screenshot_\n \
📋 - _Get clipboard_\n \
🔗 - _Get browser page link_\n \
⛔️ - Close current app\n\n \
/start - Start message"

commands = '[\
{"command":"start", "description":"Basic commands"},\
{"command":"controller", "description":"Bot\'s controller"},\
{"command":"youtube", "description":"Start youtube"},\
{"command":"write", "description":"Write text"},\
{"command":"url", "description":"Open url"},\
{"command":"alert", "description":"Show alert"}\
]'