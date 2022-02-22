from datetime import datetime

age = 0


def reg_age():
    global age
    while age == 0:
        try:
            age = int(age)
        except Exception:
            print('Нужны цифры')


def dd():
    s = datetime.now()
    print(s.strftime('%d.%m.%Y %H:::%M:%S'))


dd()
