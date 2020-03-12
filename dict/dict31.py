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
        if amt // keys > value:
            return {}
        if amt // keys != 0:
            d_amt[keys] = amt // keys
            amt %= keys
            pocket[keys] -= d_amt[keys]
    return d_amt


p={100:3, 10:5, 5:10, 1:7}
print(pay(p, 407))