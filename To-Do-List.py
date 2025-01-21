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

if __name__ == "__main__":
    main()