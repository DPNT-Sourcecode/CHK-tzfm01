

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
    batches_As = (As // 3) * 130
    individual_As = (As % 3) * 50
    Bs = skus.count('B')
    batches_Bs = (Bs // 2) * 45
    individual_Bs = (Bs % 2) * 30
    Cs = skus.count('C') * 20
    Ds = skus.count('D') * 15

    return Cs + Ds + batches_As + individual_As + batches_Bs + individual_Bs

