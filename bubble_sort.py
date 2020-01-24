def bubble_sort():
    tab = []
    n = int(input("Enter the amount of numbers:"))
    i = 0
    while i < n:
        number = int(input("Enter number:"))
        tab.append(number)
        i += 1
    while n > 1:
        i = 0
        while i < n-1:
            if tab[i] > tab[i+1]:
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
                i += 1
            else:
                i += 1
        n -= 1
    return tab
print(bubble_sort())