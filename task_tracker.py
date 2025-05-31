import sys
import os
from pathlib import Path
import json

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(sys.argv) > 2:
        raise IndexError('Pleas, select just one action')
    
    action = sys.argv[1]
    if action not in(features.keys()):
        raise ValueError('Please, select a action: [add,update,del,list]')
    else:
        json_file = check_json_file()
        features[action](json_file)

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
    return json_file

def list_task(path):
    query = input('select [all, todo, in-progress,done,]: ')
    if not path:
        print("There's no taks saved...")
    else:
        for task in path:
            print(task)

if __name__ == '__main__':
    features = {
       'add':"FUNC ADD TASK",
       'update': "FUNC UPDATE TASK",
       'del':"FUNC DELETE TASK",
       'list': list_task 
    }
    main()