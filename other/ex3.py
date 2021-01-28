s = input()
r = s.rfind('.')
l = s.find('.')
m = s.find('.', l+1)
if (r != -1 and l != -1 and m != -1) and (r != m and r != l and l != m):
    n1 = int(s[0:l])
    n2 = int(s[l+1:m])
    n3 = int(s[m+1:r])
    n4 = int(s[r+1:])
    if(0 <= n1 <= 255 and 0 <= n2 <= 255 and 0 <= n3 <= 255 and 0 <= n4 <= 255):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
