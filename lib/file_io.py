def write_file(file_name, file_content):
    pass
    with open(f'{file_name}.txt', 'w', encoding = 'utf-8') as file :
        file.write(file_content)

def append_file(file_name, append_content):
    pass
    with open(f'{file_name}.txt', 'a', encoding = 'utf-8') as file :
        file.write(append_content)

def read_file(file_name):
    pass
    with open(f'{file_name}.txt', 'r') as file :
        content = file.read()
    return content