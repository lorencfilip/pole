cars = ["ford", "volvo", "bmw", "audi"]

for x in range(len(cars)):
    print(f"auto s cislem {x+1}: {cars[x]}")


print("")
cars.append("nic nebude")

for x in range(len(cars)):
    print(f"auto s cislem {x+1}: {cars[x]}")