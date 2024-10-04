# Definieren der Variable tasklist als Liste
tasklist = []

# Definieren der add_task Funktion
def add_task():
    task = input("Was hast du zu erledigen?")                   # Nutzer wird gefragt: 'Was hast du zu erledigen?' und die Eingabe wird in der Variablen task gespeichert
    if task:                                                    # Wenn Eingabe vorhanden
        date = input("Bis wann?")                               # Nutzer wird gefragt: 'Bis wann?' und die Eingabe wird in der Variablen date gespeichert
        tasklist.append(f"{task} bis {date}")                   # Wert von task, bis und Wert von date werden als ein String der Liste tasklist hinzugefügt
        print(f"{task} wurde der Aufgabenliste hinzugefügt")    # Gib aus: '(Wert von task) wurde der Aufgabenliste hinzugefügt
    else:                                                       # Andernfalls
        print("Nichts hinzugefügt")                             # Gib aus: 'Nichts hinzugefügt'
add_task()
print(tasklist)