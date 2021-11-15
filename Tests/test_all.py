from Tests.test_crud import test_delete, test_update, test_read, test_create
#from Tests.test_undo_redo import testUndoRedo
from Tests.test_undo_redo import testUndoRedo
from Tests.tests_modificari import test_pret_minim, test_modificare_vanzare, test_aplicare_reducere_5, \
    test_aplicare_reducere_10, test_afisare_titluri_dupa_gen


def run_all_tests():
    test_create()
    test_read()
    test_update()
    test_delete()
    test_aplicare_reducere_10()
    test_aplicare_reducere_5()
    test_modificare_vanzare()
    test_afisare_titluri_dupa_gen()
    testUndoRedo()
    test_pret_minim()