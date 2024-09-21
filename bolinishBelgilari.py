def ikkigaBoluvhi(a):
    if a % 2 == 0:
        print(f"Ushbu {a} soni 2 ga bo'linadi!")
    else:
        print(f"Ushbu {a} son 2 ga bo'linmaydi!")


son = list(input("Sonni kiriting : "))

ikkigaBoluvhi(son[-1])
