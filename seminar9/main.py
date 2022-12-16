import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
# from bot_commands import hi_command, hi_command, help_command, sum_command
import bot_commands as bc
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('tg_token')

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('sum_complex', bc.sum_complex))
updater.dispatcher.add_handler(CommandHandler('sub_complex', bc.sub_complex))
updater.dispatcher.add_handler(CommandHandler('mult_complex', bc.mult_complex))
updater.dispatcher.add_handler(CommandHandler('div_complex', bc.div_complex))
updater.dispatcher.add_handler(CommandHandler('sum_fraction', bc.sum_fraction))
updater.dispatcher.add_handler(CommandHandler('sub_fraction', bc.sub_fraction))
updater.dispatcher.add_handler(CommandHandler('mult_fraction', bc.mult_fraction))
updater.dispatcher.add_handler(CommandHandler('div_fraction', bc.div_fraction))


print('server start')
updater.start_polling()
updater.idle()
