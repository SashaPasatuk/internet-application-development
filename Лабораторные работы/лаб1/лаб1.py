import math
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
print ("Пасатюк Александра Дмитриевна ИУ5-53")
n=1
while n==1:
    print ("Введите коэффициенты А, В, С биквадратного уравнения Ах^4+Bx^2+C=0")
    A = input("A=")
    while is_number(A)==False :
        print("Некорректный коэффициент. Введите число.")
        A = input("A=")   
    B = input("B=")
    while is_number(B)==False :
        print("Некорректный коэффициент. Введите число.")
        B = input("B=")
    C = input("C=")  
    while is_number(C)==False :
        print("Некорректный коэффициент. Введите число.")
        C = input("C=")  
    A = float(A)
    B = float(B)
    C = float(C)
    if A==0:
        if B==0:
            if C==0:
                print ("x - любое число")
            else:
                print ("Корней нет")
        else:
            d=-C/B
            if d>0:
                print("x1=",-math.sqrt(d))
                print("x2=", math.sqrt(d))
            elif d<0:
                print ("Корней нет")
            else:
                print("x=0")
    else:
        if B==0:
            if C==0:
                print("x=0")
            else:
                d=-C/A
                if d<0:
                    print("Корней нет")
                else:
                    print ("x1=", math.sqrt(math.sqrt(d)))
                    print ("x2=", -math.sqrt(math.sqrt(d)))
        else:
            d=B*B-4*A*C
            if d<0:
                print("Корней нет")
            elif d==0:
                m=(-B+math.sqrt(d))/(2*A)
                if m<0:
                    print("Корней нет")
                elif m==0:
                    print("x=0")
                else:
                    print("x1=", math.sqrt(m))
                    print("x2=",-math.sqrt(m))
            else:
                m1=(-B+math.sqrt(d))/(2*A)
                m2=(-B-math.sqrt(d))/(2*A)
                if m1>0:
                    print("x1=", math.sqrt(m1))
                    print("x2=", -math.sqrt(m1))
                    if m2>0:
                        print("x3=", math.sqrt(m2))
                        print("x4=", -math.sqrt(m2))
                    elif m2==0:
                        print("x3=0")
                elif m1==0:
                    print("x1=0")
                    if m2>0:
                        print("x2=", math.sqrt(m2))
                        print("x3=", -math.sqrt(m2))
                    elif m2==0:
                        print("x2=0")
                else:
                    if m2>0:
                        print("x1=", math.sqrt(m2))
                        print("x2=", -math.sqrt(m2))
                    elif m2==0:
                        print("x1=0")
                    else:
                        print ("Корней нет")
    n=input("Введите 1, если хотите решить другое уравнение, или введите 0 для завершения программы: ")
    n=float(n)
