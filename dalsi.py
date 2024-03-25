cars = ["ford", "volvo", "bmw", "audi"]

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f"auto s cislem {x+1}: {prvek[x]}")

vypis_pole(cars)

prvek_minus = input("jake auto chcete odebrat? ")
cars.remove(prvek_minus)
vypis_pole(cars)