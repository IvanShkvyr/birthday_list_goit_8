from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    """
    The main function. Accepts a list of dictionaries with names and dates of birth.
    Prints to the console a list of birthday people a week ahead of the current date.
    """

    current_day = datetime.now()

    normlize_users = _normalize_date(users, current_day)

    congratulations_list = _choice_date_in_list(normlize_users, current_day)

    _clean_congratulations_list(congratulations_list)

    order_congratulations_list = _order_congratulations_list(congratulations_list, current_day)


    print(order_congratulations_list)
    
    
def _choice_date_in_list(normlize_users, current_day):
    """
    Returns a list of greetings
    """

    congratulations_list = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[]}

    if current_day.strftime("%w") == "1":  # Checking whether the current day is monday
        start_congratulation_period = current_day - timedelta(days=2)
        finish_congratulation_period = start_congratulation_period + timedelta(days=6)
    else:
        start_congratulation_period = current_day
        finish_congratulation_period = start_congratulation_period + timedelta(days=6)

    for user in normlize_users:  # Selects users according to the specified range
        if start_congratulation_period <= user["birthday"] <= finish_congratulation_period:
            if user["birthday"].strftime('%w') == "0" or user["birthday"].strftime('%w') == "6":
                congratulations_list["Monday"].append(user['name'])
            else:
                congratulations_list[user["birthday"].strftime('%A')].append(user['name'])


    return congratulations_list


def _clean_congratulations_list(congratulations_list):
    """
    Removes all days without birthdays from the dictionary
    """
    new_congratulations_list = congratulations_list.copy()

    for day in new_congratulations_list:
        if not new_congratulations_list[day]:
            congratulations_list.pop(day)


def _normalize_date (users, current_day):
    """
    Function returns birthdays in this year
    if the current day is greater than December 25, then the days at the beginning of January will be in the next year
    """
    normlize_users = []

    for user in users:

        if datetime(year=current_day.year, month=user['birthday'].month, day=user['birthday'].day) > datetime(year=current_day.year,
         month=12, day=25):
            normlize_users.append({"name": user['name'], "birthday": user['birthday'].replace(year=current_day.year + 1)})
        else:
            normlize_users.append({"name": user['name'], "birthday": user['birthday'].replace(year=current_day.year)})

    return normlize_users


def _order_congratulations_list(congratulations_list, current_day):
    """
    Formats a list of greetings for printing
    """
    order_congratulations_list = ""

    for i in range(7):
        days_2 = current_day + timedelta(days=i)

        if days_2.strftime('%w') == "0" or days_2.strftime('%w') == "6" or days_2.strftime('%A') not in congratulations_list.keys():
            continue
        else:
            order_congratulations_list += f"{days_2.strftime('%A')}: {', '.join(congratulations_list[days_2.strftime('%A')])}\n"

    return order_congratulations_list.strip()


if __name__ == "__main__":

    users = [{"name":"Ivan1",
              "birthday":datetime(year=1988, month=7, day=24)
             },
             {"name":"Ivan2",
              "birthday":datetime(year=1989, month=7, day=25)
             },
             {"name":"Ivan3",
              "birthday":datetime(year=1990, month=7, day=26)
             },
             {"name":"Ivan4",
              "birthday":datetime(year=1991, month=7, day=27)
             },
             {"name":"Ivan5",
              "birthday":datetime(year=1992, month=7, day=28)
             },
             {"name":"Ivan6",
              "birthday":datetime(year=1972, month=7, day=29)
             },
             {"name":"Ivan7",
              "birthday":datetime(year=1975, month=7, day=30)
             },
             {"name":"Ivan8",
              "birthday":datetime(year=1976, month=8, day=1)
             },
             {"name":"Ivan9",
              "birthday":datetime(year=1977, month=8, day=2)
             },
             {"name":"Ivan10",
              "birthday":datetime(year=1978, month=8, day=3)
             },
             {"name":"Ivan11",
              "birthday":datetime(year=1980, month=8, day=4)
             },
             {"name":"Ivan12",
              "birthday":datetime(year=1980, month=8, day=8)
             },
             {"name":"Ivan13",
              "birthday":datetime(year=1980, month=8, day=9)
             },
             {"name":"Ivan114",
              "birthday":datetime(year=1980, month=8, day=10)
             },
             {"name":"Ivan115",
              "birthday":datetime(year=1980, month=8, day=11)
             },
             {"name":"Ivan116",
              "birthday":datetime(year=1980, month=8, day=12)
             }
            ]

    get_birthdays_per_week(users)