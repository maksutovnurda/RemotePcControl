from aiogram import Bot, Dispatcher, executor, filters, types
import configparser
import asyncio
import mss
import control
import urllib
import keyborads as kb

config = configparser.ConfigParser()
config.read('config.ini')
bot_token = config.get('bot_config', 'bot_token')
owner = config.get('bot_config', 'owner_username')
browser_path = config.get('bot_config', 'browser_path')
browser_name = config.get('bot_config', 'browser_name')

API_TOKEN = bot_token

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['youtube'])
async def send_welcome(message: types.Message):
	if message.from_user.username == owner:
		text = message.text.split(' ', 1)
		if len(text)>1:
			query = urllib.parse.quote_plus(text[1])
			control.openSite(browser_name, browser_path, 'youtube.com/results?search_query='+query)
		else:
			control.openSite(browser_name, browser_path, 'youtube.com')
@dp.message_handler(commands=['google'])
async def send_welcome(message: types.Message):
	if message.from_user.username == owner:
		text = message.text.split(' ', 1)
		if len(text)>1:
			query = urllib.parse.quote_plus(text[1])
			control.openSite(browser_name, browser_path, 'http://google.com/search?q='+query)
		else:
			control.openSite(browser_name, browser_path, 'google.com')
@dp.message_handler()
async def echo(message: types.Message):
	if message.from_user.username != owner:
		pass
	elif message.text == '/start':
		await bot.set_my_commands(kb.commands)
		await bot.send_message(message.from_user.id, kb.start_text, parse_mode='markdown')
	elif message.text == '/controller':
		await bot.send_message(message.from_user.id, kb.control_text, parse_mode='markdown', reply_markup=kb.controller_kb)
	elif message.text == '/shutdown':
		control.shutdown()
	elif message.text == '/restart':
		control.restart()	
	elif message.text == '/status':
		await bot.send_message(message.from_user.id, control.status(), parse_mode='markdown')	
	elif message.text.startswith('/url'):
		control.openSite(browser_name, browser_path, message.text.split(' ', 1)[1])
	elif message.text.startswith('/write'):
		control.write(message.text.split(' ', 1)[1])
	elif message.text.startswith('/alert'):
		control.alert(message.text.split(' ', 1)[1])
@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
	code = callback_query.data
	if callback_query.from_user.username != owner:
		pass
	elif code == 'vup':
		control.press('volumeup', 5)
	elif code == 'vdown':
		control.press('volumedown', 5)
	elif code == 'vmute':
		control.press('volumemute', 1)
	elif code == 'close':
		control.close()
	elif code == 'getlink':
		await bot.send_message(callback_query.from_user.id, control.getPageLink())
	elif code == 'clip':
		await bot.send_message(callback_query.from_user.id, control.getClipBoard())
	elif code == 'screen':
		await types.ChatActions.upload_photo()
		media = types.MediaGroup()
		mss.mss().shot(output="screen.png")
		media.attach_photo(types.InputFile("screen.png"), '')
		await bot.send_media_group(callback_query.from_user.id, media=media)
	elif code == 'status':
		await bot.send_message(callback_query.from_user.id, control.status(), parse_mode='markdown')
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)