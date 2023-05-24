from ftplib import FTP
import os
import zipfile
from tqdm import tqdm


def extract_zip_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                zip_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(root)
                os.remove(zip_path)


def search_files_with_query(directory, query):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                file_contents = file.read()
                if query in file_contents:
                    print(f"Найден файл: {file_path}")
                    print("Содержимое файла:")
                    print(file_contents)


def download_files(ftp, handled_files):
    file_list = ftp.nlst()
    with tqdm(total=len(file_list), desc="Загрузка файлов", unit="файл") as pbar:
        for filename in filter(lambda file_name: not (file_name in handled_files), file_list):
            if filename.endswith(".zip"):
                local_filename = os.path.join(local_path, filename)
                with open(local_filename, 'wb') as file:
                    try:
                        ftp.retrbinary('RETR ' + filename, file.write)
                        handled_files.append(filename)
                    except BrokenPipeError:
                        return False
                    except:
                        pass
            pbar.update(1)

    ftp.quit()

    return True


def create_ftp(ftp_host, ftp_user, ftp_passwd, ftp_folder):
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_passwd)
    ftp.cwd(ftp_folder)
    return ftp


def download_and_search_ftp_files(ftp_host, ftp_user, ftp_passwd, ftp_folder, local_path, query):
    handled_files = []



    ended = False


    while not(ended):
        ftp = create_ftp(ftp_host, ftp_user, ftp_passwd, ftp_folder)
        ended = download_files(ftp, handled_files)

    extract_zip_files(local_path)
    search_files_with_query(local_path, query)


if __name__ == '__main__':
    # Параметры подключения к FTP-серверу
    ftp_host = 'ftp.zakupki.gov.ru'
    ftp_user = 'free'
    ftp_passwd = 'free'

    # Параметры скачивания и поиска
    ftp_folder = '/fcs_regions/Sverdlovskaja_obl/contracts/currMonth'  # Путь к папке на FTP-сервере, где будут файлы
    local_path = input("Введите путь к папке для сохранения файлов: ")  # Путь для сохранения и распаковки файлов

    # Получаем значение для поиска от пользователя
    query = input("Введите значение для поиска: ")

    # Загружаем и ищем файлы на FTP-сервере
    download_and_search_ftp_files(ftp_host, ftp_user, ftp_passwd, ftp_folder, local_path, query)
