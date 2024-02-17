# 12, 24 užduotis: Taupyklėje guli n1 vieno cento vertės monetų, n2 – dviejų centų, n5 – penkių centų ir n10 – dešimties centų vertės monetų. Kokia suma guli taupyklėje? Išreikškite atsakymą eurais ir centais.

# Pasitikrinkite: Kai n1 = 3, n2 = 8, n5 = 6, n10 = 10, tai taupyklėje yra 1 eur. ir 49 ct.

centaiVienetukai = int(input("Kiek monetų po 1 ct.? "))
centaiDvejetukai = int(input("Kiek monetų po 2 ct.? "))
centaiPenketukai = int(input("Kiek monetų po 5 ct.? "))
centaiDesimtukai = int(input("Kiek monetų po 10 ct.? "))

visaSumaCentais = centaiVienetukai + (centaiDvejetukai * 2) + (centaiPenketukai * 5) + (centaiDesimtukai * 10)
sumaEurais = visaSumaCentais // 100
centuLikutis = visaSumaCentais % 100

print(f'Kai n1 = {centaiVienetukai}, n2 = {centaiDvejetukai}, n5 = {centaiPenketukai}, n10 = {centaiDesimtukai}, tai taupykėje yra {sumaEurais} eur. ir {centuLikutis} ct')

# Atspausdinta: Kai n1 = 3, n2 = 8, n5 = 6, n10 = 10, tai taupykėje yra 1 eur. ir 49 ct
