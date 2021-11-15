from Domain.Librarie import vanzare_obiect, get_id, get_titlu, get_gen, get_pret, get_tip_reducere

def inverse_create(lst_vanzari, id_carte):
    new_vanzari = []
    for carte in lst_vanzari:
        if get_id(carte) != id_carte:
            new_vanzari.append(carte)
    return new_vanzari


def get_by_id(id, lista):
    '''
    ia vanzarea cu id-ul dat dintr-o lista
    :param id: id-ul vanzarii - string
    :param lista: lista de vanzari
    :return: vanzarea cu id-ul dat sau None daca nu exista in lista
    '''
    for vanzare in lista:
        if get_id(vanzare) == id:
            return vanzare
    return None


def create(lst_vanzari, id_vanzare: int, titlu, gen, pret, tip_reducere, undo_list: list, redo_list: list):
    '''
   Creeaza o vanzare
   :param lst_vanzari:lista de vanzari
   :param id_vanzare: id-ul vanzarii
   :param titlu: titlul cartii din vanzare
   :param gen: genul cartii din vanzare
   :param pret: pretul vanzarii
   :param tip_reducere: tipul de reducere
   :param undo_list: lista de sters
   :param redo_list: lista de adaugat
   :return: returneaza o vanzare cu un id unic si detaliile ei
    '''
    new_list=['None', 'Gold', 'Silver']
    if tip_reducere not in new_list:
        raise TypeError('Tip reducere necunoscut.')
    if get_by_id(id_vanzare, lst_vanzari) is not None:
        raise ValueError(f'Exista deja o vanzare cu acest id {id_vanzare}.')

    vanzare_obiecte = vanzare_obiect(id_vanzare, titlu, gen, pret, tip_reducere)
       #lst_vanzari.append(vanzare_obiecte)
    undo_list.append(lst_vanzari)
    redo_list.clear()
        #return [id_vanzare, titlu, gen, pret, tip_reducere]
    return lst_vanzari + [vanzare_obiecte]



def read(lst_vanzari, id_carte: int=None):
    """
    Citeste o vanzare din "baza de date".
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii.
    :return: cartea cu id-ul id_carte sau lista cu toate vanzarile, daca id_carte=None
    """
    cartea_cu_id = None
    for cartea in lst_vanzari:
        if get_id(cartea) == id_carte:
            cartea_cu_id = cartea

    if cartea_cu_id:
        return cartea_cu_id
    return None


def update(lst_vanzari, new_vanzare, undo_list: list, redo_list: list):
    """
    Actualizeaza o vanzare.
    :param lst_vanzari: lista de vaznari
    :param new_vanzare: vanzarea care se va actualiza - id-ul trebuie sa fie unul existent.
    :param undo_list: lista cu vanzarea care tebuie stearsa
    :param redo_list: lista cu vanzarea care trebuie adaugata
    :return: o lista cu vanzari actualizata
    """

    if read(lst_vanzari, get_id(new_vanzare)) is None:
        raise ValueError(f'Nu xista o vanzare cu id-ul {get_id(new_vanzare)} pe care sa o actualizam.')

    # lst_carti=[c1:(1,Mobidic), c2:(2,Hansel si Gretel)], cartea=(2, Scufita Rosie)
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(vanzare)
        else:
            new_vanzari.append(new_vanzare)
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari


def delete(lst_vanzare, id_carte: int, undo_list: list, redo_list: list):
    """
    :param lst_vanzare: lista de vanzari
    :param id_carte: id-ul cartii din vanzare
    :param undo_list: lista cu vanzarea care trebuie stearsa
    :param redo_list: lista cu vanzarea care trebuie adaugata
    :return: o lista de vanzari fara cartea cu id-ul id_carte.
    """
    if read(lst_vanzare, id_carte) is None:
        raise ValueError(f'Nu xista o carte cu id-ul {id_carte} pe care sa o stergem.')

    new_vanzari = []
    for carte in lst_vanzare:
        if get_id(carte) != id_carte:
            new_vanzari.append(carte)
    undo_list.append(lst_vanzare)
    redo_list.clear()
    return new_vanzari


