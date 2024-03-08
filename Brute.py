import itertools
import string

# A karakterek listája, amelyeket a jelszóban használhatunk
characters = string.ascii_letters + string.digits + string.punctuation

# A támadás célja
target_password = "secret"

# Jelszó hossza
password_length = len(target_password)

print("Jelszó keresés")
number=0

# Brute force támadás
for length in range(1, password_length + 1):
    for guess in itertools.product(characters, repeat=length):
        # Az aktuális próbálkozás konvertálása stringgé
        attempt = ''.join(guess)
        
        # Ellenőrizzük, hogy az aktuális próbálkozás egyezik-e a céllal
        number+=1
        print(f"{number}.próba Jelszó keresés : {attempt}")
        if attempt == target_password:
            print(f"Jelszó megtalálva: {attempt}")
            break
