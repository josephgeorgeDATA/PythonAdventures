# Collatz Program

def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    if number % 2 ==1:
        print (3 * number + 1)
        return 3 * number + 1

print ('Enter a number ...')
num = input()

for x in range (1,1000):
    num = collatz (int (num))
    if num == 1:
        break