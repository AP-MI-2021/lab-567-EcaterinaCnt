from Logic.CRUD import create
from Tests.test_all import run_all_tests
from Tests.test_crud import test_crud
from UserInterface.command_line_console import main_line
from UserInterface.console import run_ui

def main():
    run_all_tests()
    #vanzari=[]
    #vanzari= create(vanzari, 1, 'Scufita Rosie','basm', 25.5, 'Silver')
    undo_list = []
    redo_list = []
    vanzari = []
    """vanzari = create(vanzari, 1, 'Spider-Man', 'Sci-Fi', 60, 'Silver', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Marvel: Adventures', 'Sci-Fi', 50, 'Gold', undo_list, redo_list)
    vanzari = create(vanzari, 3, 'Man in Black', 'Fiction', 25.50, 'None', undo_list, redo_list)
    vanzari = create(vanzari, 4, 'Return Home', 'Comic', 15.76, 'Silver', undo_list, redo_list)"""
    meniu = str(input('Scrieti ce tip de meniu doriti sa se afiseze: clasic sau comenzi: '))
    if meniu == "clasic":
        run_ui(vanzari, undo_list, redo_list)
    elif meniu == "comenzi":
        main_line(vanzari, undo_list, redo_list)


if __name__=='__main__':
    main()
