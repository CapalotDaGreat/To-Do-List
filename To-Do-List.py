import json
from datetime import datetime, timedelta


def load_tasks(filename="tasks.json"):
    """
    Laden von Aufgaben aus einer JSON-Datei.
    """
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename="tasks.json"):
    """
    Speichern von Aufgaben in einer JSON-Datei.
    """
    with open(filename, 'w') as f:
        json.dump(tasks, f, default=str)


def display_tasks(tasks):
    """
    Anzeigen aller Aufgaben.
    """
    if not tasks:
        print("Keine Aufgaben in der Liste.")
    else:
        print("Aktuelle Aufgaben:")
        for index, task in enumerate(tasks, start=1):
            task_type = "Einmalig" if task.get('recurring') is None else "Wiederholend"
            due_date = task.get('due_date', "Kein Fälligkeitsdatum")
            print(f"{index}. {task['description']} - Typ: {task_type}, Fällig am: {due_date}")


def add_task(tasks):
    """
    Hinzufügen einer neuen Aufgabe (einmalig oder wiederkehrend).
    """
    description = input("Geben Sie die Aufgabe ein: ")

    while True:
        due_date = input(
            "Geben Sie das Fälligkeitsdatum ein (YYYY-MM-DD) oder 'w' für wiederkehrende Aufgaben: "
        )

        if due_date.lower() == 'w':
            try:
                interval = int(input("Geben Sie das Intervall in Tagen für die wiederkehrende Aufgabe ein: "))
                due_date = (datetime.now() + timedelta(days=interval)).strftime('%Y-%m-%d')
                task = {'description': description, 'due_date': due_date, 'recurring': interval}
                break
            except ValueError:
                print("Bitte geben Sie ein gültiges Intervall ein.")
        else:
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
                task = {'description': description, 'due_date': due_date, 'recurring': None}
                break
            except ValueError:
                print("Bitte geben Sie ein gültiges Fälligkeitsdatum im Format YYYY-MM-DD ein.")

    tasks.append(task)
    save_tasks(tasks)
    print(f"Aufgabe '{description}' hinzugefügt.")


def delete_task(tasks):
    """
    Löschen einer Aufgabe anhand ihrer Indexnummer.
    """
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_index = int(input("Geben Sie die Nummer der Aufgabe ein, die Sie entfernen möchten: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Aufgabe '{removed_task['description']}' entfernt.")
        else:
            print("Ungültige Nummer.")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")


def update_recurring_tasks(tasks):
    """
    Aktualisieren von wiederkehrenden Aufgaben: Verschieben von fälligen Aufgaben basierend auf ihrem Intervall.
    """
    today = datetime.now()
    for task in tasks:
        if task.get('recurring') is not None:
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d')
            while due_date < today:
                due_date += timedelta(days=task['recurring'])
            task['due_date'] = due_date.strftime('%Y-%m-%d')


def main():
    """
    Hauptprogramm für das Aufgabenverwaltungsprogramm.
    """
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        update_recurring_tasks(tasks)
        save_tasks(tasks)

        print("\nAufgabenverwaltung")
        print("1. Eine Aufgabe hinzufügen")
        print("2. Alle Aufgaben anzeigen")
        print("3. Aufgabe löschen")
        print("4. Programm beenden")

        choice = input("Bitte eine Option auswählen (1-4): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)
            input("Drücken Sie 'Enter', um fortzufahren...")

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine Option zwischen 1 und 4.")


if __name__ == "__main__":
    main()
