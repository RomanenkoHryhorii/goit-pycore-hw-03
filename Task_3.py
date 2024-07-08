import re

def normalize_phone(phone_number):
 
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)
    
    # Якщо номер не починається з '+', додаємо '+38'
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    
    return cleaned_number