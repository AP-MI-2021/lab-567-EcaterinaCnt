from Domain.Librarie import get_str_vanzare, get_titlu, get_gen, get_pret, get_tip_reducere, \
    vanzare, vanzare_obiect
from Logic.CRUD import create, read, update, delete
from Logic.modificari import modificare_vanzare


def show_menu():
    print('1. CRUD')
    print('2. Reducere pret pentru anumite vanzari.')
    print('x. Exit')


def handle_add(vanzari):
    id_vanzare = int(input('Dati id-ul vaznarii : '))
    titlu = input('Dati titlul cartii : ')
    gen = input('Dati genul cartii : ')
    pret = float(input('Dati pretul cartii : '))
    tip_reducere = input('Dati tipul reducerii vanzarii in functie de client: ')
    return create(vanzari, id_vanzare, titlu, gen, pret, tip_reducere)


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


def handle_update(vanzari):
    id_vanzari = int(input('Dati id-ul vanzarii care se actualizeaza: '))
    titlu = input('Dati noul nume al cartii vandute: ')
    gen = input('Dati noul gen al cartii vandute: ')
    pret = float(input('Dati noul pret al cartii vandute: '))
    tip_reducere = input('Dati noul tip de reducere ce se poate face clientului: ')
    return update(vanzari, vanzare_obiect(id_vanzari, titlu, gen, pret, tip_reducere))


def handle_delete(vanzari):
    id_vanzare = int(input('Dati id-ul vanzarii care se va sterge: '))
    vanzari = delete(vanzari, id_vanzare)
    print('Stergerea a fost efectuata cu succes.')
    return vanzari


def handle_crud(vanzari):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii vanzari')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            vanzari = handle_add(vanzari)
        elif optiune == '2':
            vanzari = handle_update(vanzari)
        elif optiune == '3':
            vanzari = handle_delete(vanzari)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'd':
            handle_show_details(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return vanzari


def run_ui(vanzari):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            vanzari = handle_crud(vanzari)
        elif optiune == '2':
            vanzari = modificare_vanzare(vanzari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')
    return vanzari