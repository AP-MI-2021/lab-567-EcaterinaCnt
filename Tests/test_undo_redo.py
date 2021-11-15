from Domain.Librarie import vanzare_obiect, get_id
from Logic.CRUD import create, get_by_id
from Logic.undo_redo_efficient import do_undo_inefficient, do_redo_inefficient
from UserInterface.console import handle_undo, handle_redo


def testUndoRedo():
    undoList = []
    redoList = []
    lista = []
    #adaugam 3 obiecte
    lista = create(lista, 1, "Great Gatsby", "clasica", 15, "Gold", undoList, redoList)
    lista =create(lista, 2, "Tabloul", "mister", 20, "Silver", undoList, redoList)
    lista = create(lista, 3, "Crima si pedeapsa", "clasica", 30, "Silver", undoList, redoList)

    #undo 1
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 2
    assert get_by_id(3, lista) is None

    #undo 2
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    #assert len(lista) == 1
    assert get_by_id(2, lista) is None

    #undo 3
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert lista == []

    #undo 4 - nu face nimic
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert lista == []

    #adaugam alte 3 obiecte
    lista = create(lista,1, "Great Gatsby", "clasica", 15, "Gold",  undoList, redoList)
    lista = create(lista,2, "Tabloul", "mister", 20, "Silver",  undoList, redoList)
    lista = create(lista,3, "Crima si pedeapsa", "clasica", 30, "Silver", undoList, redoList)

    #redo - nu face nimic
    if len(redoList) > 0:
        lista = handle_redo(lista, undoList, redoList)
    assert len(lista) == 3
    assert get_id(get_by_id(1, lista)) == 1

    #undo 1
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 2
    assert get_by_id(3, lista) is None

    #undo 2
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert get_by_id(2, lista) is None

    #redo 1
    if len(redoList) > 0:
        lista = handle_redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert get_by_id(2, lista) is not None

    #redo 2
    if len(redoList) > 0:
        lista = handle_redo(lista, undoList, redoList)
    assert len(lista) == 3
    assert get_by_id(3, lista) is not None

    #undo 1
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 2
    assert get_by_id(3, lista) is None

    #undo 2 (14)
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert get_by_id(2, lista) is None

    #adaug obiectul 4
    lista = create(lista,4, "Dune", "SF", 60, "Gold", undoList, redoList)

    #redo - nu face nimic
    if len(redoList) > 0:
        lista = handle_redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert get_id(get_by_id(4, lista)) == 4

    #undo 1
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert get_by_id(4, lista) is None

    #undo 2
    if len(undoList) > 0:
        lista = handle_undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None

    #redo 1
    if len(redoList) > 0:
        lista = handle_redo(lista, undoList, redoList)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None

    #redo 2
    if len(redoList) > 0:
        lista = handle_redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert get_by_id(4, lista) is not None

    #redo - nu face nimic
    if len(redoList) > 0:
        lista = handle_redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert get_id(get_by_id(1, lista)) == 1
    assert get_id(get_by_id(4, lista)) == 4
