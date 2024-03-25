cars = ["ford", "volvo", "bmw", "audi"]

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f"auto s cislem {x+1}: {prvek[x]}")

vypis_pole(cars)
prvek_plus = input("zadejte auto, ktere chcete pridat: ")

print("")
cars.append(prvek_plus)
vypis_pole(cars)

prvek_minus = int(input("jakou pozici chcete odebrat? "))
cars.pop(prvek_minus)
vypis_pole(cars)
