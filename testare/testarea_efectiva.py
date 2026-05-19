
from functia_de_testat import este_bisect


## Intai scriu un test care nu trece, apoi scriu atat de putin cod in cat sa treaca 

## Testul 1
assert este_bisect(2026) == False, "Anul 2026 nu este bisect"

## Testul 2
assert este_bisect(2024) == True, "Anul 2024 este bisect"

assert este_bisect(100) == False, "Anul 100 nu este bisect"

assert este_bisect(400) == True, "Anul 400  este bisect"