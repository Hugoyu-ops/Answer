
def isSubnet(set1, set2):
    result = set1.issubset(set2)
    return result

a = {'a', 'c', 'd'}
b = {'a', 'v', 'n', 'c', 'd', 'g'}

print(isSubnet(a,b))