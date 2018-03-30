
def mortality(evitable, inevitable):
    num = (1*evitable) + (0.1*inevitable)
    return num

e = int(input('Type evitable '))
i = int(input('Type inevitable '))

print(mortality(e,i))


