
from datetime import datetime

cnp = "29902190450000"

# # Formatul
# if not isinstance(cnp, str): return False
# if not cnp.isdigit(): return False
# if len(cnp) != 13: return False

gen = int(cnp[0])
# if gen not in range(1, 9): return False

an = cnp[1:3]

if gen in [1, 2]:
    an_cal = 1900 
elif gen in [3, 4]:
    an_cal = 1800
if gen in [5, 6]:
    an_cal = 2000

an_cal +=  int(an)

# # Anul trebuie sa fie cu 14 an mai mic cel putin decat anul curent
# if datetime.now().year - 14 < an_cal: return False


# luna = int(cnp[3:5])
# if luna not in range(1, 13): return False

# zi = int(cnp[5:7])
# if zi not in range(1, 32): return False

# if luna in [4,6,9,11] and zi not in range(1, 31): return False

# if luna == 2:
#     if zi not in range(1, 30): return False
#     este_bisect = (an_cal % 400 == 0 or (an_cal % 4 == 0 and an_cal % 100 != 0))
#     if zi == 29 and not este_bisect : return False


judet = int(cnp[7:10])
# if judet not in (list(range(1, 49)) + [51, 52, 70]): return False

masca = "279146358279"

suma = 0
for i in range(12):
    suma += int(cnp[i]) * int(masca[i])

# Rezultatele înmulțirilor sunt însumate, iar numărul rezultat se împarte la 11.
rest = suma % 11
print("Orice.../")
print("restul :", rest)

# # Dacă restul împărțirii este mai mic decât 10, atunci acel număr reprezintă cifra de control, cea de 13-a cifra a CNP-ului.
# if rest < 10 and str(rest) != cnp[-1]: return False

# # În schimb, dacă restul împărțirii este 10, atunci cifra de control este 1.
# if rest == 10 and str(rest) != "1": return False

    

# print(este_valid("29902190450000"))
