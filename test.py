def my_func():
    name = input("Jak masz na imie? ")
    age_raw = input("Podaj swoj wiek :) ")

    try:
        age = int(age_raw)
        if age <= 0:
            print("Podales zly wiek! Tak sie nie bawimy.")
            return
    except ValueError:
        print("Podaj prosze wiek a nie sie bawisz!")
        return

    print(f"Czyli nazywasz sie {name} i masz {age} lat.")

    agree = input("Czy chcesz zeby zapisal twoje dane?? Tak lub Nie ").strip().lower()
    if agree == "tak":
        with open("data.txt", "a") as file:
            file.write(f"{name} {age}\n")
        print("Zapisano!")
    elif agree == "nie":
        print("Okej, to nie zapisuje.")
    else:
        print("Nie rozumiem cie.")


my_func()
