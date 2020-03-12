def no_lowercase(t):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for e in t:
        if e in a:
            return False
    return True


def no_uppercase(t):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for e in t:
        if e in a:
            return False
    return True


def no_numbers(t):
    a = '123456789'
    for e in t:
        if e in a:
            return False
    return True


def no_symbols(t):
    a = '!@#$%^&*()_+-=[]{};"?/>.<,'
    for e in t:
        if e in a:
            return False
    return True


def character_repetition(t):
    for e in range(len(t) - 3):
        if t[e] == t[e + 1] and t[e] == t[e + 2] and t[e] == t[e + 3]:
            return True
    return False


def number_sequence(t):
    a = '01234567890'
    for e in range(len(t) - 3):
        if a.find(t[e:e + 3]) != -1:
            return True
        if a[-1::-1].find(t[e:e + 3]) != -1:
            return True
    return False


def letter_sequence(t):
    t = t.lower()
    a = 'abcdefghijklmnopqrstuvwxyz'
    for e in range(len(t) - 3):
        if a.find(t[e:e + 4]) != -1:
            return True
        if a[-1::-1].find(t[e:e + 4]) != -1:
            return True
    return False


def keyboard_pattern(t):
    t = t.lower()
    a = '!@#$%^&*()_+'
    b = 'qwertyuiop'
    c = 'asdfghjkl'
    d = 'zxcvbnm'
    for e in range(len(t) - 3):
        if a.find(t[e:e + 3]) != -1:
            return True
        if a[-1::-1].find(t[e:e + 3]) != -1:
            return True
        if b.find(t[e:e + 3]) != -1:
            return True
        if b[-1::-1].find(t[e:e + 3]) != -1:
            return True
        if c.find(t[e:e + 3]) != -1:
            return True
        if c[-1::-1].find(t[e:e + 3]) != -1:
            return True
        if d.find(t[e:e + 3]) != -1:
            return True
        if d[-1::-1].find(t[e:e + 3]) != -1:
            return True
    return False


t = input()
i = 0
if len(t) < 8: print('Less than 8 characters'); i+= 1
if no_lowercase(t): print('No lowercase letters'); i+= 1
if no_uppercase(t): print('No uppercase letters'); i+= 1
if no_numbers(t): print('No numbers'); i+= 1
if no_symbols(t): print('No symbols'); i+= 1
if character_repetition(t): print('Character repetition'); i+= 1
if number_sequence(t): print('Number sequence'); i+= 1
if letter_sequence(t): print('Letter sequence'); i+= 1
if keyboard_pattern(t): print('Keyboard pattern'); i+= 1
if i == 0: print('OK')
