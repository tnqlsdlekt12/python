a = 1
if a == 1:
    print("참")
else:
    print("거짓")
    
if a < 1:
    print("a는 1보다 작다.")
else:
    print("a는 1보다 크거나 같다.")

if a < 1:
    print("a는 1보다 작다.")
else:
    if a == 1:
        print("a는 1이랑 같다.")
    print("a는 1보다 크다.")

if a < 1:
    print("a는 1보다 작다.")
elif a == 1:
    print("a는 1이랑 같다.") 
else:
    print("a는 1보다 크다.")

