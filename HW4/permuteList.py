import copy

# ACKNOWLEDGEMENTS: Justin Tanon, Patrick Morehead

def permute(originalList, aPermutation):
    if originalList == []:
        print(aPermutation)
    for x in range(len(originalList)):
        e = [originalList[x]]  # made e a list
        l2 = originalList[:x] + originalList[x+1:]
        p2 = e + aPermutation
        permute(l2, p2)

    

def printPermutations(a):
    permute(a, [])

myArray = []
try:
    n = int(input("Enter integers, 0 to stop "))
    while n != 0:
        myArray.append(n)
        n = int(input("Enter integers, 0 to stop "))
    print("The original list: ",myArray)
    printPermutations(myArray)
except ValueError:
    print("Invalid input")