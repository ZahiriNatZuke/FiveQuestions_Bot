from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update


def markup_start() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Question 1', callback_data='qs1')],
        [InlineKeyboardButton(text='Question 2', callback_data='qs2')],
        [InlineKeyboardButton(text='Question 3', callback_data='qs3')],
        [InlineKeyboardButton(text='Question 4', callback_data='qs4')],
        [InlineKeyboardButton(text='Question 5', callback_data='qs5')]
    ])


def reply_markup_callback(update: Update, text: str, reply_markup: InlineKeyboardMarkup):
    update.callback_query.message.reply_text(text=text, reply_markup=reply_markup)


def init_quiz(update: Update):
    update.callback_query.message.reply_text(
        text='Hello, I have 5 simple questions for you',
        reply_markup=markup_start()
    )


def markup_qs1() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='A joke in bad taste', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Some kind of reptile', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='A programming language', callback_data='correct_answer')],
        [InlineKeyboardButton(text='An american football team', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='A bus stop', callback_data='wrong_answer')]
    ])


def markup_qs2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='1999', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='2022', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='1959', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='1969', callback_data='correct_answer')],
        [InlineKeyboardButton(text='1917', callback_data='wrong_answer')]
    ])


def markup_qs3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Mount Elbrús', callback_data='correct_answer')],
        [InlineKeyboardButton(text='Annapurna I', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Turquino Peak', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Dhaulagiri', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Mount Everest', callback_data='wrong_answer')]
    ])


def markup_qs4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Argentina', callback_data='correct_answer')],
        [InlineKeyboardButton(text='Egypt', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Spain', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Ecuador', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Malaysia', callback_data='wrong_answer')]
    ])


def markup_qs5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Baconao', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Twister', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Marengo ', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Palmiche', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Rocinante', callback_data='correct_answer')]
    ])
