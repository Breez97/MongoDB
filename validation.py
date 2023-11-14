#Функция проверки ввода имени и названий
def limitNameTitle(text):
    if len(text) < 40 and all(char.isalpha() or char.isspace() for char in text):
        return True
    else:
        return False

#Функция проверки чисел
def limitNumber(text):
    if len(text) < 12 and all(char.isnumeric() for char in text):
        return True
    else:
        return False

#Функция проверки даты
def limitDate(text):
    if len(text) < 11 and all(char.isnumeric() or char == '-' for char in text):
        return True
    else:
        return False