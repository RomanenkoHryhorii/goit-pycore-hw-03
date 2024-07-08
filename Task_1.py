from datetime import datetime

def get_days_from_today(date):
   
    # Перетворюємо рядок дати у об'єкт datetime
    given_date = datetime.strptime(date, '%Y-%m-%d')
    
    # Отримуємо поточну дату
    current_date = datetime.today()
    
    # Розраховуємо різницю між датами
    difference = current_date - given_date
    
    # Повертаємо кількість днів
    return difference.days

