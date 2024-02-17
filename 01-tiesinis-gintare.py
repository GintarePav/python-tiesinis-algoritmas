# 12, 25. Viena gimnazijos klasė sugalvojo važiuoti į koncertą Kaune. Autobusas į Kauną veža už x eurų, o koncerto bilietas kainuoja y eurų. Į koncertą važiuoja m mokinių. Parašykite programą, kuri apskaičiuotų po kiek pinigų iš kiekvieno mokinio turėtų surinkti klasės auklėtoja, kad užtektų išvykai.

autobusoKaina = int(input("Kiek eurų kainuoja autobusas visai klasei? "))
koncertoKaina = int(input("Kiek eurų kainuoja koncerto bilietas vienam asmeniui? "))
mokiniuSkaicius = int(input("Kiek mokinių vyksta į koncertą? "))

bendraKaina = autobusoKaina + (koncertoKaina * mokiniuSkaicius)
kainaZmoguiEurai = bendraKaina // mokiniuSkaicius
kainaZmoguiCentai = bendraKaina % mokiniuSkaicius

# Pasitikrinkite. Jeigu x=120, y=10, m=23, turi būti spausdinama:
# Viso kelionė kainuos 350eur. Kadangi važiuoja 23 mokinai, tai vienam mokiniui kainuos apytiksliai 15eur. 21ct.

print(f'Viso kelionė kainuos {bendraKaina}eur. Kadangi važiuoja {mokiniuSkaicius} mokinai, tai vienam mokiniui kainuos apytiksliai {kainaZmoguiEurai}eur. {kainaZmoguiCentai}ct.')

# Atspausdinta: Viso kelionė kainuos 350eur. Kadangi važiuoja 23 mokinai, tai vienam mokiniui kainuos apytiksliai 15eur. 5ct.
# P.S. Pateiktame pavyzdyje, kad įvyktų kelionė mokiniams truks 17 centų. Laikysim, kad vežanti kompanija suteiks tokio dydžio nuolaidą.


