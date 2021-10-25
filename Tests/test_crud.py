from Domain.Librarie import vanzare_obiect, get_id, get_gen, get_pret, get_tip_reducere, get_titlu
from Logic.CRUD import create, read, update, delete


def get_data():
    return [
        vanzare_obiect(1, 'c1', 'titlu 1', 50.0, 'None'),
        vanzare_obiect(2, 'c2', 'titlu 2', 80.30, 'Gold'),
        vanzare_obiect(3, 'c3', 'titlu 3', 20, 'Silver'),
        vanzare_obiect(4, 'c4', 'titlu 4', 150, 'Gold'),
        vanzare_obiect(5, 'c5', 'titlu 5', 40, 'Gold'),
   ]


def test_create():
    vanzari = get_data()
    params = (10, 'titlu new', 'gen new', 20.32, 'None')
    p_new = vanzare_obiect(*params)
    new_vanzari = create(vanzari, *params)
    assert len(new_vanzari) == len(vanzari) + 1

    # found = False
    # for prajitura in new_prajituri:
    #     if prajitura == p_new:
    #         found = True
    assert p_new in new_vanzari


def test_read():
    vanzari = get_data()
    some_c = vanzari[2]
    assert read(vanzari, get_id(some_c)) == some_c
    assert read(vanzari, None) == vanzari


def test_update():
    vanzari = get_data()
    c_updated = vanzare_obiect(1, 'c1000', 'titlu 1', 50.0, 'None')
    updated = update(vanzari, c_updated)
    assert c_updated in updated
    assert c_updated not in vanzari
    assert len(updated) == len(vanzari)


def test_delete():
    vanzari = get_data()
    to_delete = 3
    c_deleted = read(vanzari, to_delete)
    deleted = delete(vanzari, to_delete)
    assert c_deleted not in deleted
    assert c_deleted in vanzari
    assert len(deleted) == len(vanzari) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()