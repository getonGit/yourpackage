



def try_me():
    import datetime
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))
    today = datetime.date.today()
    my_birthday = datetime.date(today.year, month, day)

    if my_birthday == today:
        print("Happy Birthday!")
    elif my_birthday < today:
            my_birthday = my_birthday.replace(year=today.year + 1)
            days = my_birthday - today
            print(days)

    else:
        days = my_birthday - today
        print(days)


    return f'you have {days} left until your birthday'

if __name__ == "__main__":

    days = try_me()
    print(days)
