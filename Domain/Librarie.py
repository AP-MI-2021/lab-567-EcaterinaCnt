def vanzare(id_carte, titlu, gen, pret, tip_reducere_client):
    '''
    Gestioneaza vanzarea unui obiect din librarie, o carte
    :param id_carte:id_carte, trebuie sa fie unic.
    :param titlu:titlul cartii, nenul
    :param gen:genul cartii, nenul
    :param pret:pretul cartii
    :param tip_reducere_client:reducerea in functie de tipul clientului:none, silver, gold
    :return:o vanzare a unei carti
    '''

def vanzare_obiect(id_vanzare, titlu, gen, pret, tip_reducere_client: str ):
    return {'id_vanzare':id_vanzare,
        'titlu':titlu,
        'gen':gen,
        'pret':pret,
        'tip_reducere':tip_reducere_client,
    }

def get_id(vanzare):
    '''
    Getter pentru id-ul vanzarii
    :param vanzare: vanzarea
    :return: id-ul vanzarii
    '''
    return vanzare['id_vanzare']

def get_titlu(carte):
    """
    TODO
    :param carte:
    :return:
    """
    return carte['titlu']


def get_gen(carte):
    return carte['gen']


def get_pret(carte):
    return carte['pret']


def get_tip_reducere(carte):
    return carte['tip_reducere']


def get_str_vanzare(carte):
    return f'Vanzare cartea cu id-ul {get_id(carte)}, din genul {get_gen(carte)}, titlul {get_titlu(carte)}, pretul {get_pret(carte)}, cu reducerea {get_tip_reducere(carte)}.'