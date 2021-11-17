from Domain.Librarie import vanzare_obiect, get_str_vanzare
from Logic.CRUD import create, delete


def show_all(vanzari):
    for vanzare in vanzari:
        print(get_str_vanzare(vanzare))


def main_line(vanzari, undo_list, redo_list):
    """"

    :param vanzari:
    :return:
    '''print('Scrieti help (pentru a vedea comenzile disponibile) sau dati comanda: ')
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
                    opt = optiune.split(", ")
                    if opt[0] == "add":
                        try:
                            vanzari = create(vanzari, int(opt[1]), opt[2], opt[3], float(opt[4]), opt[5], undo_list, redo_list)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif opt[0] == "showall":
                        show_all(vanzari)
                    elif opt[0] == "delete":
                        vanzari = delete(vanzari, int(opt[1]), [], [])
                    else:
                        print("Optiune gresita, scrieti 'help' pentru a vedea optiunile disponibile")
    """

    command_line_str = input('Dati comanda dorita: ')
    command_line = []
    command_line_str_split = command_line_str.split(', ')
    for i in command_line_str_split:
        command_line.append(i)
    for i in range(0, len(command_line)):
        if command_line[i] == 'add':
            try:
                vanzari = create(vanzari, int(command_line[i+1]), command_line[i+2], command_line[i+3], float(command_line[i+4]), command_line[i+5], undo_list, redo_list)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
        elif command_line[i] == 'showall':
            for vanzare in vanzari:
                print(get_str_vanzare(vanzare))
        elif command_line[i] == 'delete':
            try:
                vanzari = delete(vanzari, int(command_line[i+1]), undo_list, redo_list)
            except ValueError:
                print("Optiune gresita.")

    return vanzari

