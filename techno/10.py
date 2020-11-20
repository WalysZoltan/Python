#how split works"
s = (
    'rogue cleric fighter monk' +
    'ranger warlock wizard' +
    'sorcerer druid'
)
#print(s)
first = sorted(s.split())[0]
print(first.split('r')[0])
