from Logic.CRUD import create
from Tests.test_crud import test_crud
from UserInterface.command_line_console import main_line
from UserInterface.console import run_ui

def main():
    vanzari=[]
    vanzari= create(vanzari, 1, 'Scufita Rosie','basm', 25.5, 'Silver')
    meniu = str(input('Scrieti ce tip de meniu doriti sa se afiseze: clasic sau comenzi: '))
    if meniu == "clasic":
        run_ui([])
    elif meniu == "comenzi":
        main_line([])


if __name__=='__main__':
    test_crud()
    main()
