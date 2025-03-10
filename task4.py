from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = [] 
    today = datetime.today().date()  
     
    for user in users:
       
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birth_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() in {5, 6}:  
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
