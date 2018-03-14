

# noinspection PyUnusedLocal
# skus = unicode string
def calculate_Bs(Es):
    free_bs = Es // 2
    return free_bs

def checkout(skus):
    if not isinstance(skus, unicode):
        return -1

    skus_copy = skus
    if skus == ' ':
        # if it's a string with a space
        return -1
    items = ['A', 'B', 'C', 'D', 'E']
    for item in items:
        skus_copy = skus_copy.replace(item, '')
    if skus_copy != '':
        print skus_copy
        return -1


    print 'skus', skus
    As = skus.count('A')

    Bs = skus.count('B')
    Es = skus.count('E') * 40
    Cs = skus.count('C') * 20
    Ds = skus.count('D') * 15
    as_sum = 0
    if As > 0:
        as_sum += (As // 5) * 200
        as_sum += (As // 3) * 130
        as_sum += (As % 3) * 50
    if
    bs_sum = 0
    if Bs > 0:
        bs_sum += (Bs // 2) * 45
        bs_sum += (Bs % 2) * 30
    print 'As', as_sum
    print 'Bs', bs_sum
    print 'Cs', Cs
    print 'Ds', Ds
    return Cs + Ds + bs_sum + as_sum

