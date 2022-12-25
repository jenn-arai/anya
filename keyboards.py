from telegram import *

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
converting_dict = {'dec2bi': ['Jenn_FrEbzz'], 'dec2oct': [], 'dec2hex': [], 'hex2dec': [], 'oct2dec': [], 'bi2dec': []}

again_btn = InlineKeyboardButton('مرة ثانية', callback_data='again')

dec_to_bi_btn = InlineKeyboardButton('عشري الى ثنائي', callback_data='dec_to_bi')
dec_to_oct_btn = InlineKeyboardButton('عشري الى ثماني', callback_data='dec_to_oct')
dec_to_hex_btn = InlineKeyboardButton('عشري الى سداسي عشر', callback_data='dec_to_hex')

bi_to_dec_btn = InlineKeyboardButton('ثنائي الى عشري', callback_data='bi_to_dec')
oct_to_dec_btn = InlineKeyboardButton('ثماني الى عشري', callback_data='oct_to_dec')
hex_to_dec_btn = InlineKeyboardButton('سداسي عشر الى عشري', callback_data='hex_to_dec')
converts_keyboard = InlineKeyboardMarkup([[dec_to_bi_btn, bi_to_dec_btn], [dec_to_oct_btn, oct_to_dec_btn], [dec_to_hex_btn, hex_to_dec_btn]])






def query_handler(update, context):
    global likes, dislikes
    query = update.callback_query
    # update.callback_query.answer
    # برتقال
    if "yes" in query.data:
        likes += 1
        query.edit_message_text(text='حلووو البرتقال صار عندة ' + str(likes+1) + ' لايك انيا تحب البرتقال ☺')

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
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير باينري' , reply_markup=InlineKeyboardMarkup([[again_btn]]))
    elif 'dec_to_oct' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['dec2oct'].append(user)
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير اوكتال', reply_markup=InlineKeyboardMarkup([[again_btn]]))
    elif 'dec_to_hex' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['dec2hex'].append(user)
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير هكزادسمل', reply_markup=InlineKeyboardMarkup([[again_btn]]))

    elif 'bi_to_dec' in query.data:
        print(query)
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['bi2dec'].append(user)
        print(converting_dict['bi2dec'])
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير عشري', reply_markup=InlineKeyboardMarkup([[again_btn]]))
    elif 'oct_to_dec' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['oct2dec'].append(user)
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير عشري', reply_markup=InlineKeyboardMarkup([[again_btn]]))
    elif 'hex_to_dec' in query.data:
        user = query.from_user['username']
        print(user + 'have been added to the dict')
        converting_dict['hex2dec'].append(user)
        query.edit_message_text(text='يلا دز الرقم الي تريده يصير عشري', reply_markup=InlineKeyboardMarkup([[again_btn]]))

    if 'again' in query.data:
        query.edit_message_text(text='اختار نوع التحويل', reply_markup=converts_keyboard)



    # print(f'likes ---> {likes}, and dislikes ----> {dislikes}')