from Domain.Librarie import get_id, get_pret, get_tip_reducere, vanzare_obiect
from Logic.CRUD import create
from Logic.modificari import aplicare_reducere_10, aplicare_reducere_5, modificare_vanzare, pret_minim, \
    afisare_titluri_dupa_gen


def test_aplicare_reducere_10():
    assert aplicare_reducere_10(100)==90
    assert aplicare_reducere_10(20)==18
    assert aplicare_reducere_10(35)==31.5

def test_aplicare_reducere_5():
    assert aplicare_reducere_5(100)==95
    assert aplicare_reducere_5(10)==9.5
    assert aplicare_reducere_5(20)==19

def get_data():
    return [vanzare_obiect(1, 'c1', 'g1', 10, 'None' ),
            vanzare_obiect(2, 'b2', 'g2', 100, 'Silver'),
            vanzare_obiect(3, 'b3', 'g3', 200, 'Gold'),
            vanzare_obiect(4, 'b4', 'g4', 25, 'Silver'),
            ]

def test_modificare_vanzare():
    vanzari= get_data()
    undo_list=[]
    redo_list=[]
    list=modificare_vanzare(vanzari, undo_list, redo_list)
    assert len(vanzari)==len(list)
    for vanzare in list:
        assert get_tip_reducere(vanzare) == 'None'
    index=0
    while index<len(vanzari):
        if get_tip_reducere(vanzari[index]) != 'None':
            assert get_pret(list[index]) != get_pret(vanzari[index])
        index=index+1


def test_pret_minim():
    vanzari=[]
    vanzari=create(vanzari, 1, 'c1', 'g1', 10, 'Silver', [],[])
    vanzari=create(vanzari, 2, 'c2', 'g2', 100, 'Silver',[],[])
    vanzari=create(vanzari, 3, 'c3', 'g2', 1000, 'Gold',[],[])
    pret=pret_minim(vanzari)
    assert len(pret)==2
    assert pret['g2']==100

def test_afisare_titluri_dupa_gen():
    lista = []
    lista = create(lista, 1, "Great Gatsby", "clasica", 15, "Gold", [], [])
    lista = create(lista, 2, "Tabloul", "mister", 20, "Silver",[],[])
    lista = create(lista, 3, "Crima si pedeapsa", "clasica", 30, "Silver", [], [])
    lista = create(lista, 4, "Crima si pedeapsa", "clasica", 30, "Gold", [], [])

    new_list= afisare_titluri_dupa_gen(lista)

    assert len(new_list) == 2
    assert new_list["clasica"] == 2
    assert new_list["mister"] == 1