elements = sorted([3, 6, 20, 99, 10, 15])
elements_len = len(elements)
if elements_len % 2 != 0:
    index = elements_len/2-0.5
    print(elements[int(index)])
else:
    index = int(elements_len/2-1)
    result = elements[index] + elements[index+1]
    print(result/2)
