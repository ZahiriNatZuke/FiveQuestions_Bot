from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update


def markup_start() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Questions 1', callback_data='qs1')],
        [InlineKeyboardButton(text='Questions 2', callback_data='qs2')],
        [InlineKeyboardButton(text='Questions 3', callback_data='qs3')],
        [InlineKeyboardButton(text='Questions 4', callback_data='qs4')],
        [InlineKeyboardButton(text='Questions 5', callback_data='qs5')]
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
        [InlineKeyboardButton(text='Questions 1.1', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 1.2', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 1.3', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 1.4', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 1.5', callback_data='last_menu')]
    ])


def markup_qs2() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Questions 2.1', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 2.2', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 2.3', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 2.4', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 2.5', callback_data='last_menu')]
    ])


def markup_qs3() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Questions 3.1', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 3.2', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 3.3', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 3.4', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 3.5', callback_data='last_menu')]
    ])


def markup_qs4() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Questions 4.1', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 4.2', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 4.3', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 4.4', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 4.5', callback_data='last_menu')]
    ])


def markup_qs5() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Questions 5.1', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 5.2', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 5.3', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 5.4', callback_data='last_menu')],
        [InlineKeyboardButton(text='Questions 5.5', callback_data='last_menu')]
    ])


def markup_last_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Answer #1', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Answer #2', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Answer #3', callback_data='wrong_answer')],
        [InlineKeyboardButton(text='Answer #4', callback_data='correct_answer')],
        [InlineKeyboardButton(text='Answer #5', callback_data='wrong_answer')]
    ])
