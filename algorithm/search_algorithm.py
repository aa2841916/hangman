def ss(number_list,n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

number = range(0,100)
s1 = ss(number,2)
print(s1)

s2 = ss(number,102)

print(s2)
