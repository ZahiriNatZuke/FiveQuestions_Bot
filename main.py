# Press the green button in the gutter to run the script.
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, CallbackContext

from utils import markup_start, reply_markup_callback, markup_qs1, init_quiz, markup_qs2, markup_qs3, markup_qs4, \
    markup_qs5


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Hello, I have 5 simple questions for you',
        reply_markup=markup_start()
    )


def qs1_callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Question 1.')
    query.edit_message_text(text='You have selected question #1.')
    reply_markup_callback(update=update, text="What is Python?", reply_markup=markup_qs1())
    return ConversationHandler.END


def qs2_callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Question 2.')
    query.edit_message_text(text='You have selected question #2.')
    reply_markup_callback(
        update=update,
        text="In what year did man reach the moon?",
        reply_markup=markup_qs2()
    )
    return ConversationHandler.END


def qs3_callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Question 3.')
    query.edit_message_text(text='You have selected question #3.')
    reply_markup_callback(
        update=update,
        text="What is the highest mountain in Europe?",
        reply_markup=markup_qs3()
    )
    return ConversationHandler.END


def qs4_callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Question 4.')
    query.edit_message_text(text='You have selected question #4.')
    reply_markup_callback(
        update=update,
        text="In which country is Aconcagua peak located?",
        reply_markup=markup_qs4()
    )
    return ConversationHandler.END


def qs5_callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Question 5.')
    query.edit_message_text(text='You have selected question #5.')
    reply_markup_callback(
        update=update,
        text="What is the name of Don Quixote de la Mancha's horse?",
        reply_markup=markup_qs5()
    )
    return ConversationHandler.END


def correct_answer_callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer('Correct Answer')
    query.edit_message_text(text='You have answered correctly 👌')
    init_quiz(update=update)
    return ConversationHandler.END


def wrong_answer_callback_handler(update: Update, context: CallbackContext) -> None:
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
            CallbackQueryHandler(pattern='qs1', callback=qs1_callback_handler),
            CallbackQueryHandler(pattern='qs2', callback=qs2_callback_handler),
            CallbackQueryHandler(pattern='qs3', callback=qs3_callback_handler),
            CallbackQueryHandler(pattern='qs4', callback=qs4_callback_handler),
            CallbackQueryHandler(pattern='qs5', callback=qs5_callback_handler),
            CallbackQueryHandler(pattern='correct_answer', callback=correct_answer_callback_handler),
            CallbackQueryHandler(pattern='wrong_answer', callback=wrong_answer_callback_handler),
        ],
        states={},
        fallbacks=[]
    ))

    # add handler
    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
