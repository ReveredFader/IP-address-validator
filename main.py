import json

def check_ip_addresses(stoplist_file, text_file):
    with open(stoplist_file) as f:
        file_content = f.read()
        templates = json.loads(file_content)

    items = []
    for section, commands in templates.items():
        items.extend(commands) # Записываем в один список все адреса из стоплиста
    to_valid = [] # Адреса которые отправят на валидацию

    with open(text_file, 'r') as r:
        for line in r:
            text_file_content = line.split()
            to_valid.extend(list(set(text_file_content) - set(items))) # Убираем адреса, если они есть в стоп листе

        to_valid = set(to_valid)
        valid = [] # Подходящие адреса

        for i in to_valid: # Отправляем все адреса на проверку
            if validIP(i):
                valid.append(i)
    return valid

def validIP(address):
    parts = address.split(".") # Разбиваем ip на 4 части
    if len(parts) != 4: # Проверяем подходят ли части ip под условия
        return False
    for item in parts:
        if not item.isdigit():
            return False
        if not 0 <= int(item) <= 255:
            return False
        if len(item) != 1 and item[0] == "0":
            return False
    return True