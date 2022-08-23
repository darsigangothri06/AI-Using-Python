# inp = red-black-pink-yellow
# output = black-pink-red-yellow

inp = 'red-black-pink-yellow'
colors = inp.split('-')
colors.sort()
print('-'.join(colors))