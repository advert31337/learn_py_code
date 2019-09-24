import os

path = os.getcwd()
folders = [
    ['input', []], 
    ['output', []], 
    ['temp', []], 
    ['media', [
        ['images', []], 
        ['video', []]]]
]

def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
        
def build(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            create_folder(path)
            if len(d[1])>0:
                build(path, d[1])
            
        
projectname = input('Введите имя прокта: ')
if projectname:
    full_path = os.path.join(path, projectname)
    create_folder(full_path)
    build(full_path, folders)