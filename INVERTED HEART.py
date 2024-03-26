# define size n = even only
n = 8
 
# so this heart can be made n//2 part left,
# n//2 part right, and one middle line
# i.e; columns m = n + 1
m = n+1
 
# loops for upper part
for i in range(n//2-1):
    for j in range(m):
         
        # condition for printing stars to KK upper line
        if i == n//2-2 and (j == 0 or j == m-1):
            print("*", end=" ")
             
        # condition for printing stars to left upper
        elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
                            or (j-i == m//2-n//2+3 and j > m//4)):
            print("*", end=" ")
             
        # condition for printing stars to right upper
        elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
                           or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
            print("*", end=" ")
             
        # condition for printing spaces
        else:
            print(" ", end=" ")
    print()
 
# loops for lower part
for i in range(n//2-1, n):
    for j in range(m):
         
        # condition for printing stars
        if (i-j == n//2-1) or (i+j == n-1+m//2):
            print('*', end=" ")
             
        # condition for printing KK
        elif i == n//2-1:
             
            if j == m//2-1 or j == m//2+1:
                print('K', end=" ")
            else:
                print('K', end=" ")
                 
        # condition for printing spaces
        else:
            print(' ', end=" ")
             
    print()


    # determining the size of the hearT
    size = 15
 
# printing the inverted triangle
for a in range(0, size):
    for b in range(a, size):
        print(" ", end = "")
    for b in range(1, (a * 2)): 
        print("*", end = "") 
    print("")
 
# printing rest of the heart
for a in range(size, int(size / 2) - 1 , -2):
 
    # printing the white space right-triangle
    for b in range(1, size - a, 2):  
        print(" ", end = "")
 
    # printing the first trapezium
    for b in range(1, a + 1): 
        print("*", end = "")
 
    # printing the white space triangle
    for b in range(1, (size - a) + 1): 
        print(" ", end = "")
 
    # printing the second trapezium
    for b in range(1, a): 
        print("*", end = "")
 
    # new line
    print("")