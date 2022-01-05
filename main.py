# Press the green button in the gutter to run the script.
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, CallbackContext

from utils import markup_start, reply_markup_callback, markup_qs1, init_quiz, markup_qs2, markup_qs3, markup_qs4, \
    markup_qs5, markup_last_menu


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Hello, I have 5 simple questions for you',
        reply_markup=markup_start()
    )


def qs1(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Questions 1.')
    query.edit_message_text(text='You have selected questions #1.')
    reply_markup_callback(update=update, text="Questions 1.", reply_markup=markup_qs1())
    return ConversationHandler.END


def qs2(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Questions 2.')
    query.edit_message_text(text='You have selected questions #2.')
    reply_markup_callback(
        update=update,
        text="Questions 2.",
        reply_markup=markup_qs2()
    )
    return ConversationHandler.END


def qs3(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Questions 3.')
    query.edit_message_text(text='You have selected questions #3.')
    reply_markup_callback(
        update=update,
        text="Questions 3.",
        reply_markup=markup_qs3()
    )
    return ConversationHandler.END


def qs4(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Questions 4.')
    query.edit_message_text(text='You have selected questions #4.')
    reply_markup_callback(
        update=update,
        text="Questions 4.",
        reply_markup=markup_qs4()
    )
    return ConversationHandler.END


def qs5(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Questions 5.')
    query.edit_message_text(text='You have selected questions #5.')
    reply_markup_callback(
        update=update,
        text="Questions 5.",
        reply_markup=markup_qs5()
    )
    return ConversationHandler.END


def last_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Last Menu')
    reply_markup_callback(
        update=update,
        text="Another menu",
        reply_markup=markup_last_menu()
    )
    return ConversationHandler.END


def correct_answer(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Correct Answer')
    query.edit_message_text(text='You have answered correctly 👌')
    init_quiz(update=update)
    return ConversationHandler.END


def wrong_answer(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Wrong Answer')
    query.edit_message_text(text='Your answer is not correct 😥')
    init_quiz(update=update)
    return ConversationHandler.END


if __name__ == '__main__':
    updater: Updater = Updater(token=os.environ['FIVE_QUESTIONS_BOT'], use_context=True)
    dp = updater.dispatcher

    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='qs1', callback=qs1),
            CallbackQueryHandler(pattern='qs2', callback=qs2),
            CallbackQueryHandler(pattern='qs3', callback=qs3),
            CallbackQueryHandler(pattern='qs4', callback=qs4),
            CallbackQueryHandler(pattern='qs5', callback=qs5),
            CallbackQueryHandler(pattern='last_menu', callback=last_menu),
            CallbackQueryHandler(pattern='correct_answer', callback=correct_answer),
            CallbackQueryHandler(pattern='wrong_answer', callback=wrong_answer),
        ],
        states={},
        fallbacks=[]
    ))

    # add handler
    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
