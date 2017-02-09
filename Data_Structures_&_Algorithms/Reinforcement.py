#R-1.1
def is_multiple(n, m):
    print True if n % m == 0 else False
   


#R-1.2
#Revisit: function is from book, but it does not print line 11; cannot tell 
#if it is exectuing any of the code
def factors(n):
    print "here"
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
            
        k +=1

    if k * k == n:
        yield k



#R-1.3
#Can also add line below if I want to call with just "data"
#data = [2, 4, 5, 7, 8]
def minmax(data):
    result = data[0], data[-1]
    print result




#R-1.4
def sum_squares(n):
    sum = 0
    if n == 1:
        print sum

    for i in range(0,n):
        sum = sum + i*i
    print sum




#R-1.5
def sum_squares_2(n):
    squares = sum(k*k for k in range(1, n))
    print squares




#R-1.6
def sum_squares_3(n):
    sum = 0
    if n == 1:
        print sum

    for i in range(0,n):
        if i % 2 !=0:
            sum = sum + i*i
    print sum




#R-1.7
def sum_squares_4(n):
    squares = sum(k*k for k in range(1, n) if k % 2 !=0)
    print squares




#R-1.8
lst = [4, 5, 7, 9, 12, 16]
def negative_index(k, lst):
    n = len(lst)
    number = lst[n+k]
    print number




#R-1.9
lst = range(50, 90, 10)
#print lst




#R-1.10
lst = range(8, -10, -2)
#print lst




#R-1.11
powers_of_two = [pow(2, i) for i in range(1,9)]
print powers_of_two



#R-1.9
#is_multiple(8, 4)
#is_multiple(9, 4)
#factors(12)
#minmax([2,4,5,7,8])
#sum_squares(8)
#sum_squares_2(5)
#sum_squares_3(5)
#sum_squares_4(5)
#negative_index(-2, lst)


