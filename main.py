import datetime
import random
from telegram.ext import *
from keyboards import *
import keys, skills, support


def start_command(update, context):
    update.message.reply_text(
        ' هلو اسمي انيا, انيا بوتة الشعبة A قسم نظم المعلومات' + '\n' +
        'شعبة A حاليا مرحلة اولى بس انيا راح تبقى بوتتهم حتى من يصعدون لباقي المراحل > _ <')


def help_command(update, context):
    update.message.reply_text(text='انيا بعدهي قيد التطوير , _ , بس يلا نجرب..', reply_markup=help_keyboard)


def send_pic_command(update, context):
    bot.send_photo(update.message.chat.id, photo=open('schedule.png', 'rb'))
    update.message.reply_text('ياا انيا صارت تعرف ترسل جدول انيا سوبر فرحانه > _ <')

def dance(update, context):
    bot.send_animation(update.message.chat.id, 'https://media.giphy.com/media/qVfJX3Si7MLkOksNMB/giphy.gif')
    update.message.reply_text('انيا تعرف تركص Uwu')


def handle_response(text: str, user):  # important
    # تحويلات الارقام
    print(user)
    for list in converting_dict:
        if user in converting_dict[list]:
            if list == 'dec2bi':
                converting_dict[list].remove(user)
                return support.decimal_to_binary(text)
            if list == 'dec2oct':
                converting_dict[list].remove(user)
                return support.decimal_to_octal(text)
            if list == 'dec2hex':
                converting_dict[list].remove(user)
                return support.decimal_to_hexadecimal(text)

            if list == 'bi2dec':
                converting_dict[list].remove(user)
                return support.to_decimal(text, 2)
            if list == 'oct2dec':
                converting_dict[list].remove(user)
                return support.to_decimal(text, 8)
            if list == 'hex2dec':
                converting_dict[list].remove(user)
                return support.to_decimal(text, 16)



    # الرسائل
    if 'آنيا' in text or keys.bot_name in text:
        if 'هلو' in text:
            return 'هلو uwu'
        if 'شلونج' in text.replace('چ', 'ج') or 'خبارج' in text.replace('چ', 'ج'):
            return 'آنيا زينة'
        if 'شنو' in text:
            if 'شغلج' in text or 'فائدتج' in text.replace('ي', 'ئ') or 'وظيفتج' in text.replace('ض', 'ظ'):
                return 'انيا وظيفتهة تساعد شعبة A بكم شغلة وبلمقابل تتعلم منهم كم شغلة'
            if 'معنى' in text or 'يعني' in text:
                if 'uwu' in text:
                    return 'Uwu uwu uwU'

        if 'جدول' in text:  # star
            return 'زينب رتبت الجدول الجديد  > _ < 🍊 '
        if 'بيت' in text and 'وين' in text:
            return random.choice([' حاليا آنيا عايشة بلابتوب 🥲 آنيا تريد سيرفر.. ', '🥲 آنيا ما تكول انيا تخاف تنخطف',
                                  '😱😱😱 انيا تلوذ بلفرار 🏃🏼 ', ' حاليا آنيا عايشة بلابتوب 🥲 آنيا تريد سيرفر.. ',
                                  'حاليا آنيا عايشة بلابتوب 🥲 آنيا تريد سيرفر.. '])
        if 'لا' in text and 'ضوجين' in text:
            return random.choice(['محد يهتم بمشاعر آنيا', 'آنيا تريد تموت..', '🥲', 'شكرا آنيا زينة', 'آنيا اسوء بوت..'])
        if 'لا' in text and 'زعلين' in text:
            return random.choice(
                ['محد يهتم بمشاعر آنيا', 'آنيا مو قصدهة تزعل بس انيا زعلانة', '🥲', 'شكرا آنيا زينة', 'آنيا اسوء بوت..'])
        if 'تردين' in text:
            return random.choice(['يي اريد', 'اوكي آنيا تقبل تاخذ', 'يي نطيني', 'ما', 'شكرا آنيا متريد'])
        if 'تريدين' in text:
            return random.choice(['يي اريد', 'اوكي آنيا تقبل تاخذ', 'يي نطيني', 'ما', 'شكرا آنيا متريد'])
        if 'مال' in text and 'من' in text and 'انتي' in text:
            return 'آنيا مالت حوراء > _ < '
        if 'سواج' in text and 'من' in text:
            return '!diotic Jenn#6790'
        if 'سويج' in text and 'من' in text:
            return '!diotic Jenn#6790'
        if 'صممج' in text and 'من' in text:
            return '!diotic Jenn#6790'
        if 'طلعي' in text:
            return random.choice(['لا فدوة لا حبابيين لا طردون آنيا', 'ب-بس آنيا شنو سوت؟🥲🥲'])
        if 'تحبين' in text:
            return random.choice(['يب', 'كلش هواي', 'شوي', 'لا', 'ما اعرف'])
        if 'ولي' in text:
            return 'اسفة...'
        if 'سكتي' in text:
            return 'آنيا سكتت'
        if 'مسوي' in text and 'دايت':
            return random.choice(['هية آنيا بوت وين شايفة الاكل اصلا 🥲🥲 '])
        if 'خطف' in text and 'خل':
            return random.choice(['تمام آنيا تحب الخطف'])
        if 'قتل' in text:
            return random.choice(['آنيا ماتحب القتل'])
        if 'وجع' in text:
            return random.choice(['🥲🥲'])
        if 'نجب' in text:
            return random.choice(['🥲🥲 آنيا نجبت'])
        if 'تعالي' in text or 'تعاي' in text:
            return random.choice(['آنيا اجت'])
        if 'طردو' in text or 'طردي' in text:
            return random.choice(['الطرد شي مو حلو'])
        if 'طلعو' in text or 'طلعي' in text:
            return random.choice(['Anya left the chat '])
        if 'ليش' in text and 'ما' in text and 'ترد' in text:
            return random.choice(['آنيا ما عدهة رد', 'آنيا اسفة', ' آنيا بعدهي ما تعرف شنو تكول..'])
        if 'ردي' in text:
            return random.choice(['آنيا ما عدهة رد', 'آنيا اسفة', ' آنيا بعدهي ما تعرف شنو تكول..'])
        if 'منو' in text or ' منو انتي' in text or 'انتي منو' in text or 'انت منو' in text or 'منو انت' in text:
            return ' هلو اسمي آنيا, آنيا بوتة الشعبة A قسم نظم المعلومات' + '\n' + 'شعبة A حاليا مرحلة اولى بس انيا راح تبقى بوتتهم حتى من يصعدون لباقي المراحل > _ <'
        if 'صباح' in text:
            return random.choice(['آنيا ما تحب الصبح', 'صباح الخير', 'صباحكم', 'صباح النور'])
        if 'مساء' in text:
            return random.choice(['مسائكم', 'مساء الخير', 'مساء النور'])
        if '🍊' in text:
            return random.choice(['هاي برتقالة زينب 🙂', 'يااا برتقال زينب', 'شوفو برتقالة زينب 😍😍'])
        # مال من
        if 'المن' in text or 'مال من' in text or 'مال' in text or 'تبع من' in text or 'تخص من' in text or 'ملكية' in text or 'لمن' in text or 'مالمن' in text:
            if 'برتقالة' in text.replace('ه','ة'):
                return random.choice(['البرتقالة ملكية خاصة لزينب 🍊', 'الكل يعرف البرقتالة مال زينب > _ <', 'مالت زينب'])

        # if 'ملزمة' in text.replace('ه', 'ة') and 'برمجة' in text.replace('ه', 'ة'):
        #     return '❤❤'
        if 'ملزمة' in text.replace('ه', 'ة') or 'دفتر' in text or 'كتاب' in text or 'برنامج' in text:
            return ''
        if 'ابجي' in text or 'ابكي' in text or 'خايسة' in text:
            return ''
        # تعاريف
        if 'تعريف' in text or 'عرفي' in text or 'شنو' in text:
            if 'حاسوب' in text or 'كمبيوتر' in text or 'computer' in text:
                return skills.computer
            if 'اجهزة الكمبيوتر' in text.replace('ه', 'ة') or 'هاردوير' in text or 'hardware' in text:
                return skills.hardware
            if 'برامج' in text or 'سوفتوير' in text or 'software' in text:
                return skills.software
            if 'معالج' in text or 'سي بي يو' in text or 'cpu' in text:
                return skills.CPU
            if 'وحدة منطقية' in text.replace('ه', 'ة') or 'ارذمتك لوجكل يونت' in text or 'arithmetic logical unit' in text:
                return skills.arithmetic_logical_unit
            if 'وحدة التحكم' in text.replace('ه', 'ة') or 'كنترول يونت' in text or 'control unit' in text:
                return skills.control_unit
            if 'اجهزة التخزين' in text.replace('ه', 'ة') or 'ستورج' in text or 'storage' in text:
                return skills.storage_devices
            if 'فرص صلب' in text or 'هارد دسك' in text or 'hard disk' in text:
                return skills.hard_disk
            if 'فرص مرن' in text or 'فلوبي دسك' in text or 'floppy disk' in text:
                return skills.floppy_disk
        if 'عشري الى ثنائي' in text or 'دسمل تو باينري' in text or 'دسمل الى باينري' in text:
            return support.decimal_to_binary(text)
        if 'عشري الى ثماني' in text or 'دسمل تو اوكتال' in text or 'دسمل الى اوكتال' in text:
            return support.decimal_to_octal(text)
        if 'عشري الى سداسي عشر' in text or 'دسمل تو هكس' in text.replace('ز', 'س') or 'دسمل الى هكس' in text.replace('ز','س'):
            return support.decimal_to_hexadecimal(text)

        if 'سداسي عشر الى عشري' in text or 'هكس تو دسمل' in text.replace('ز', 'س') or 'هكس الى دسمل' in text.replace('ز','س'):
            return support.to_decimal(text, 16)
        if 'ثمانس الى عشري' in text or 'اوكتال تو دسمل' in text or 'اوكتال الى دسمل' in text:
            return support.to_decimal(text, 8)
        if 'ثنائي الى عشري' in text or 'باينري تو دسمل' in text or 'باينري الى دسمل' in text:
            return support.to_decimal(text, 2)

        if 'شكر' in text:
            return random.choice(['عفوا', '🌹', 'هذا واجب آنيا 😗'])


        if text.strip() == 'آنيا':
            return 'نعم'
        if 'آنيا' in text:
            # 'آنيا ما اتعرف جواب لهل كلام', 'آنيا ما تعرف هواي اشيائات علموها لآنيا بليز', 'آنيا ما تدري بس آنيا تريد تتعلم',
            return random.choice(['🤷'])

    if '🍊' in text and text != '🍊':
        return random.choice(['هاي برتقالة زينب 🙂', 'يااا برتقال زينب', 'شوفو برتقالة زينب 😍😍'])


def handle_message(update, context):
    message_type = update.message.chat.type
    date = update['message']['date']
    username = update.message.from_user.username
    # print(date)
    text = str(update.message.text).lower()
    # print(update.message.from_user)
    print(f'User ({username}) says: "{text}" in: "{message_type} " at: "{date}"')
    new_text = text
    response = handle_response(text, username)
    if message_type == 'supergroup' or message_type == 'private':

        if 'جدول' in new_text and 'آنيا' in new_text:
            bot.send_photo(update.message.chat.id, photo=open('schedule.png', 'rb'))

        if 'آنيا' in new_text and 'كتاب' in new_text:
            if 'c' in new_text or 'سي'in new_text:
                bot.send_document(update.message.chat.id, document=open('books/سي.pdf', 'rb'))

        # ملازم
        if 'ملزمة' in new_text.replace('ه', 'ة') and 'آنيا' in new_text:

            if 'عملي' in new_text:     # عملي

                # مهارات
                if 'مهارات' in new_text.replace('ه', 'ة') or 'سكلز' in text or 'programming' in text:
                    if 'عربي' in new_text or 'arabic' in new_text:
                        bot.send_message(update.message.chat.id, 'ماكو...')
                    else:
                        bot.send_document(update.message.chat.id, document=open('books/مهارات-علمي.pdf', 'rb'))
                else:
                    bot.send_message(update.message.chat.id, 'ماكو...')

            else:                  # نظري

                # مهارات
                if 'مهارات' in new_text.replace('ه', 'ة') or 'سكلز' in text or 'skills' in text:
                    if 'عربي' in new_text or 'arabic' in new_text:
                        bot.send_message(update.message.chat.id, 'ماكو...')
                    else:
                        bot.send_document(update.message.chat.id, document=open('books/مهارات-نظري.pdf', 'rb'))

                # برمجة
                elif 'برمجة' in new_text.replace('ه', 'ة') or 'بروكرامنك' in text.replace('گ', 'ك') or 'programming' in text:
                    if 'عربي' in new_text or 'arabic' in new_text:
                        bot.send_message(update.message.chat.id, 'ماكو...')
                    else:
                        bot.send_document(update.message.chat.id, document=open('books/برمجة.pdf', 'rb'))

                # لوجك
                elif 'تصميم منطقي' in new_text or 'لوجك' in text.replace('گ', 'ك') or 'logic' in text:
                    if 'عربي' in new_text or 'arabic' in new_text:
                        bot.send_message(update.message.chat.id, 'ماكو...')
                    else:
                        bot.send_document(update.message.chat.id, document=open('books/اللوجك-ديزاين.pdf', 'rb'))

                # حقوق
                elif 'حقوق' in new_text or 'ديمقراطية' in text or 'democracy' in text or 'human rights' in text:
                    if 'عربي' in new_text or 'arabic' in new_text:
                        bot.send_message(update.message.chat.id, 'هية بلعربي ماكو نكليزي الهة 😁😁')
                        bot.send_document(update.message.chat.id, document=open('books/مادة-حقوق-الانسان.pdf', 'rb'))
                    else:
                        bot.send_document(update.message.chat.id, document=open('books/مادة-حقوق-الانسان.pdf', 'rb'))
                else:
                    bot.send_message(update.message.chat.id, 'ماكو...')

        if 'دفتر' in new_text and 'آنيا' in new_text:
            if 'برمجة' in new_text.replace('ه', 'ة') or 'بروكرامنك' in text.replace('گ', 'ك') or 'programming' in text:
                bot.send_document(update.message.chat.id, document="https://cdn.discordapp.com/attachments/921287193828425778/1053554569919078470/-.pdf")
                bot.send_message(update.message.chat.id, ' بيد بنت الهدى احمد حد يوم 15 ديسمبر ')
            elif 'منطقي' in new_text or 'لوجك' in text.replace('گ', 'ك') or 'logic' in text:
                bot.send_document(update.message.chat.id, document=open('note-books/دفتر-لوجك.pdf', 'rb'))
                bot.send_message(update.message.chat.id, ' بيد بنت الهدى احمد حد يوم 12 ديسمبر ')
            elif 'نكليزي' in text.replace('گ', 'ك') or 'نكلش' in text.replace('گ', 'ك') or 'english' in text:
                bot.send_document(update.message.chat.id, document=open('note-books/دفتر-انكلش.pdf', 'rb'))
                bot.send_message(update.message.chat.id, ' بيد بنت الهدى احمد حد يوم 15 ديسمبر ')
            elif 'رياضيات' in text.replace('ظ', 'ض') or 'ماث' in text or 'math' in text:
                bot.send_document(update.message.chat.id, document="https://cdn.discordapp.com/attachments/921287193828425778/1053554191307636757/-.pdf")
                bot.send_message(update.message.chat.id, ' بيد بنت الهدى احمد حد يوم 15 ديسمبر ')
            else:
                bot.send_message(update.message.chat.id, ' ماكو..')


        if 'برنامج' in new_text and 'آنيا' in new_text:    # برامج
            if 'لوجك' in new_text or 'ورك بنش' in new_text.replace('ج', 'ش') or 'workbench' in new_text:
                bot.send_message(update.message.chat.id, 'https://mega.nz/file/HNElWbTC#wNt3aJTPp_jU4_2IpJzMjLP3APWS07m-oH7PM596jSo')
                bot.send_message(update.message.chat.id, ' رفع بواسطة تبارك احمد يوم 16 ديسمبر ')

            else:
                bot.send_message(update.message.chat.id, ' آنيا ماعدهة هذا البرنامج..')


        if 'آنيا' in new_text:
            if 'ابجي' in new_text or 'ابكي' in new_text or 'خايسة' in new_text:
                bot.send_animation(update.message.chat.id, 'https://media.giphy.com/media/DNe4LKL6iwZ2goCSx6/giphy.gif')
        if '🍊' == text:
            bot.send_message(update.message.chat.id, text='تحبون البرتقال ؟', reply_markup=orange_keyboard)





    else:

        response = handle_response(text, username)

    update.message.reply_text(response)


def error(update, context):
    print(f'Update: {update}, caused error: {context.error}')


if __name__ == '__main__':
    bot = ExtBot(keys.token)
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # query
    dp.add_handler(CallbackQueryHandler(query_handler))

    # commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('schedule', send_pic_command))
    dp.add_handler(CommandHandler('dance', dance))



    # messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))


    # error
    dp.add_error_handler(error)

    # run bot
    updater.start_polling(1.0)
    updater.idle()
