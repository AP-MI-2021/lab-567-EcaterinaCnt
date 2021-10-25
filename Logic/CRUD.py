from Domain.Librarie import vanzare_obiect, get_id, get_titlu, get_gen, get_pret, get_tip_reducere


def create(lst_vanzari, id_carte: int, titlu, gen, pret, tip_reducere):
    '''
    TODO
   :param lst_vanzari:lista de vanzari
   :param id_carte:
   :param titlu: 
   :param gen: 
   :param pret: 
   :param tip_reducere: 
   :return: 
    '''
    vanzare_obiecte = vanzare_obiect(id_carte, titlu, gen, pret, tip_reducere)
    #lst_vanzari.append(vanzare_obiecte)
    return lst_vanzari + [vanzare_obiecte]


def read(lst_vanzari, id_carte: int=None):
    """
    Citeste o vanzare din "baza de date".
    :param lst_vanzari: lista de vanzari
    :param id_carte: id-ul cartii vandute.
    :return: cartea cu id-ul id_carte sau lista cu toate vanzarile, daca id_carte=None
    """
    cartea_cu_id = None
    for cartea in lst_vanzari:
        if get_id(cartea) == id_carte:
            cartea_cu_id = cartea

    if cartea_cu_id:
        return cartea_cu_id
    return lst_vanzari


def update(lst_vanzari, new_vanzare):
    """
    Actualizeaza o vanzare.
    :param lst_vanzari: lista de vaznari.
    :param new_vanzare: vanzarea care se va actualiza - id-ul trebuie sa fie unul existent.
    :return: o lista cu vanzari actualizata.
    """

    # lst_carti=[c1:(1,Mobidic), c2:(2,Hansel si Gretel)], cartea=(2, Scufita Rosie)
    new_vanzari = []
    for carte in lst_vanzari:
        if get_id(carte) != get_id(new_vanzare):
            new_vanzari.append(carte)
        else:
            new_vanzari.append(new_vanzare)
    return new_vanzari


def delete(lst_vanzare, id_carte: int):
    """
    :param lst_vanzare:
    :param id_carte:
    :return: o lista de vanzari fara cartea cu id-ul id_carte.
    """
    new_vanzari = []
    for carte in lst_vanzare:
        if get_id(carte) != id_carte:
            new_vanzari.append(carte)

    return new_vanzari

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

def modificare_vanzare(lst_vanzari):
    for vanzare in lst_vanzari:
        reducere=get_tip_reducere(vanzare)
        id_vanzare=get_id(vanzare)
        titlu=get_titlu(vanzare)
        gen=get_gen(vanzare)
        pret=get_pret(vanzare)
        if reducere == 'Silver':
            lst_vanzari=update(lst_vanzari, vanzare_obiect(id_vanzare, titlu, gen, aplicare_reducere_5(pret), 'None'))
        elif reducere == 'Gold':
            lst_vanzari=update(lst_vanzari,vanzare_obiect(id_vanzare, titlu, gen, aplicare_reducere_10(pret), 'None'))
    return lst_vanzari

