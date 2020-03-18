filename = input().strip()
fn = open(filename, 'r')
code = fn.readline().strip('\n')
pattern = fn.readline().strip('\n')
if code == 'T2M':
    a = pattern.strip('[').split('[')
    m_dict = {}
    for e in a:
        b = e.split(']')
        m_dict[b[0]] = b[1]
    for e in fn:
        ans = []
        e = e.strip('\n')
        for i in e:
            if i not in m_dict:
                print('Invalid : ' + e)
                ans = []
                break
            else:
                ans.append(m_dict[i])
        if len(ans) != 0:
            print(' '.join(ans))
elif code == 'M2T':
    a = pattern.strip('[').split('[')
    m_dict = {}
    for e in a:
        b = e.split(']')
        m_dict[b[1]] = b[0]
    for e in fn:
        ans = []
        e = e.split()
        for i in e:
            if i not in m_dict:
                print('Invalid : ' + ' '.join(e))
                ans = []
                break
            else:
                ans.append(m_dict[i])
        if len(ans) != 0:
            print(''.join(ans))
else:
    print('Invalid code')