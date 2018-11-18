import os


def list_files(path, suffix='', recursive=True):
    files_list = []
    if os.path.exists(path):
        if recursive:
            for root, dirs, files in os.walk(path):
                for name in files:
                    if name.endswith(suffix) or name.endswith(suffix):
                        file_path = os.path.join(root, name)
                        files_list.append(file_path)
        else:
            lists = os.listdir(path)
            for line in lists:
                file_path = os.path.join(path, line)
                if not os.path.isdir(file_path) & (line.endswith(suffix) or line.endswith(suffix)):
                    files_list.append(file_path)

    return files_list


def add_pre_suffix(path, extension='', prefix='', suffix='', recursive=True):
    files_list = list_files(path, extension, recursive)
    for file in files_list:
        head, tail = os.path.split(file)
        file_name = os.path.splitext(tail)[0]
        ext = os.path.splitext(tail)[1]
        file_name = prefix + file_name + suffix + ext
        new_file_path = os.path.join(head, file_name)
        os.rename(file, new_file_path)


add_pre_suffix(r'E:\Projects\data\test', prefix='head_', suffix='_tail')