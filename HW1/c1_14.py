# takes sequence of integer values and determines if distinct pair of numbers w/ odd product

list = []  # init list

n = int(input("Enter number of elements. Then enter the elements line by line. # of elements? "))

for i in range(0, n):       # iter till end
    ints = int(input())

    list.append(ints)   # add the ints to the list



def op(list):
    for i in range(0, n):  # get an int from list
        for j in range(0, n):  # get another int
            if i != j:   #making sure not same
                odprod = list[i] * list[j]
                if odprod % 2 == 1:
                    return True
    return False



if op(list):     #calling function, if true prints yes if false print none
    print("There is an odd pair.")
else:
    print("There is not an odd pair")