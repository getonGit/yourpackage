def try_me():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime.datetime(year,month,day)
    date1 = now
    delta = date2 - date1
    days = delta.total_seconds() / 60 /60 /24
    return f'you have {days} left until your birthday'
