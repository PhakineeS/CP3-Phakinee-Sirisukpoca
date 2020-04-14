n = int(input("Size Of Pyramid : "))
lev = n-1
for i in range(1,n+1):
    print(' '*lev,end='')
    print('*'*(2*i-1))
    lev-=1