m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def read_date():
    day, month, year = [e for e in input().split()]
    month = m.index(month) + 1
    return [int(day), int(month), int(year)]


def zodiac(d1, m1):
    if d1 >= 22 and m1 == 3 or d1 <= 21 and m1 == 4:
        return "Aries"
    elif d1 >= 22 and m1 == 4 or d1 <= 21 and m1 == 5:
        return "Taurus"
    elif d1 >= 22 and m1 == 5 or d1 <= 21 and m1 == 6:
        return "Gemini"
    elif d1 >= 22 and m1 == 6 or d1 <= 21 and m1 == 7:
        return "Cancer"
    elif d1 >= 22 and m1 == 7 or d1 <= 21 and m1 == 8:
        return "Leo"
    elif d1 >= 22 and m1 == 8 or d1 <= 21 and m1 == 9:
        return "Virgo"
    elif d1 >= 22 and m1 == 9 or d1 <= 21 and m1 == 10:
        return "Libra"
    elif d1 >= 22 and m1 == 10 or d1 <= 21 and m1 == 11:
        return "Scorpio"
    elif d1 >= 22 and m1 == 11 or d1 <= 21 and m1 == 12:
        return "Sagittarius"
    elif d1 >= 22 and m1 == 12 or d1 <= 20 and m1 == 1:
        return "Capricorn"
    elif d1 >= 21 and m1 == 1 or d1 <= 20 and m1 == 2:
        return "Aquarius"
    elif d1 >= 21 and m1 == 2 or d1 <= 21 and m1 == 3:
        return "Pisces"


def days_in_feb(y):
    if y % 400 == 0:
        return 29
    elif y % 4 == 0 and y % 100 != 0:
        return 29
    else:
        return 28


def days_in_month(m, y):
    f = days_in_feb(y)
    mday = [31, f, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return mday[m-1]


def days_in_between(d1, m1, y1, d2, m2, y2):
    days = 0
    if m1 < 12: days += 31
    if m1 < 11: days += 30
    if m1 < 10: days += 31
    if m1 < 9: days += 30
    if m1 < 8: days += 31
    if m1 < 7: days += 31
    if m1 < 6: days += 30
    if m1 < 5: days += 31
    if m1 < 4: days += 30
    if m1 < 3: days += 31
    if m1 < 2: days += days_in_feb(y1)
    if m2 > 1: days += 31
    if m2 > 2: days += days_in_feb(y2)
    if m2 > 3: days += 31
    if m2 > 4: days += 30
    if m2 > 5: days += 31
    if m2 > 6: days += 30
    if m2 > 7: days += 31
    if m2 > 8: days += 31
    if m2 > 9: days += 30
    if m2 > 10: days += 31
    if m2 > 11: days += 30
    days += (days_in_month(m1, y1) - d1 + 1) + int((y2 - y1 - 1) * 365.25) + (d2 - 1)
    return days


def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))


exec(input().strip())