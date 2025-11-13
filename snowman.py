import random
# Importiert die STAGES Liste aus der neuen Datei
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown", "java", "stralsund"]
 
def get_random_word():
    """Selects a random word from the list."""
    # Verwende random.choice für eine einfachere Auswahl
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt den aktuellen Spielstand an (ASCII-Art und Wort-Status)."""
    print("\n" + "="*30)
    print(STAGES[mistakes]) # Zeigt die ASCII-Art basierend auf der Anzahl der Fehler

    # Generiert die Wortanzeige (mit Unterstrichen)
    display_word_list = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_word_list.append(letter)
        else:
            display_word_list.append("_")
            
    print("\nAktuelles Wort: ", " ".join(display_word_list))
    print("Bereits geraten: ", ", ".join(sorted(guessed_letters)))
    print("="*30 + "\n")

def play_game():
    """Führt eine Spielrunde "Snowman Meltdown" aus."""
    secret_word = get_random_word()
    guessed_letters = set() # Ein Set verhindert doppelte Einträge
    # display_word wird weiterhin intern für die Sieg-Bedingung benötigt
    display_word = ["_"] * len(secret_word) 
    mistakes = 0 # Variable für Fehler initialisiert
    max_wrong_guesses = len(STAGES) - 1

    print("Willkommen bei Snowman Meltdown!")
    print(f"Das Wort hat {len(secret_word)} Buchstaben. Du hast {max_wrong_guesses} Fehlversuche.")

    # --- Haupt-Spielschleife ---
    while mistakes < max_wrong_guesses:
        # Zeigt den Zustand *vor* der Eingabeaufforderung an
        display_game_state(mistakes, secret_word, guessed_letters)

        # 1. Rateversuch einholen
        guess = input("Rate einen Buchstaben: ").lower().strip() # .strip() entfernt Leerzeichen

        # 2. Eingabe validieren
        if not guess.isalpha() or len(guess) != 1:
            print("Ungültige Eingabe. Bitte gib einen einzelnen Buchstaben ein.")
            continue
        
        if guess in guessed_letters:
            print(f"Den Buchstaben '{guess}' hast du schon geraten. Versuche einen anderen.")
            continue

        # 3. Rateversuch verarbeiten
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Gut geraten! '{guess}' ist im Wort enthalten.")
            # display_word (interne Liste) aktualisieren
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
        else:
            print(f"Falsch! '{guess}' ist nicht im Wort. Der Schneemann schmilzt...")
            mistakes += 1 # Fehlerzähler erhöhen

        # 4. Sieg-Bedingung prüfen (verwendet die interne display_word Liste)
        if "_" not in display_word:
            print("\n" + "*"*30)
            print("Herzlichen Glückwunsch! Du hast das Wort erraten!")
            print(f"Das Wort war: {secret_word}")
            print("*"*30 + "\n")
            break # Spielschleife verlassen

    # 5. Niederlage-Bedingung prüfen
    if mistakes == max_wrong_guesses:
        # Zeigt den finalen (geschmolzenen) Zustand an
        display_game_state(mistakes, secret_word, guessed_letters)
        print("\n" + "!"*30)
        print("Oh nein! Der Schneemann ist geschmolzen!")
        print(f"Das gesuchte Wort war: {secret_word}")
        print("!"*30 + "\n")

def main():
    """Hauptfunktion, um das Spiel zu starten und Wiederholungen zu ermöglichen."""
    while True:
        play_game()
        
        play_again = input("Möchtest du nochmal spielen? (j/n): ").lower().strip()
        if play_again != 'j':
            print("Danke fürs Spielen! Bis zum nächsten Mal.")
            break

if __name__ == "__main__":
    # Ruft die Hauptfunktion auf, die die Spiel- und Wiederholungsschleife enthält
    main()