import os
import time

ROOT_FOLDER = 'Numerator'

def print_title_and_instructions() -> None:
    'Prints the program title and instructions.'

    print(f'''{"-" * 32}
----- Numerador de páginas -----
{"-" * 32}
''')

    print('''- Coloque todas as pastas que deseja ter as páginas com os nomes formatados dentro da recém criada pasta "Numerator".
- Confirme que colocou as pastas com "OK".
''')

def create_root_folder() -> None:
    'Creates the root folder "Numerator".'

    os.makedirs(name=ROOT_FOLDER, exist_ok=True)

def check_folders_on_root() -> None:
    'Verify if the user have already placed the folders on "Numerator" by asking "OK".'

    while True:
        ok = input('OK: ').strip().upper()
        if ok != 'OK':
            print('Digite somente "OK".')
        else:
            print()
            break

def format_number(number:int, total:int) -> str:
    '''Format the number of the page to #, 0#, 00#, etc.

    Args:
        number (int): Number to be formated
        total (int): Total of files on the folder

    Returns:
        str: Formated number
    '''

    number_characters = len(str(number))
    total_characters = len(str(total))
    difference = total_characters - number_characters
    return f'{"0" * difference}{number}'

def get_files(files:str, folder_path:str) -> list[str]:
    '''_summary_

    Args:
        files (str): _description_
        folder_path (str): _description_

    Returns:
        list[str]: _description_
    '''

    return [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

def enumerate_files() -> None:
    'Enumerate the files.'

    for folder_path, subfolders, files in os.walk(ROOT_FOLDER):

        initial_files_list = get_files(files, folder_path)
        
        display_folder_path = folder_path.replace('\\', ' / ')
        
        print(f'Numerando páginas em: {display_folder_path}\n',)

        if len(files) == 0:
            print('-\n')
        else:
            try:
                for index, file_name in enumerate(initial_files_list, start=1):

                    temporary_name = f'XXX{file_name}'

                    old_file_path = os.path.join(folder_path, file_name)
                    temporary_file_path = os.path.join(folder_path, temporary_name)

                    os.rename(old_file_path, temporary_file_path)

                temporary_files_list = get_files(os.listdir(folder_path), folder_path)
                
                for index, file_name in enumerate(temporary_files_list, start=1):

                    new_name = f'{format_number(index, len(temporary_files_list))}{os.path.splitext(file_name)[1]}'

                    old_file_path = os.path.join(folder_path, file_name)
                    new_file_path = os.path.join(folder_path, new_name)

                    os.rename(old_file_path, new_file_path)

                    print('.', end='', flush=True)
                    time.sleep(0.01)
                
                print('\n')

            except Exception as e:
                print(f'Erro: {str(e)}\n')

def end_program() -> None:
    'Finish the program.'

    print('Arquivos renomeados!\n')
    input('Pressione ENTER para encerrar o programa...')
