s = '1abcddcaba'
for i in s:
    if not s:
        print("ok")
        break
    if i != s[-1]:
        print("not ok")
        break
    else:
        s = s[1:-1]


