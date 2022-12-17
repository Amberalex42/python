from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import fractions
from spy import *


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'''
Этот бот может делать арифметические действия с комплексными и рациональными числами.
Введите нужную команду:
/sum_complex a b - сумма комплексных чисел a и b,
/sub_complex a b - разность комплексных чисел a и b,
/mult_complex a b - умножение комплексных чисел a и b,
/div_complex a b - деление комплексных чисел a и b,
/sum_fraction a b c d - сумма рациональных чисел a/b и c/d,
/sub_fraction a b c d - разность рациональных чисел a/b и c/d,
/mult_fraction a b c d - умножение рациональных чисел a/b и c/d,
/div_fraction a b c d - деление рациональных чисел a/b и c/d
''')


def sum_complex(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} + {y} = {get_sum(x, y)}')


def sub_complex(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} - {y} = {get_sub(x, y)}')


def mult_complex(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} * {y} = {get_mult(x, y)}')


def div_complex(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} / {y} = {get_div(x, y)}')


def sum_fraction(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = fractions.Fraction(int(items[1]), int(items[2]))
    y = fractions.Fraction(int(items[3]), int(items[4]))
    update.message.reply_text(f'{x} + {y} = {get_sum(x, y)}')


def sub_fraction(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = fractions.Fraction(int(items[1]), int(items[2]))
    y = fractions.Fraction(int(items[3]), int(items[4]))
    update.message.reply_text(f'{x} - {y} = {get_sub(x, y)}')


def mult_fraction(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = fractions.Fraction(int(items[1]), int(items[2]))
    y = fractions.Fraction(int(items[3]), int(items[4]))
    update.message.reply_text(f'{x} * {y} = {get_mult(x, y)}')


def div_fraction(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = fractions.Fraction(int(items[1]), int(items[2]))
    y = fractions.Fraction(int(items[3]), int(items[4]))
    update.message.reply_text(f'{x} / {y} = {get_div(x, y)}')


def get_sum(x, y):
    return x + y


def get_sub(x, y):
    return x - y


def get_mult(x, y):
    return x * y


def get_div(x, y):
    return x / y
