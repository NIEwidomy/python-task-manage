import sys
import json

try:
    funkcja = sys.argv[1]
except IndexError:
    sys.exit("Podaj 1 argument")

try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}
except json.JSONDecodeError:
    sys.exit("Błędny JSON")

def dodanie(wartosc):
    tablica = []
    for i in data.keys():
        tablica.append(int(i))
        
    nowe_id = 0
    if len(tablica) == 0:
        nowe_id = 0
    else:
        nowe_id = max(tablica)+1
    data[str(nowe_id)] = {'name': wartosc, 'status': False}
    with open("data.json", "w") as j:
        json.dump(data, j)
    
def wylistowanie():
    for i in data.keys():
        print("ID: ",i, "Nazwa zadania: ",data[i]['name'], " Czy wykonane:", data[i]['status'])

def zrobione(wartosc):
    if wartosc not in data:
                sys.exit("nie ma takiego id w bazy")
    for i in data.keys():
        if int(i) == int(wartosc):
            data[i].update({'status': True})
    
    with open("data.json", "w") as j:
            json.dump(data, j)
    
def usuwanie(wartosc):
    if wartosc not in data:
                sys.exit("Nie ma zadania o takim ID")
    for i in data.keys():
        if int(i) == int(wartosc):
            data.pop(i)
            break
    with open("data.json", "w") as j:
        json.dump(data, j)
    
        


if funkcja == "add":
    try:
        argument = sys.argv[2]
    except IndexError:
        sys.exit("Podaj argument")
    if argument.strip() == "":
        sys.exit("Podaj jakie ma byc zadanie")
    else:
        dodanie(argument)
elif funkcja == "list":
    wylistowanie()
elif funkcja == "done":
    try:
        argument = sys.argv[2]
        int(argument)
    except (ValueError, IndexError):
        sys.exit("Podaj argument/prawidłowy argument")
    zrobione(argument)
elif funkcja == "delete":
    try:
        argument = sys.argv[2]
        int(argument)
    except (ValueError, IndexError):
        sys.exit("Podaj argument/prawidłowy argument")
    usuwanie(argument)
else:
    print("Nie ma takiej funkcji")