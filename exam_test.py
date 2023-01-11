import random

q1 = {
    'question': [  # a list with 2 elements
        '____ is an electronic device that has the ability to receive data, modify it, process it and convert it to valuable information,'
        'then store it in internal or external storage media.',  # english
        'هو جهاز الكتروني يمتلك القدرة على استقبال المعلومات وتعديلها ومعالجتها'
        ' وتحويلها الى معلومات قيمة ثم خزنها في وسائل تخزين داخلية او خارجية'
        # arabic
    ],

    'answers': {'correct': ['computer'],
                'false': ['motherboard', 'hard disk', 'mouse', 'BIOS', 'scanner']
                }
}

q2 = {
    'question': [
        '____ is the set of physical parts of a computer system, that make up the computer.\n'
        'Such as the screen, keyboard, data storage media (such as the hard disk), \n'
        'and the system unit',

        'وهو تلك المجموعة من القطع المادية لنظام الحاسوب التي تكوّن جهاز الحاسوب مثل الشاشة والكيبورد'
        ' ووسائل التخزين (مثل القرص الصلب) ووحدة النظام (المذربورد وغراضها تقصد)'

    ],

    'answers': {'correct': ['hardware'],
                'false': ['firmware', 'hard disk', 'BIOS', 'software']
                }
}

q3 = {
    'question': [
        '____ is not a part of the system unit',
        'هو لا يعتبر جزء من وحدة النظام'
    ],

    'answers': {'correct': [random.choice(['keyboard', 'screen', 'hard disk'])],
                'false': ['graphics card', 'sound card', 'memory', 'motherboard']
                }
}

q4 = {
    'question': [
        '____ is all physical things that can be touched',
        'هو قطع مادية يمكن لمسها'
    ],

    'answers': {'correct': ['hardware'],
                'false': ['firmware', 'software', 'BIOS', 'adware']
                }
}

q5 = {
    'question': [
        '____ or (the processor) is a small silicon chip that contains complex electronic circuits.',
        'او (المعالج) هو شريحة سيليكونية صغيرة تحتوي دوائر كهربائية معقدة'
    ],

    'answers': {'correct': ['cpu'],
                'false': ['monitor', 'plotter', 'headphones', 'malware']
                }
}

q6 = {
    'question': [
        'the ____ is where arithmetic and logical operations are processed.',
        'ال ____ هي مكان معالجة العمليات الرياضية والمنطقية'
    ],

    'answers': {'correct': ['arithmetic logical unit'],
                'false': ['control unit', 'bios', 'system unit', 'firewall']
                }
}

q7 = {
    'question': [
        'the ____ is considered the brain of the computer, it can issue commands to all computer departments'
        ' and coordinate among them to perform the required functions between them.',
        'ال ____ هي ما يعتبر عقل الحاسوب , يمكنها اصدار اوامر لجميع اجزاء الحاسوب والتنسيق بينهم لاجراء العمليات المطلوبة بينهم'
    ],

    'answers': {'correct': ['control unit'],
                'false': ['arithmatic logical unit', 'system unit', 'audio converter', 'sound card']
                }
}

q8 = {
    'question': [
        '____ allow the user to store data before or after processing it to get it back later.',
        'تمكن المستخدمين من خزن البيانات قبل او بعد معالجتها للحصول عليها لاحقا'
                 ],

    'answers': {'correct': ['storage devices'],
                'false': ['processing devices', 'output devices', 'input devices', 'graphics cards']
                }
}

q9 = {
    'question':[
        '____ is a magnetic-coated metal disk placed inside an airtight and sealed container.'
        ' Information is stored in it permanently with the ability to delete or re-store it.',

        'هو قرص معدني مغطى بطبقة مغناطيسية موضوع في حاوية مغلقة ومفرغة من الهواء تخزن المعلومات فيه بشكل دائم مع امكانية حذفها او استرجاعها'
    ],

    'answers': {'correct': ['hard disk'],
                'false': ['floppy disk', 'magnetic tape', 'optical disk', 'applications software']
                }
}

q10 = {
    'question': [
        'the ____ consists of cylinders made of plastic material and coated with brown magnetic material '
        'and is considered a mobile store, but its storage capacity is limited.',

        'ال ____ يتكون من اسطوانات مصنوعة من مادة بلاستيكية مغطاة يمادة مغناطيسية بنية اللون يُعتبر مخزن متنقل ولكن سعة تخزينه محدودة'
    ],

    'answers': {'correct': ['floppy disk'],
                'false': ['hard disk', 'magnetic tape', 'optical disk', 'applications software']
                }
}

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
random.shuffle(questions)
