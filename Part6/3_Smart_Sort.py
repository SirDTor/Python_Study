def byAbs_key(element):
    return abs(element)

elements = (-20, -5, 10, 15)
elements = sorted(elements, key=byAbs_key)
print(elements)
