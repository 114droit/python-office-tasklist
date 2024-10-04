# Definieren der Variable tasklist als Liste
tasklist = []

# Definieren der add_task Funktion
def add_task():
    task = input("\nWas hast du zu erledigen?")                   # Nutzer wird gefragt: 'Was hast du zu erledigen?' und die Eingabe wird in der Variablen task gespeichert
    if task:                                                    # Wenn Eingabe vorhanden
        date = input("\nBis zu welchem Datum?")                   # Nutzer wird gefragt: 'Bis wann?' und die Eingabe wird in der Variablen date gespeichert
        tasklist.append(f"{task} bis {date}")                   # Wert von task, bis und Wert von date werden als ein String der Liste tasklist hinzugefügt
        print(f"\n{task} wurde der Aufgabenliste hinzugefügt")    # Gib aus: '(Wert von task) wurde der Aufgabenliste hinzugefügt
    else:                                                       # Andernfalls
        print("\nDer Aufgabenliste wurde nichts hinzugefügt")     # Gib aus: 'Nichts hinzugefügt'

# Definieren der show_tasklist Funktion
def show_tasklist():
    if not tasklist:
        print("\nDeine Aufgabenliste ist leer")
    else:
        for x in tasklist:
            print(x)

# Definieren der main Funktion
def main ():
    while True:
        print("\n      Menü      ")
        print("----------------")
        print("\n1. Aufgabe hinzufügen")
        print("\n2. Aufgabenliste anzeigen")
        print("\n3. Programm beenden")
        choice = input("\nWas möchtest du tun?")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            print("\nProgramm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("\nKeine gültige Eingabe. Bitte wähle 1,2 oder 3!")
main ()