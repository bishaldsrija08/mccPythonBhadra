'''
*
**
***
****
*****
'''

row = 5
for i in range(1, row+1): # outer loop
    for j in range(1, i+1): # inner loop
        print("*", end=" ")
    print()