num_d = {0: 'soon', 1: 'neung', 2: 'song', 3: 'sam', 4: 'si', 5: 'ha', 6: 'hok', 7: 'chet', 8: 'paet', 9: 'kao',
         10: 'sip', 11: 'et', 20: 'yi', 100: 'roi', 1000: 'pun'}


def to_Thai(n):
    ans = []
    if n >= 1000:
        test = n // 1000
        ans.append(num_d[test])
        ans.append(num_d[1000])
        n %= 1000
    if n >= 100:
        test = n // 100
        ans.append(num_d[test])
        ans.append(num_d[100])
        n %= 100
    if n >= 10:
        test = n // 10
        if test == 2:
            ans.append(num_d[20])
            ans.append(num_d[10])
        elif test == 1:
            ans.append(num_d[10])
        else:
            ans.append(num_d[test])
            ans.append(num_d[10])
        n %= 10
    if n >= 1:
        if n == 1 and ('sip' in ans or 'roi' in ans or 'pun' in ans):
            ans.append(num_d[11])
        else:
            ans.append(num_d[n])
    if n == 0 and len(ans) == 0:
        ans.append(num_d[0])
    return ' '.join(ans)


exec(input().strip())
