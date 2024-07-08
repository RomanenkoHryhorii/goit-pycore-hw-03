import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    
    # Перевіряємо, чи відповідають параметри заданим обмеженням
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    # Генеруємо набір унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Сортуємо числа за зростанням
    numbers.sort()
    
    return numbers


