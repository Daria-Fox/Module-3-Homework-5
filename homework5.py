def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient and sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient.endswith(not '.com') and recipient.endswith(not '.ru') and recipient.endswith(not '.net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender.endswith(not ".com") and sender.endswith(not ".ru") and sender.endswith(not '.net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
send_email("Гав!", "sobaka@sobaka.com")
send_email("Мяу!", "koshka.ru", "sobaka@sobaka.com")
send_email("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.net", "university.help@gmail.com")
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')
