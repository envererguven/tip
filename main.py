fis=input("How much was the total bill?:\n")

fis=float(fis)

kisi=input("Between how many people would you like to split the bill?:\n")
bahsis=input("How much of a bill would you like to give?[Popular tips 10/12/15%]\n")


bahsis=int(bahsis)
kisi=int(kisi)

toplam=fis+fis*(bahsis/100)

kisi_basi=toplam/kisi
kisi_basi_y=round(kisi_basi,2)

toplam=round(toplam,2)

print(f"Each person should pay ${kisi_basi_y} in a total of {toplam}")
