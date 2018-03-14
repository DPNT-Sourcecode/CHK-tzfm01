

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
    batches_As = As // 3
    individual_As = As % 3
    Bs = skus.count('B')
    Cs = skus.count('C') * 20
    Ds = skus.count('D') * 15

    return 30

