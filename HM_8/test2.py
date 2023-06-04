from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.today()
    end_of_week = today + timedelta(days=7)

    birthdays = {}

    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y-%m-%d")

        if today <= birthday <= end_of_week:
            weekday = birthday.strftime("%A")

            if weekday == "Saturday":
                next_day = birthday + timedelta(days=2)
            elif weekday == "Sunday":
                next_day = birthday + timedelta(days=1)
            else:
                next_day = birthday

            next_day_weekday = next_day.strftime("%A")
            if next_day_weekday not in birthdays:
                birthdays[next_day_weekday] = []
            birthdays[next_day_weekday].append(name)

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Іван", "birthday": "2023-06-04"},
    {"name": "Марія", "birthday": "2023-06-08"},
    {"name": "Петро", "birthday": "2023-06-07"},
    {"name": "Олена", "birthday": "2023-06-14"},
    {"name": "Михайло", "birthday": "2023-06-11"}
]

get_birthdays_per_week(users)
