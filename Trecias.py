pin = "1234"
while True:
    i = input("Įveskite PIN ")
    if i.isdigit():
        if i == pin:
            print("Seifas atsidare.")
            break
        else:
            print("Neteisingas PIN kodas. Bandykite dar kartą.")
