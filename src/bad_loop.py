import time

def run_forever():
    """Boucle infinie (code smell volontaire pour SonarQube)."""
    while True:                # Noncompliant: infinite loop
        time.sleep(1)          # évite de consommer 100% CPU

if __name__ == "__main__":
    # NE PAS lancer pendant les tests
    run_forever()
