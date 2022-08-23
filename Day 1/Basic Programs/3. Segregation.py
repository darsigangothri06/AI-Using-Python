inp = list('0011010101')
start = 0 
end = len(inp) - 1
while start < end:
    if inp[start] == '1' and inp[end] == '0':
        inp[start], inp[end] = inp[end], inp[start]
    elif inp[start] == '0':
        start += 1
    elif inp[end] == '1':
        end -= 1
print(''.join(inp))