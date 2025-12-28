print("Napisz zadnie , a policze ile masz znakow \n i czy jest to okej ")
string = input()

if len(string) <= 1:
    print(len(string), "wyrazow")
    print("Za krotkie ")
elif len(string) <= 10:
    print(len(string), "wyrazow")
    print("Juz lepiej")
elif len(string) <= 20:
    print(len(string), "wyrazow")
    print("Jestes na dobrej drodze :)")
elif len(string) <= 50:
    print(len(string), "wyrazow")
    print("O wiele lepiej ")
elif len(string) <= 100:
    print(len(string), "wyrazow")
    print("Brawo ty :)")
else:
    print(len(string), "wyrazow")
    print("To jest niesamowite !")
