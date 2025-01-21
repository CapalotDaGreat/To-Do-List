def display_tasks(tasks):
    if not tasks:
        print("Keine Aufgaben in der Liste.")
    else:
        print("Aktuelle Aufgaben:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []

    while True:
        print("\nAufgabenverwaltung")
        print("1. Eine Aufgabe hinzufügen")
        print("2. Alle Aufgaben anzeigen")
        print("3. Aufgabe löschen")
        print("4. Programm beenden")

        choice = input("Bitte eine Option auswählen (1-4): ")

        if choice == "1":
            task = input("Neue Aufgabe eingeben: ")
            tasks.append(task)
            print(f"Aufgabe '{task}' hinzugefügt.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            try:
                task_index = int(input("Geben Sie die Nummer der Aufgabe ein, die Sie entfernen möchten: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Aufgabe '{removed_task}' entfernt.")
                else:
                    print("Ungültige Nummer.")
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")

        elif choice == '4':
            print("Programm beendet.")
            break

        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine Option zwischen 1 und 4.")

if __name__ == "__main__":
    main()