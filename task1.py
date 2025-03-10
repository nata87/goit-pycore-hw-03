from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        difference = today_date - given_date

        return difference.days
    
    except ValueError:
        print("Неправильний формат дати! Використовуйте 'РРРР-ММ-ДД'.")
        return None  

