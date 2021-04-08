'''
Author: Javier Fumanal Idocin
javierfumanalidocin at gmail dot com

Module comprising the save file comparison.
'''
import os
import time
import shutil
import datetime
import pathlib


NOT_FOUND_CODE = -1

def compare_file(path1, path2):
    '''
    returns the path of the most recent file.
    :param path1:
    :param path2:
    :return:
    '''

    def obtain_date(path):
        try:
            f = pathlib.Path(path)
            return datetime.datetime.fromtimestamp(f.stat().st_mtime)

        except FileNotFoundError:
            return NOT_FOUND_CODE

    date1 = obtain_date(path1)
    date2 = obtain_date(path2)

    if date1 == NOT_FOUND_CODE:
        return path2

    elif date2 == NOT_FOUND_CODE:
        return path1

    elif date1 < date2:
        return path2

    elif date2 < date1:
        return path1

def sync_folder(folder1, folder2):
    '''
    Both folder1 and folder2 end up with the same files. The most recent version
    in case of name collision.

    :param folder1:
    :param folder2:
    :return:
    '''

    def update_folder(folder1, folder2):
        for filename in os.listdir(folder1):
            path1 = os.path.join(folder1, filename)
            path2 = os.path.join(folder2, filename)

            newest_path = compare_file(path1, path2)

            if path1 != newest_path:
                shutil.copyfile(newest_path, path1)

            elif path2 != newest_path:
                shutil.copyfile(newest_path, path2)


    update_folder(folder1, folder2)
    update_folder(folder2, folder1)

def sync_games():
    import persistence

    profiles = persistence.load_games()

    for k, folders in profiles.items():
        sync_folder(folders[0], folders[1])

if __name__ == '__main__':
    sync_games()