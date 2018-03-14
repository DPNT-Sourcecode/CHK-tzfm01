

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, unicode):
        return -1

    skus_copy = skus
    if skus == ' ':
        # if it's a string with a space
        return -1
    items = ['A', 'B', 'C', 'D']
    for item in items:
        skus_copy = skus_copy.replace(item, '')
    if skus_copy != '':
        print skus_copy
        return -1


    print 'skus', skus
    As = skus.count('A')

    Bs = skus.count('B')

    Cs = skus.count('C') * 20
    Ds = skus.count('D') * 15
    as_sum = 0
    if As > 0:
        as_sum += (As // 3) * 130
        as_sum += (As % 3) * 50
    bs_sum = 0
    if Bs > 0:
        bs_sum += (Bs // 2) * 45
        bs_sum += (Bs % 2) * 30
    print 'As', as_sum
    print 'Bs', bs_sum
    print 'Cs', Cs
    print 'Ds', Ds
    return Cs + Ds + bs_sum + as_sum

