import math
def sieve():
    end_of_range = int(input("Enter the end of the range:"))
    tab = [True]*(end_of_range-1)
    prime_numbers = []
    actual_number = 2
    eor_root = math.sqrt(end_of_range)
    while actual_number <= eor_root:
        status = tab[actual_number-2]
        if status == True:
            plotted_number = actual_number*2
            while plotted_number <= end_of_range:
                tab[plotted_number-2] = False
                plotted_number += actual_number
        actual_number += 1
    examined = 2
    while examined <= end_of_range:
        if tab[examined-2] == True:
            prime_numbers.append(examined)
            examined += 1
        else:
            examined += 1
    print("Prime numbers from range 0 -",end_of_range, prime_numbers)

print(sieve())