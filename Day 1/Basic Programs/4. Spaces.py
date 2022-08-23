inp = "abcd"
for i in range(1, len(inp)):
    print(inp[:i] + ' ' + inp[i:])
print(' '.join([i for i in inp]))