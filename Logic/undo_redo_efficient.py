'''def do_undo_efficient(undo_list: list, redo_list: list, current_list: list):
    """
    Stergerea unei vanzari
    :param undo_list: lista cu vanzarea care trebuie stearsa
    :param redo_list: lista cu vanzaea care a fost stearsa
    :return: sterge lista cu vanzarea ceruta
    """
    if undo_list:
        top_undo = undo_list.pop() # top_undo[0] = f_lambda
        redo_list.append(top_undo)
        return top_undo[0](current_list) # return f_lambda()

    return None
'''

'''
def do_redo_efficient(undo_list: list, redo_list: list, current_list: list):
    """
    Adaugarea vanzarii sterse
    :param undo_list: lista cu vanzarea care a fost adaugata
    :param redo_list: lista cu vanzarea care a fost inainte stearsa
    :return: adauga lista cu vanzarea ceruta
    """
    if redo_list:
        top_redo = redo_list.pop() # top_undo[1] = f_lambda
        undo_list.append(top_redo)
        return top_redo[1](current_list) # return f_lambda()

    return None
'''''

def do_undo_inefficient(undo_list:list, redo_list:list, current_list):
    """
    Face un undo
    :param undo_list: Lista pentru undo
    :param redo_list: Lista pentru redo
    :return:
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()
    return current_list


def do_redo_inefficient(undo_list:list, redo_list:list, current_list):
    """
    Face un redo
    :param undo_list: Lista pentru undo
    :param redo_list: Lista pentru redo
    :return:
    """

    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    else:
        return current_list
