from rich import print
import time
import os

# === Main Function ===

def main():
    schuelerverzeichnis = []

    while True:
        clear_screen()
        print(
            "Bitte Wählen:\n\t1. Schüler anlegen\n\t2. Alle Schüler ausgeben\n\t3. Schüler löschen\n\t4. Programm beenden"
        )

        eingabe = input("> ")

        try:
            eingabe = int(eingabe.strip())

        except:
            continue

        if eingabe == 1:
            schuelerverzeichnis.append(schueler_anlegen())

        if eingabe == 2:
            schueler_anzeigen(schuelerverzeichnis)

        if eingabe == 3:
            schuelerverzeichnis = schueler_loeschen(schuelerverzeichnis)

        if eingabe == 4:
            exit()


def schueler_anlegen():
    clear_screen()
    print("\n[green]Neuen Schüler anlegen[/green]\n")
    while True:
        name = input("Name des Schuelers: ").strip()
        klasse = input("Klasse des schuelers: ").strip()
        iq = input("IQ des Schülers: ").strip()

        # === Leere Felder

        if name == "":
            print("[red]Es wurde kein Name angegeben.[/red]")
            continue

        if klasse == "":
            print("[red]Es wurde keine Klasse angegeben.[/red]")
            continue

        if iq == "":
            print("[red]Es wurde kein IQ angegeben.[/red]")
            continue

        # === IQ Parsen

        try:
            iq = int(iq)
        except:
            print("[red]Der IQ muss ein Zahlenwert sein.[/red]")
            continue

        # === Joshua Asmus

        if iq < 0 and name.lower() != "joshua asmus":
            print('[red]Der IQ darf nur bei "Joshua Asmus" negativ sein.[/red]')
            continue

        # === Return

        return {"name": name, "klasse": klasse, "iq": iq}


def schueler_anzeigen(liste):
    clear_screen()
    print("\n[green]Liste aller Schüler:[/green]\n")
    for idx, eintrag in enumerate(liste):
        print(f"Schüler ID: {idx}")
        for key, value in eintrag.items():
            print(f"{key}: {value}")

        print("\n" + 20 * "=" + "\n")
    print("[yellow]Drücken Sie Enter um zum Hauptmenü zu gelangen![/yellow]", end="")
    input()


def schueler_loeschen(list):
    clear_screen()
    while True:
        namen_ausgeben(list)

        print("\n[green]Geben Sie die ID des Schülers ein, den Sie löschen möchten.[/green]\n")
        schueler_id = input("> ")

        try:
            schueler_id = int(schueler_id)
        except:
            print("[red]Bitte geben Sie eine Zahl ein.[/red]")
            continue

        try:
            del(list[schueler_id])
        except:
            print(
                "[red]Diese ID existiert nicht. Es werden keine Änderungen vorgenommen."
            )

        print("\n[green]Schüler gelöscht[/green]\n")
        time.sleep(1)
        return list


def namen_ausgeben(list):
    for idx, schueler in enumerate(list):
        print(f"{idx}: {schueler["name"]}")


def clear_screen():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()
