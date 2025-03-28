x =(int(input("Vvedit' 5 zhachne chislo: ")))

a5 = (x % 10)
a4 = ((x // 10) % 10)
a3 = ((x // 100) % 10)
a2 = ((x // 1000) % 10)
a1 = (x // 10000)

print(a5,a4,a3,a2,a1)