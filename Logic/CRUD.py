from Domain.Librarie import vanzare_obiect, get_id, get_titlu, get_gen, get_pret, get_tip_reducere
from Logic.List_id import list_id


def create(lst_vanzari, id_vanzare: int, titlu, gen, pret, tip_reducere):
    '''
   Creeaza o vanzare
   :param lst_vanzari:lista de vanzari
   :param id_vanzare: id-ul vanzarii
   :param titlu: titlul cartii din vanzare
   :param gen: genul cartii din vanzare
   :param pret: pretul vanzarii
   :param tip_reducere: tipul de reducere
   :return: returneaza o vanzare cu un id unic si detaliile ei
    '''
    new_list=['None', 'Gold', 'Silver']
    if id_vanzare in list_id(lst_vanzari):
        raise ValueError(f'Exista deja o carte cu id-ul {id_vanzare}')
    if tip_reducere not in new_list:
        raise TypeError('Tip reducere necunoscut.')
    else:
        vanzare_obiecte = vanzare_obiect(id_vanzare, titlu, gen, pret, tip_reducere)
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
    return None


def update(lst_vanzari, new_vanzare):
    """
    Actualizeaza o vanzare.
    :param lst_vanzari: lista de vaznari.
    :param new_vanzare: vanzarea care se va actualiza - id-ul trebuie sa fie unul existent.
    :return: o lista cu vanzari actualizata.
    """

    if read(lst_vanzari, get_id(new_vanzare)) is None:
        raise ValueError(f'Nu xista o vanzare cu id-ul {get_id(new_vanzare)} pe care sa o actualizam.')

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
    if read(lst_vanzare, id_carte) is None:
        raise ValueError(f'Nu xista o carte cu id-ul {id_carte} pe care sa o stergem.')

    new_vanzari = []
    for carte in lst_vanzare:
        if get_id(carte) != id_carte:
            new_vanzari.append(carte)

    return new_vanzari


