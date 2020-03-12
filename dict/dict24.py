to_text = {'2': 'a', '22': 'b', '222': 'c', '3': 'd', '33': 'e', '333': 'f', '4': 'g', '44': 'h', '444': 'i',
           '5': 'j', '55': 'k', '555': 'l', '6': 'm', '66': 'n', '666': 'o', '7': 'p', '77': 'q', '777': 'r',
           '7777': 's', '8': 't', '88': 'u', '888': 'v', '9': 'w', '99': 'x', '999': 'y', '9999': 'z', '0': ' '}


def reverse(d):
    new = {}
    for key, value in d.items():
        new[value] = key
    return new


to_keys = reverse(to_text)


def text2keys(text):
    x = text.lower()
    ans = []
    for e in x:
        if e in to_keys:
            ans.append(to_keys[e])
    return ' '.join(ans)


def keys2text(keys):
    x = keys.split()
    ans = ''
    for e in x:
        ans += to_text[e]
    return ans


exec(input().strip())