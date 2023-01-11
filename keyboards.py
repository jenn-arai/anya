import random
from telegram import *
from exam_test import questions
from keys import bot

# orange
button1 = InlineKeyboardButton("يي", callback_data='yes')
button2 = InlineKeyboardButton("لا", callback_data='no')
orange_keyboard = InlineKeyboardMarkup([[button1, button2]])
likes = 0
dislikes = 0

# help
convert_button = InlineKeyboardButton('تحويلات انظمة الارقام', callback_data='convert numbers')
help_keyboard = InlineKeyboardMarkup([[convert_button]])

# convert
converting_dict = {'dec2bi': [], 'dec2oct': [], 'dec2hex': [], 'hex2dec': [], 'oct2dec': [], 'bi2dec': []}

again_btn = InlineKeyboardButton('مرة ثانية', callback_data='again')

dec_to_bi_btn = InlineKeyboardButton('عشري الى ثنائي', callback_data='dec_to_bi')
dec_to_oct_btn = InlineKeyboardButton('عشري الى ثماني', callback_data='dec_to_oct')
dec_to_hex_btn = InlineKeyboardButton('عشري الى سداسي عشر', callback_data='dec_to_hex')

bi_to_dec_btn = InlineKeyboardButton('ثنائي الى عشري', callback_data='bi_to_dec')
oct_to_dec_btn = InlineKeyboardButton('ثماني الى عشري', callback_data='oct_to_dec')
hex_to_dec_btn = InlineKeyboardButton('سداسي عشر الى عشري', callback_data='hex_to_dec')
converts_keyboard = InlineKeyboardMarkup(
    [[dec_to_bi_btn, bi_to_dec_btn], [dec_to_oct_btn, oct_to_dec_btn], [dec_to_hex_btn, hex_to_dec_btn]])

# ~~~~~~~~~~~~~~~~~~~~ امتحان ~~~~~~~~~~~~~~~~~~
exam_dict = {}  # takes 'username': { 'index: 0', score: 0}
start_exam_button = InlineKeyboardButton('ابداء الامتحان', callback_data='start exam')
exam_keyboard = InlineKeyboardMarkup([[start_exam_button]])
settings_buttons = [[InlineKeyboardButton('ترجم', callback_data='translate'), InlineKeyboardButton('الغاء', callback_data='cancel exam')]]

def exam_btn_gen(user):
    global exam_dict
    question = questions[exam_dict[user]['index']]
    print(question)
    false_answers = question['answers']['false']
    false_answers = false_answers[:3] if len(false_answers) >= 4 else false_answers
    correct_answers = question['answers']['correct']
    answers = false_answers + correct_answers
    # print(f'answers are {answers}')
    random.shuffle(answers)
    # print(f'shuffled answers are {answers}')
    buttons = [InlineKeyboardButton(x, callback_data=x) for x in answers]
    # print(f'buttons is {buttons}')
    keyboard = InlineKeyboardMarkup(settings_buttons + [[btn] for btn in buttons])
    # print(f'keyboard is {keyboard}')

    return keyboard, correct_answers[0], question['question']
    # a list of buttons( the keyboard), the answer button callback and the question


# ~~~~~~~~~~~~~~~~~~~~ امتحان ~~~~~~~~~~~~~~~~~~


def query_handler(update, context):
    global likes, dislikes
    query = update.callback_query
    # update.callback_query.answer
    # برتقال
    if "yes" in query.data:
        likes += 1
        query.edit_message_text(text='حلووو البرتقال صار عندة ' + str(likes + 1) + ' لايك انيا تحب البرتقال ☺')

    if "no" in query.data:
        dislikes += 1
        query.edit_message_text(text='اوبسي بس البرتقال طيب .. البرتقال صار عندة ' + str(dislikes) + ' دسلايك 🤦')

    # المساعدة
    if 'convert numbers' in query.data:
        query.edit_message_text(text='اختار نوع التحويل', reply_markup=converts_keyboard)

    # التحويلات
    if 'dec_to_bi' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['dec2bi'].append(user)
        print(converting_dict['dec2bi'])
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير باينري',
                                reply_markup=InlineKeyboardMarkup([[again_btn]]))
    elif 'dec_to_oct' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['dec2oct'].append(user)
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير اوكتال',
                                reply_markup=InlineKeyboardMarkup([[again_btn]]))
    elif 'dec_to_hex' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['dec2hex'].append(user)
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير هكزادسمل',
                                reply_markup=InlineKeyboardMarkup([[again_btn]]))

    elif 'bi_to_dec' in query.data:
        print(query)
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['bi2dec'].append(user)
        print(converting_dict['bi2dec'])
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير عشري',
                                reply_markup=InlineKeyboardMarkup([[again_btn]]))
    elif 'oct_to_dec' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['oct2dec'].append(user)
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير عشري',
                                reply_markup=InlineKeyboardMarkup([[again_btn]]))
    elif 'hex_to_dec' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['hex2dec'].append(user)
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير عشري',
                                reply_markup=InlineKeyboardMarkup([[again_btn]]))

    if 'again' in query.data:
        query.edit_message_text(text='اختار نوع التحويل', reply_markup=converts_keyboard)

    # امتحان
    if 'start exam' in query.data:    # if the user clicks start
        user = query.from_user['username']
        exam_dict.update({user: {'index': 0, 'score': 0, 'ar': False}})  # add a user
        keyboard, correct_ans, question = exam_btn_gen(user)
        query.edit_message_text(text='تمام ' + '\n' + question[0], reply_markup=keyboard)  # ask a question
        # start asking questions
    elif query.from_user['username'] not in exam_dict.keys():
        bot.answer_callback_query(query.id, text='مو امتحانك 🙂 ', show_alert=True)
    elif exam_dict:

        if query.data in exam_btn_gen(query.from_user['username']):  # if the user clicks one of the correct answers
            exam_dict[query.from_user['username']]['index'] += 1
            # exam_dict[query.from_user['username']]['score'] += 1
            if exam_dict[query.from_user['username']]['index'] != len(questions): # if the index doesn't equal the length of the questions list
                index = exam_dict[query.from_user['username']]['index']
                keyboard, correct_ans, question = exam_btn_gen(query.from_user['username'])
                query.edit_message_text(text=f'{index}/{len(questions)}' + '\n' + f'{question[0]}',
                                        reply_markup=keyboard)
            else:    # if the exam finish
                mistakes = exam_dict[query.from_user['username']]['score']
                query.edit_message_text(text=f'عفية خلصت المتحان' + '\n' + f' عدد الاخطاء {mistakes}',
                                        reply_markup=exam_keyboard)
                update.send_message(update.message.chat.id, '🙂')

        elif 'cancel exam' in query.data:
            exam_dict.pop(query.from_user['username'])         # delete the username from the exam dictionary
            query.edit_message_text(text='تم الغاء الامتحان', reply_markup=exam_keyboard)   # change the message
        elif 'translate' in query.data:
            exam_dict[query.from_user['username']]['ar'] = not exam_dict[query.from_user['username']]['ar']    # *
            trans_state = 1 if exam_dict[query.from_user['username']]['ar'] else 0

            # exam_dict[query.from_user['username']]['index'] += 1
            # exam_dict[query.from_user['username']]['score'] += 1
            index = exam_dict[query.from_user['username']]['index']
            keyboard, correct_ans, question = exam_btn_gen(query.from_user['username'])
            query.edit_message_text(text=f'{index}/{len(questions)}' + '\n' + f'{question[trans_state]}',   # *
                                    reply_markup=keyboard)
        else:    # if the user clicks the wrong answer
            print(f"answer is {exam_btn_gen(query.from_user['username'])[2]}")
            # exam_dict[query.from_user['username']]['index'] += 1
            exam_dict[query.from_user['username']]['score'] += 1
            index = exam_dict[query.from_user['username']]['index']
            keyboard, correct_ans, question = exam_btn_gen(query.from_user['username'])
            query.edit_message_text(text=f'{index}/{len(questions)}' + '\n' + 'خطاء حاول مرة ثانية' + '\n'
                                         + question[0], reply_markup=keyboard)

            # print(f'likes ---> {likes}, and dislikes ----> {dislikes}')

