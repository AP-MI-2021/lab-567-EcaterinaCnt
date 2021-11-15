

def vanzare_obiect(id_vanzare, titlu, gen, pret, tip_reducere_client: str):
    '''
    Gestioneaza o vanzare
    :param id_vanzare:id-ul vanzarii
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param tip_reducere_client:
    :return: vanzarea
    '''
    if id_vanzare == '' or titlu == '' or gen == '' :
        raise ValueError('Id_vanzare, titlu, gen trebuie sa fie nenule.')
    if pret is not None and not isinstance(pret, (float, int)):
        raise ValueError('Pretul trebuie sa fie un numar.')
    elif pret is None:
        price = 0
    elif pret < 0:
        raise ValueError('Pretul nu poate fi negativ.')
    #if tip_reducere_client != 'Silver' or tip_reducere_client!= 'Gold':
        #raise ValueError('Tipul de reducere poate fi doar Silver sau Gold. ')
    return (id_vanzare, titlu, gen, pret, tip_reducere_client)


def get_id(carte):
    '''
    Getter pentru id-ul vanzarii
    :param carte: vanzarea
    :return: id-ul vanzarii
    '''
    return carte[0]


def get_titlu(carte):
    """
    Titlul cartii din vanzare.
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
    return f'Vanzare cartea cu id-ul {get_id(carte)}, din genul {get_gen(carte)}, titlul {get_titlu(carte)},' \
           f' pretul {get_pret(carte)}, cu reducerea {get_tip_reducere(carte)}.'
