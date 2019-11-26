#from common import splitfn
import os


def splitfn(file_path):

    file_path_parts = file_path.split(sep=os.sep)
    _path = os.path.join(*file_path_parts[:-1])
    file_name = file_path_parts[-1]
    file_name_parts = file_name.split(sep='.')
    return _path, file_name_parts[0], file_name_parts[1]