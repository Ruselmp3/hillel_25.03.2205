x =(int(input("Vvedit' 5 zhachne chislo: ")))

a5 = (x % 10)
a4 = ((x // 10) % 10)
a3 = ((x // 100) % 10)
a2 = ((x // 1000) % 10)
a1 = (x // 10000)

b1= a5 * 10000 + a4 * 1000 + a3 * 100 + a2 * 10 + a1

print(b1)