from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо дати народження з рядка в об'єкт date
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Розраховуємо різниці днів між поточною датою та днем народження
        delta_days = (birthday_this_year - today).days

        # Перевіряємо, чи день народження випадає на наступний тиждень
        if 0 <= delta_days < 7:
            congratulation_date = birthday_this_year

            # Перенесення дати привітання на понеділок, якщо вона випадає на вихідний
            if congratulation_date.weekday() >= 5:  # 5 - субота, 6 - неділя
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

            # Додаємо інформації про користувача до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

