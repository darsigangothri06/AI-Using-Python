first = "dog"
second = "gos"
def findAng(s, p):
    if len(s) != len(p):
        return False
    for i in range(len(p)):
        if p[i] not in s:
            return False
    return True
print(findAng(first, second))