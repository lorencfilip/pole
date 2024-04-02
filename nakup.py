zbozi = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "Chlazení vodní"]
kosik = []

while True:
    for x in range(len(zbozi)):
        print(f"zbozi s cislem {x+1}: {zbozi[x]}")

    def vypis_pole(prvek):
        for x in range(len(prvek)):
            print(f"zbozi s cislem {x+1}: {prvek[x]}")


    prvek_minus = input("co si chces koupit ? ")
    zbozi.remove(prvek_minus)
    vypis_pole(zbozi)

    kosik.append(prvek_minus)

    print("stav vaseho kosiku: ")
    print(kosik)

    print("co dalsiho chces koupit?  m")