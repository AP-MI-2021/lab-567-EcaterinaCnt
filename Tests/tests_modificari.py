from Domain.Librarie import get_id, get_pret, get_tip_reducere, vanzare_obiect
from Logic.modificari import aplicare_reducere_10, aplicare_reducere_5, modificare_vanzare


def test_aplicare_reducere_10(pret):
    assert aplicare_reducere_10(100)==90
    assert aplicare_reducere_10(20)==18
    assert aplicare_reducere_10(35)==31.5

def test_aplicare_reducere_5(pret):
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
    list=modificare_vanzare(vanzari)
    assert len(vanzari)==len(list)
    for vanzare in list:
        assert get_tip_reducere(vanzare)=='None'
    index=0
    while index<len(vanzari):
        if get_tip_reducere(vanzari[index]) is not 'None':
            assert get_pret(list[index]) != get_pret(vanzari[index])
        index=index+1


