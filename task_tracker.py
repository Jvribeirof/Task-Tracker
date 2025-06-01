import sys
import os
from pathlib import Path
import json
from datetime import date
from time import time

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(sys.argv) > 2:
        raise IndexError('Pleas, select just one action')
    
    action = sys.argv[1]
    if action not in(features.keys()):
        raise ValueError('Please, select a action: [add,update,del,list]')
    else:
        json_file, JSON_PATH = check_json_file()
        features[action](json_file,JSON_PATH)

def check_json_file():
    MAIN_PATH = Path(__file__).parent
    JSON_PATH = MAIN_PATH / 'tasks.json'
    if not JSON_PATH.exists():
        with open(JSON_PATH, 'w') as file:
            file.write('[]')
    with open(JSON_PATH,'r',encoding='utf-8') as file:
        try:
            json_file = json.load(file)
        except:
            json_file = None
    return json_file,JSON_PATH

def list_task(tasks:list,path:Path):
    query = input('select [all, todo, in-progress,done,]: ')
    if not tasks:
        print("There's no taks saved...")
    else:
        for task in tasks:
            print(task)

def add_task(tasks:list,path:Path):
    descript = input('Description: ')
    id_task = str(int(time()))
    current_date = date.today()
    new_task = {
        'id':id_task,
        'description':descript,
        'createdAt': str(current_date),
        'updatedAt': str(current_date)
    }
    tasks.append(new_task)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii= False, indent=4)
    
def del_task(tasks:list,path:Path):
    descript = input('Select wich one you want to be deleted [Description]: ')
    for i, task in enumerate(tasks):
        if task['description'] == descript:
            del tasks[i]
            break
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii= False, indent=4)

def updt_task(tasks:list,path:Path):
    descript = input('Select wich one you want to be update [Description]: ')
    new_dscrpt = input('Please, wright down the new description: ')
    current_date = date.today()
    for i, task in enumerate(tasks):
        if task['description'] == descript:
            tasks[i]['updatedAt'] = str(current_date)
            tasks[i]['description'] = new_dscrpt
            break
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii= False, indent=4)

if __name__ == '__main__':
    features = {
       'add':add_task,
       'update': updt_task,
       'del':del_task,
       'list': list_task 
    }
    main()