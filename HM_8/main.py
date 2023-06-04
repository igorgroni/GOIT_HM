from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.today()
    # current_week = today.isocalendar()[1]
    sorted_users = sorted(users, key=lambda user: datetime.strptime(
        user['birthday'], "%Y-%m-%d").day)

    for user in sorted_users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y-%m-%d")
        # birthday_week = birthday.isocalendar()[1]
        weekday = birthday.strftime("%A")

        if weekday == "Sunday":
            next_day = birthday + timedelta(days=1)
            next_day_weekday = next_day.strftime("%A")
            print(f"{next_day_weekday}: {name}")
        elif weekday == "Saturday":
            next_day = birthday + timedelta(days=2)
            next_day_weekday = next_day.strftime("%A")
            print(f"{next_day_weekday}: {name}")
        else:
            print(f"{weekday}: {name}")


users = [
    {"name": "Іван", "birthday": "2023-06-04"},
    {"name": "Марія", "birthday": "2023-06-08"},
    {"name": "Петро", "birthday": "2023-06-07"},
    {"name": "Олена", "birthday": "2023-06-07"},
    {"name": "Михайло", "birthday": "2023-06-11"}
]

get_birthdays_per_week(users)
