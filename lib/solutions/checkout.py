
PRICE_OFFERS = {
    'A':{'p': 50, 'o': {3: 130, 5: 200}, 't': 2},
    'B':{'p': 30, 'o': {2: 45}, 't': 1},
    'C':{'p': 20, },
    'D':{'p': 15, },
    'E':{'p': 40, 'o': {'B': 2}, 't': 4},
    'F':{'p': 10, 'o': {3: 2}, 't': 3},
    'G':{'p': 20, },
    'H':{'p': 10, 'o': {5: 45, 10: 80}, 't': 2},
    'I':{'p': 35, },
    'J':{'p': 60, },
    'K':{'p': 80, 'o': {2: 150}, 't': 1},
    'L':{'p': 90, },
    'M':{'p': 15, },
    'N':{'p': 40, 'o': {'M': 3}, 't': 4},
    'O':{'p': 10, },
    'P':{'p': 50, 'o': {5: 200}, 't': 1},
    'Q':{'p': 30, 'o': {3: 80}, 't': 1},
    'R':{'p': 50, 'o': {'dependency':'Q', 'group':3}, 't':4},
    'S':{'p': 30, },
    'T':{'p': 20, },
    'U':{'p': 40, 'o': {4: 3}, 't': 3},
    'V':{'p': 50, 'o': {2: 90, 3: 130}, 't': 2},
    'W':{'p': 20, },
    'X':{'p': 90, },
    'Y':{'p': 10, },
    'Z':{'p': 50, },
}

OFFER_TYPE = {
    1: 'itemx_stacked',
    2: 'itemx_stacked',
    3: 'one_free',
    4: 'nX_Y_free'
}


def itemx_stacked(item, quantity):
    offer = PRICE_OFFERS[item]['o']
    # get best offer, sort descending the keys
    best_offer = offer.keys.sort(reverse=True)
    price = 0
    for group in best_offer:
        os = quantity // group
        price += os * offer[group]
        quantity -= os * group
    # individual items
    price += quantity * PRICE_OFFERS[item]['p']
    return price


def one_free(item, quantity):
    offer = PRICE_OFFERS[item]['o']
    individual_price = PRICE_OFFERS[item]['p']
    total_price = 0
    best_offer = offer.keys.sort(reverse=True)
    for group in best_offer:
        group_price = offer[group] * individual_price
        os = quantity // group
        total_price += os * group_price
        quantity -= os * group
    # individual items
    total_price += quantity * individual_price
    return total_price

def nX_Y_free(item, quantity):
    offer = PRICE_OFFERS[item]

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

