

# noinspection PyUnusedLocal
# skus = unicode string
def calculate_Bs(Es):
    free_bs = Es // 2
    return free_bs

def calculate_As(As):
    # apply 5x offer
    as_5x = (As // 5) * 200
    print 'as_5x', as_5x
    as_3x = ((As % 5) // 3) * 130
    print 'as_3', as_3x
    as_individual = ((As % 5) % 3) * 50
    print 'as_ind', as_individual
    return sum([as_individual, as_3x, as_5x])

def calculate_Fs(Fs):
    fs_3x = (Fs // 3) * 20
    fs_individual = (Fs % 3) * 10
    return sum([fs_3x, fs_individual])


def checkout(skus):
    # if not isinstance(skus, unicode):
    #     return -1
    skus = str(skus)
    skus_copy = skus
    if skus == ' ':
        # if it's a string with a space
        return -1
    items = ['A', 'B', 'C', 'D', 'E', 'F']
    for item in items:
        skus_copy = skus_copy.replace(item, '')
    if skus_copy != '':
        print 'replaces ', skus_copy
        return -1


    print 'skus', skus
    As = skus.count('A')

    Bs = skus.count('B')
    Es = skus.count('E')
    es_sum = Es * 40
    Cs = skus.count('C') * 20
    Ds = skus.count('D') * 15
    Fs = skus.count('F')
    fs_sum = calculate_Fs(Fs)
    as_sum = 0
    if As > 0:
        as_sum += calculate_As(As)

    Bs = Bs - calculate_Bs(Es)
    bs_sum = 0
    if Bs > 0:
        bs_sum += (Bs // 2) * 45
        bs_sum += (Bs % 2) * 30
    print 'As', as_sum
    print 'Bs', bs_sum
    print 'Cs', Cs
    print 'Ds', Ds
    print 'Es', es_sum
    print 'Fs', fs_sum
    return Cs + Ds + bs_sum + as_sum + es_sum + fs_sum

