try:
    def divisor_volume_and_miscellany(n):
        divisor_volume = 0
        divisor_sum = 0
        divisors = []
        for i in range(1, n+1):
            if n %i == 0:
                divisor_volume += 1
                divisor_sum += i
                divisors.append(i)
        if divisor_volume == 2:
            print(f"{n} Ushbu son toq son. This number is odd!")
        else:
            print(f"Bo'luvchilar soni {divisor_volume}, Bo'luvchilar yig'indisi {divisor_sum},\nBo'luvchilari {divisors}")
except:
    print("Kiritishda xatolik ! qaytadan ununing !!!")


n = int(input("Berilgan sonni kiriting : "))
divisor_volume_and_miscellany(n)
