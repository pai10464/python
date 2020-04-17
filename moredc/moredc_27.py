def knows(R, x, y):
    if y in R[x]:
        return True
    return False


def is_celeb(R,x): # return True if a is celeb, otherwise return False
    # return False if x knows someone who is not him/herself
    if len(R[x]) != 0 or (len(R[x]) == 1 and R[x] != x):
        return False
    # return False if there exists someone in R who don't know x
    for key, value in R.items():
        if x not in value and key != x:
            return False
    # otherwise return True
    return True


def find_celeb(R):
    # for each person x in the party
    for x in R:
        # if x is celeb --> return x
        if is_celeb(R, x):
            return x
    # if no celeb in the party --> return None
    return None


def read_relations():
    # build a dictionary R from inputs
    # whose structure is shown in the example
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1:
            break
        if d[0] not in R:
            R[d[0]] = set(d[1])
        elif d[0] in R:
            R[d[0]].add(d[1])
    return R


def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)


exec(input().strip()) # do not remove this line