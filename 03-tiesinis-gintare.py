# 5, 12, 17. Įvedamas dydis sekundėmis. Parašykite programą, kuri tą dydį paverstu valandomis, minutėmis ir sekundėmis.

sekundes = int(input("Įveskite norimą skaičių: "))

istrauktosValandos = sekundes // 3600
valanduLikutis = sekundes % 3600
istrauktosMinutes = valanduLikutis // 60
likusiosSekundes = valanduLikutis % 60

print(f'{sekundes} sekundės sudaro {istrauktosValandos} val. {istrauktosMinutes} min. ir {likusiosSekundes} s.')