tid = input("Hur många sekunder vill du konvertera till timmar och minuter:")
sek1 = int(tid)
sek2 = int(tid)
a = sek1//60
z = a%60
b = sek2%60
c = sek1//3600
print(f"Det blir {c} timmar {z} minuter och {b} sekunder ")
