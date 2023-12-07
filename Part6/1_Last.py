elements = [[0, 1, 2, 3, 4, 5], [1, 3, 5], []]
elements_inner_sum = 0
for elements_inner in elements:
    i = 0
    if not elements_inner:
        print(0)
        break

    elements_inner_length = len(elements_inner)
    while (i < elements_inner_length):
        elements_inner_sum += elements_inner[i]
        i += 2

    print(elements_inner_sum*elements_inner[elements_inner_length-1])
