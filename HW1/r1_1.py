# Takes 2 integer values and returns True if n is multiple of m
# so n = mi for some integer i
# returns False o/wise

print('Is it a multiple')
print('Please enter 2 numbers to be evaluated.')

def is_multiple(n, m):
    if n%m ==0:
        return True
    else:
        return False

n = int(input("Please enter a number: "))
m = int(input("Please enter a number: "))

print(is_multiple(n, m))

