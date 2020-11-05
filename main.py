lo = int(input("What is the largest number's value?  "))
m = int(input("What is the middle number's value?  "))
s = int(input("What is the smallest number's value?  "))
max = lo / s
if lo < m or m < s or lo < s:
    print("That's not valid. Make sure numbers are in order.")
else:
    x = 0
    y = 0
    off = 0
    l = lo
    while m * x + s * y != l:
        off = 0
        while m * x + s * y != l and off < max:
            y = 0
            x = 0
            y = y + off
            while y < max and m * x + s * y != l:
                y = y + 1
                x = x + 1
            off = off + 1
        off = 0
        while m * x + s * y != l and off < max:
            x = 0
            y = 0
            x = x + off
            while x < max and m * x + s * y != l:
                y = y + 1
                x = x + 1
            off = off + 1
        if m * x + s * y != l:
            l = l - 1
    if m * x + s * y == l:
        rem = lo - ((m * x) + (s * y))
        print(x,y)
        print("The least possible remainder is", rem)
