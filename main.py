# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import shutil
import os


class FileManager:
    def __init__(self):
        self.__current_absolute_path = os.path.abspath("./")

    def print_content_folder(self):
        print(*os.listdir(self.__current_absolute_path))

    def print_content_folder(self, folder_path=None, separator=None):
        print(*os.listdir(folder_path), sep=separator)

    def back_way(self):
        self.__current_absolute_path = self.__current_absolute_path[0:self.__current_absolute_path.rfind('\\')]

    def creater_folder(self, folder_name):
        trable_words = tuple('=' '+' '-' '%' '&' '//' ':' '/')

        for word in trable_words:
            if word in folder_name:
                folder_name = folder_name.replace(word, '')
        if os.path.exists(folder_name):
            print("Папка уже существует")
        else:
            os.mkdir(self.__current_absolute_path + '\\' + folder_name)

    def file_creator(self, file_name):
        if os.path.exists(file_name):
            print("Файл уже существует")
        else:
            open(self.__current_absolute_path + '\\' + file_name, 'w')

    def folder_rm(self, folder_name):
        if os.path.exists(folder_name):
            os.remove(self.__current_absolute_path + '\\' + folder_name)
        else:
            print("Папки не существует")

    def file_rm(self, file_name):
        if os.path.exists(file_name):
            os.remove(self.__current_absolute_path + '\\' + file_name)
        else:
            print("Файл не существует")

    def rename_file(self, file_name, new_name_of_file):
        if os.path.exists(file_name):
            os.rename(self.__current_absolute_path + '\\' + file_name,
                      self.__current_absolute_path + '\\' + new_name_of_file)
        else:
            print("Файл не существует")

    def rename_folder(self, folder_name, new_name_of_folder):
        if os.path.exists(folder_name):
            os.rename(self.__current_absolute_path + '\\' + folder_name,
                      self.__current_absolute_path + '\\' + new_name_of_folder)
        else:
            print("Папка не существует")

    def moving_folder(self, folder_name, new_place_of_folder):
        if os.path.exists(folder_name):
            shutil.move(os.path.exists(folder_name), new_place_of_folder)
        else:
            print("Папка не существует")

    def moving_file(self, file_name, new_place_of_file):
        if os.path.exists(file_name):
            shutil.move(os.path.exists(file_name), new_place_of_file)
        else:
            print("Папка не существует")

    def size_file(self, file_name):
        if os.path.exists(file_name):
            file_size = os.path.getsize(file_name)
            print('Размер файла:', file_size, 'байт')
        else:
            print("Файл не существует")

    def find_in_folder(self, file_name):
        for root, dirs, files in os.walk('D:/'):
            for file in files:
                if file_name in file:
                    return True
        return False

    def menu_manager(self):
        spisok = ['шаг назад',
                  'создание папки',
                  'создание файла',
                  'удаление папки',
                  'удаление файла',
                  'переименовывание файла',
                  'переименовывание папки',
                  'перемещение файла',
                  'премещение папки',
                  'размер файла', 'поиск файла по папкам', 'остановить программу']
        while True:
            for i in range(0, len(spisok)):
                print(f'{i + 1}. {spisok[i]}')
            selected_element = int(input())

            match selected_element:
                case 1:
                    self.print_content_folder()
                    self.back_way()
                    break
                case 2:
                    name_folder = input('введите название папки ')
                    self.creater_folder(name_folder)
                    break
                case 3:
                    name_file = input('введите название файла ')
                    self.file_creator(name_file)
                    break
                case 4:
                    name_folder = input('введите название папки ')
                    self.folder_rm(name_folder)
                    break
                case 5:
                    name_file = input('введите название папки ')
                    self.file_rm(name_file)
                    break
                case 6:
                    name_file = input('введите название папки ')
                    new_name_file = input('введите название папки ')
                    self.rename_file(name_file, new_name_file)
                    break
                case 7:
                    name_folder = input('введите название папки ')
                    new_name_folder = input('введите название папки ')
                    self.rename_folder(name_folder, new_name_folder)
                    break
                case 8:
                    name_file = input('введите название папки ')
                    new_place_file = input()
                    self.moving_file(name_file, new_place_file)
                    break
                case 9:
                    name_folder = input('введите название папки ')
                    new_place_folder = input()
                    self.moving_folder(name_folder, new_place_folder)
                    break
                case 10:
                    name_folder = input('введите название папки ')
                    self.size_file(name_folder)
                    break
                case 11:
                    name_file = input('введите название файла ')
                    c = self.find_in_folder(name_file)
                    if c == True:
                        print('файл есть')
                    else:
                        print('файла нету')
                    break
                case 12:
                    break


file_manager = FileManager()
file_manager.menu_manager()