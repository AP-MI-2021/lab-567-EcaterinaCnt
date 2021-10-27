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
    '''
    Gestioneaza o vanzare
    :param id_vanzare:id-ul vanzarii
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param tip_reducere_client:
    :return: vanzarea
    '''
    return (id_vanzare, titlu, gen, pret,tip_reducere_client)

def get_id(vanzare):
    '''
    Getter pentru id-ul vanzarii
    :param vanzare: vanzarea
    :return: id-ul vanzarii
    '''
    return vanzare[0]

def get_titlu(carte):
    """
    TODO
    :param carte:cartea vanduta
    :return:titlul cartii vandute
    """
    return carte[1]


def get_gen(carte):
    '''
    Genul cartii
    :param carte:cartea vanduta
    :return: genul cartii vandute
    '''
    return carte[2]


def get_pret(carte):
    '''
    Pretul cartii
    :param carte:cartea vanduta
    :return: pretul cartii vandute
    '''
    return carte[3]


def get_tip_reducere(carte):
    '''
    Reducerea in functie de tipul de client
    :param carte: cartea vanduta
    :return: reducerea tipului de client
    '''
    return carte[4]


def get_str_vanzare(carte):
    '''
    Vanzarea
    :param carte: obiectul vandut, cu specificatiile sale
    :return:genereaza o vanzare ce contine toate detaliile obiectului vandut
    '''
    return f'Vanzare cartea cu id-ul {get_id(carte)}, din genul {get_gen(carte)}, titlul {get_titlu(carte)}, pretul {get_pret(carte)}, cu reducerea {get_tip_reducere(carte)}.'