from Domain.Librarie import get_str_vanzare, get_titlu, get_gen, get_pret, get_tip_reducere, \
     vanzare_obiect
from Logic.CRUD import create, read, update, delete
from Logic.undo_redo_efficient import do_undo_inefficient, do_redo_inefficient
from Logic.modificari import modificare_vanzare, change_gen, ord_price, pret_minim, afisare_titluri_dupa_gen


def show_menu():
    print('1. CRUD')
    print('2. Reducere pret pentru anumite vanzari.')
    print('3. Schimbarea genului unei carti cu titlul dat.')
    print('4. Determina pretul minim in functie de gen.')
    print('5. Ordonarea crescatoare a cartilor in functie de pret.')
    print('6. Afiseaza titlurile distincte in functie de gen.')
    print('u. Undo.')
    print('r. Redo.')
    print('x. Exit')


def handle_add(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii : '))
        titlu = input('Dati titlul cartii : ')
        gen = input('Dati genul cartii : ')
        pret = float(input('Dati pretul cartii : '))
        tip_reducere = input('Dati tipul reducerii vanzarii in functie de client: ')
        return create(vanzari, id_vanzare, titlu, gen, pret, tip_reducere, undo_list, redo_list)
    except ValueError as ve:
        print("Nu ati introdus un numar corect! Detalii: ", ve)
    return vanzari


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str_vanzare(vanzare))


def handle_show_details(vanzari):
    id_vanzare = int(input('Dati id-ul vaznarii pentru care doriti detalii: '))
    vanzare = read(vanzari, id_vanzare)
    print(f'Titlu: {get_titlu(vanzare)}')
    print(f'Gen: {get_gen(vanzare)}')
    print(f'Pret: {get_pret(vanzare)}')
    print(f'Tip de reducere: {get_tip_reducere(vanzare)}')


def handle_update(vanzari, undo_list, redo_list):
    try:
        id_vanzari = int(input('Dati id-ul vanzarii care se actualizeaza: '))
        titlu = input('Dati noul nume al cartii vandute: ')
        gen = input('Dati noul gen al cartii vandute: ')
        pret = float(input('Dati noul pret al cartii vandute: '))
        tip_reducere = input('Dati noul tip de reducere ce se poate face clientului: ')
        return update(vanzari, vanzare_obiect(id_vanzari, titlu, gen, pret, tip_reducere), undo_list, redo_list)
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_delete(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii care se va sterge: '))
        vanzari = delete(vanzari, id_vanzare, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return vanzari
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_change_gen(vanzari,undo_list, redo_list):
    try:
        titlul=input('Dati titlul cartii: ')
        gen= input('Noul gen al cartii este: ')
        vanzari=change_gen(vanzari, titlul, gen, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari

def handle_pret_minim(vanzari):
    pret=pret_minim(vanzari)
    for gen in pret:
        print('Genul {}, are pretul minim {}'.format(gen, pret[gen]))


def handle_ordonare_pret(vanzari, undo_list, redo_list):
    rezultat = ord_price(vanzari, undo_list, redo_list)
    return rezultat

def handle_afisare_titlu_dupa_gen(lista):
    try:
        new_list = afisare_titluri_dupa_gen(lista)
        for gen in new_list:
            if new_list[gen] != 1:
                print("Genul {} are {} titluri".format(gen, new_list[gen]))
            else:
                print("Genul {} are un singur titlu".format(gen))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return lista


def handle_undo(vanzari, undo_list, redo_list):
    undo_result = do_undo_inefficient(undo_list, redo_list, vanzari)
    if undo_result is not None:
        return undo_result
    return vanzari


def handle_redo(vanzari, undo_list, redo_list):
    redo_result = do_redo_inefficient(undo_list, redo_list, vanzari)
    if redo_result is not None:
        return redo_result
    return vanzari

def handle_crud(vanzari, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii vanzari')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            vanzari = handle_add(vanzari, undo_list, redo_list)
        elif optiune == '2':
            vanzari = handle_update(vanzari, undo_list, redo_list)
        elif optiune == '3':
            vanzari = handle_delete(vanzari, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'd':
            handle_show_details(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return vanzari


def run_ui(vanzari, undo_list, redo_list):

    while True:
        try:
            handle_show_all(vanzari)
            show_menu()
            optiune = input('Optiunea aleasa: ')
            if optiune == '1':
                vanzari = handle_crud(vanzari, undo_list, redo_list)
            elif optiune == '2':
                vanzari = modificare_vanzare(vanzari, undo_list, redo_list)
            elif optiune == '3':
                vanzari = handle_change_gen(vanzari, undo_list, redo_list)
            elif optiune == '4':
                handle_pret_minim(vanzari)
            elif optiune == '6':
                handle_afisare_titlu_dupa_gen(vanzari)
            elif optiune == '5':
                vanzari = handle_ordonare_pret(vanzari, undo_list, redo_list)
            elif optiune == 'u':
                if len(undo_list) > 0:
                    vanzari = handle_undo(vanzari, undo_list, redo_list)
                else:
                    print('Nu se poate face undo.')
            elif optiune == 'r':
                if len(redo_list) > 0:
                    vanzari = handle_redo(vanzari, undo_list, redo_list)
                else:
                    print('Nu se poate face redo.')
            elif optiune == 'x':
                break
            else:
                print('Optiune invalida.')
        except Exception as ex:
            print('Eroare: ', ex)
