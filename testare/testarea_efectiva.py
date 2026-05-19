
from functia_de_testat import este_bisect_v1
from o_alta_functie_de_testat import este_bisect_v2


## Intai scriu un test care nu trece, apoi scriu atat de putin cod in cat sa treaca 

este_bisect = este_bisect_v2

## Testul 1
assert este_bisect(2026) == False, "Anul 2026 nu este bisect"

## Testul 2
assert este_bisect(2024) == True, "Anul 2024 este bisect"

## Testul 3
assert este_bisect(100) == False, "Anul 100 nu este bisect"

## Testul 4
assert este_bisect(400) == True, "Anul 400  este bisect"