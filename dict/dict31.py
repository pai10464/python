def total(pocket):
    tot = 0
    for keys, value in pocket.items():
        tot += keys * value
    return tot


def take(pocket, money_in):
    for keys, value in money_in.items():
        if keys in pocket:
            pocket[keys] += money_in[keys]
        else:
            pocket[keys] = money_in[keys]


def pay(pocket, amt):
    d_amt = {}
    for keys, value in pocket.items():
        while amt >= keys and pocket[keys] != 0:
            if keys not in d_amt:
                amt -= keys
                d_amt[keys] = 1
                pocket[keys] -= 1
            else:
                amt -= keys
                d_amt[keys] += 1
                pocket[keys] -= 1
    if amt != 0:
        for keys, value in d_amt.items():
            pocket[keys] += value
        return {}
    return d_amt


exec(input().strip())