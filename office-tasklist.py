# Definieren der Variable tasklist als Liste
tasklist = []

# Definieren der add_task Funktion
def add_task():
    task = input("\nWas hast du zu erledigen?")                             # Nutzer wird nach einer leeren Zeile gefragt: 'Was hast du zu erledigen?' und die Eingabe wird in der Variablen task gespeichert
    if task:                                                                # Wenn Eingabe vorhanden
        date = input("\nBis zu welchem Datum?")                             # Nutzer wird nach einer leeren Zeile gefragt: 'Bis wann?' und die Eingabe wird in der Variablen date gespeichert
        tasklist.append(f"{task} bis {date}")                               # Wert von task, bis und Wert von date werden als ein String der Aufgabenliste (tasklist) hinzugefügt
        print(f"\n{task} wurde der Aufgabenliste hinzugefügt")              # Gib aus: leere Zeile und '(Wert von task) wurde der Aufgabenliste hinzugefügt' in nächster Zeile
    else:                                                                   # Andernfalls
        print("\nDer Aufgabenliste wurde nichts hinzugefügt")               # Gib aus: leere Zeile und 'Der Aufgabenliste wurde nichts hinzugefügt' in nächster Zeile

# Definieren der show_tasklist Funktion
def show_tasklist():
    if not tasklist:                                                        # Wenn nichts in Aufgabenliste
        print("\nDeine Aufgabenliste ist leer")                             # Gib aus: leere Zeile und 'Deine Aufgabenliste ist leer' in nächster Zeile
    else:                                                                   # Andernfalls
        for x in tasklist:                                                  # Für jedes Element (x) in der Aufgabenliste (tasklist) tue:
            print(x)                                                        # Gib das jeweilige Element (x) aus/bzw. den Wert

# Definieren der main Funktion
def main ():
    while True:                                                             # Solange True wahr -> Unendlicher Loop, da True immer wahr, wird mit break beendet
        print("\n      Menü      ")                                         # Gib aus: leere Zeile und '      Menü      ' in nächster Zeile
        print("----------------")                                           # Gib aus:'----------------'
        print("\n1. Aufgabe hinzufügen")                                    # Gib aus: leere Zeile und '1. Aufgabe hinzufügen' in nächster Zeile
        print("\n2. Aufgabenliste anzeigen")                                # Gib aus: leere Zeile und '2. Aufgabenliste anzeigen' in nächster Zeile
        print("\n3. Programm beenden")                                      # Gib aus: leere Zeile und '3. Programm beenden' in nächster Zeile
        choice = input("\nWas möchtest du tun?")                            # Nutzer wird nach einer leeren Zeile gefragt: 'Was möchtest du tun?' und die Eingabe in der Variablen choice gespeichert
        if choice == "1":                                                   # Wenn der Wert von der string Variablen choice 1 ist
            add_task()                                                      # Starte die add_task Funktion
        elif choice == "2":                                                 # Desweiteren, wenn Wert von choice = 2
            show_tasklist()                                                 # Starte die show_tasklist Funktion
        elif choice == "3":                                                 # Desweiteren, wenn Wert von choice = 3
            print("\nProgramm wird beendet. Auf Wiedersehen!")              # Gib aus:'Programm wird beendet. Auf Wiedersehen!' und
            break                                                           # beende das Programm
        else:                                                               # Andernfalls
            print("\nKeine gültige Eingabe. Bitte wähle 1,2 oder 3!")       # Gib aus:'Keine gültige Eingabe. Bitte wähle 1,2 oder 3!'
            
# Lege Autostart für main Funktion fest
if __name__ == "__main__":
    main()