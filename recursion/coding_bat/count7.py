def countSeven(num):
    if num == 0:
        return 0
    if num%10 == 7:
        return 1 + countSeven(num//10)
    return countSeven(num//10)
print(countSeven(1237177777))