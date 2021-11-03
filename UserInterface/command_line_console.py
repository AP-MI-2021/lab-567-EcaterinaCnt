from Domain.Librarie import vanzare_obiect
from Logic.CRUD import create, delete


def show_all(vanzari):
    for vanzare in vanzari:
        print(vanzare_obiect(vanzare))


def main_line(vanzari):
    print('Scrieti help (pentru a vedea comenzile disponibile) sau dati comanda: ')
    while True:
        givenString = input()
        if givenString == "help":
            print("add, id, titlu, gen, pret, reducere")
            print("delete, id")
            print("showall")
            print("exit")
        else:
            optiuni = givenString.split(";")
            if optiuni[0] == "exit":
                break
            else:
                for optiune in optiuni:
                    opt = optiune.split(",")
                    if (opt[0] == "add"):
                        try:
                            vanzari = create(vanzari, int(opt[1]), opt[2], opt[3], opt[4], opt[5])
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif opt[0] == "showall":
                        show_all(vanzari)
                    elif opt[0] == "delete":
                        vanzari = delete(vanzari, int(opt[1]))
                    else:
                        print("Optiune gresita, scrieti 'help' pentru a vedea optiunile disponibile")

