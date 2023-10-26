Istorija = []
while True:
    print("Pasirinkimai")
    print("Įveskite 'sudėti' norint sudėti")
    print("Įveskite 'atimti' norint atimti")
    print("Įveskite 'dauginti' norint daugybos")
    print("Įveskite 'dalinti' norint dalybos")
    print("Norint išeiti iš programos įveskite 'q'")
    print("Norint pasiekti skaičiavimu istorija įveskite 'Istorija'")

    ivestis = input("=>> ")
    if ivestis == "q":
        break
    if ivestis == "Istorija":
        if not Istorija:
            print("Nėra nieko")
        else:
            print("Skaičiavimu Įstorija")
            for x in Istorija:
                print(x)
        continue
    if ivestis in ["sudeti", "atimti", "dauginti", "dalinti"]:
        num1 = float(input("Įveskite pirmajį skaičių: "))
        num2 = float(input("Įveskite antrajį skaičių: "))
        if ivestis == "sudeti":
            rezultatas = num1 + num2
            Istorija.append(f"{num1} + {num2} = {rezultatas}")
        elif ivestis == "atimti":
            rezultatas = num1 - num2
            Istorija.append(f"{num1} - {num2} = {rezultatas}")
        elif ivestis == "dauginti":
            rezultatas = num1 * num2
            Istorija.append(f"{num1} * {num2} = {rezultatas}")
        elif ivestis == "dalinti":
            if num2 != 0:
                rezultatas = num1 / num2
                Istorija.append(f"{num1} / {num2} = {rezultatas}")
            else:
                rezultatas = "Dalyba iš nulio negalima"

        print("Štai jūsų rezultatas:", rezultatas)

print("new")
