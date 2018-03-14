

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    if not skus:
        # if it's null string
        return -1
    if skus == ' ':
        # if it's a string with a space
        return -1
    skus = skus.upper()
    As = skus.count('A')
    if As != 0:

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
    return Cs + Ds + bs_sum +  as_sum

