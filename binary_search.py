def binary_search(items, n):
    first = 0
    last = len(items) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if items[midpoint] == n:
            found = True
        else:
            if n < items[midpoint]:
                last = midpoint-1
            else:
                first = midpoint + 1

    return found


result = binary_search([1,2,3,4,5,666,777,888,9999999,2222222222222],123)
print(result)
