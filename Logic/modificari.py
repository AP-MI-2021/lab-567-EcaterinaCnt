from Domain.Librarie import get_tip_reducere, get_id, get_titlu, get_gen, get_pret, vanzare_obiect
from Logic.CRUD import update


def aplicare_reducere_5(pret):
    '''
    Aplica o reducere pentru clientul de tip Silver
    :param pret: pretul initial al vanzarii
    :return: pretul nou dupa reducerea aplicata
    '''
    reduceri=5*pret/100
    return pret- reduceri


def aplicare_reducere_10(pret):
    '''
    Aplica o reducere pentru clientul de tip Gold
    :param pret:pretul initial al vanzarii
    :return:pretul nou dupa reducerea aplicata
    '''
    reduceri=10*pret/100
    return pret-reduceri


def change_gen(vanzari, titlu, gen, undo_list:list, redo_list:list):
    '''
    Schimbam genul unei carti cu titlul dat.
    :param vanzari: vanzarea care ne intereseaza
    :param titlu: titlul cartii dat
    :param gen: genul pe care vrem sa il aiba cartea
    :return: Returneaza cartea cu un nou gen
    '''
    for vanzare in vanzari:
        nume =get_titlu(vanzare)
        if nume==titlu:
            id= get_id(vanzare)
            pret=get_pret(vanzare)
            reducere=get_tip_reducere(vanzare)
            vanzari =update(vanzari, vanzare_obiect(id, get_titlu(vanzare), gen, pret, reducere), undo_list,redo_list)
        else:
            raise ValueError('Nu exista titlul introdus in cartile din vanzari')
    undo_list.append(vanzari)
    redo_list.clear()
    return vanzari


def ord_price(vanzari, undo_list, redo_list):
    '''
    Ordoneaza vanzarile in functie de pret
    :param vanzari: vanzarea care ne intereseaza
    :return: returneaza lista cu vanzaril in ordinea preturilor
    '''
    undo_list.append(vanzari)
    redo_list.clear()
    return sorted(vanzari, key=get_pret)


def modificare_vanzare(lst_vanzari, undo_list, redo_list):
    '''
    Modifica vanzarea initiala
    :param lst_vanzari: vanzarea introdusa
    :param undo_list: lista cu vanzarea care trebuie stearsa
    :param redo_list: lista cu vanzarea care trebuie adaugata
    :return:modifica pretul vanzarii in functie de tipul de abonament pe care il are clientul
    '''
    for vanzare in lst_vanzari:
        reducere=get_tip_reducere(vanzare)
        id_vanzare=get_id(vanzare)
        titlu=get_titlu(vanzare)
        gen=get_gen(vanzare)
        pret=get_pret(vanzare)
        if reducere == 'Silver':
            lst_vanzari=update(lst_vanzari, vanzare_obiect(id_vanzare, titlu, gen, aplicare_reducere_5(pret), 'None'), undo_list, redo_list)
        elif reducere == 'Gold':
            lst_vanzari = update(lst_vanzari,vanzare_obiect(id_vanzare, titlu, gen, aplicare_reducere_10(pret), 'None'), undo_list, redo_list)
        #else:
            #raise TypeError('Reducerea este introdusa incorect.')
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return lst_vanzari


def pret_minim(vanzari):
    '''
    Determina pretul minim
    :param vanzari: vanzarea introdusa
    :return:returneaza pretul minim
    '''
    pret = {}
    for vanzare in vanzari:
        gen = get_gen(vanzare)
        if gen in pret:
            if get_pret(vanzare) < pret[gen]:
                pret[gen] = get_pret(vanzare)
        else:
            pret[gen] = get_pret(vanzare)
    return pret


def afisare_titluri_dupa_gen(vanzari):
    '''
    Afiseaza numarul de titluri distincte pentru fiecare gen
    :param lista: o lista de vanzari
    :return: numarul de titluri distincte pentru fiecare gen
    '''
    rezultat = {}
    titluri =[]
    for vanzare in vanzari:
        gen = get_gen(vanzare)
        titlu = get_titlu(vanzare)
        if gen in rezultat:
            if titlu not in titluri:
                titluri.append(titlu)
                rezultat[gen] += 1
        else:
            rezultat[gen] = 1
            titluri.append(titlu)
    return rezultat
