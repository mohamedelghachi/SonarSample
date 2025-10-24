import time
# add tow ints
def add(a: int, b: int) -> int:
    """Addition simple."""
    return a + b
# add1 function
def add1(a: int, b: int) -> int:
    """Addition simple."""
    return a + b

def run_forever():
    """Boucle infinie (code smell volontaire pour SonarQube)."""
    while True:                # Noncompliant: infinite loop
        time.sleep(1)          # évite de consommer 100% CPU


def is_palindrome(s: str) -> bool:
    """Retourne True si s est un palindrome (insensible à la casse/espaces)."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # Petit bout de code exécutable
    print("2 + 3 =", add(2, 3))
    print("'Radar' est palindrome ?", is_palindrome("Radar"))
    print(run_forever)
