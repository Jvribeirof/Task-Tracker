import sys
import os
from pathlib import Path
def main():
    check_json_file()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(sys.argv) > 2:
        raise IndexError('Pleas, select just one action')
    
    action = sys.argv[1]
    if action not in(features.keys()):
        raise ValueError('Please, select a action: [add,update,del,list]')
    else:
        print(features[action])

def check_json_file():
    MAIN_PATH = Path(__file__).parent
    JSON_PATH = MAIN_PATH / 'tasks.json'
    if not JSON_PATH.exists():
        with open(JSON_PATH, 'w'):
            pass

if __name__ == '__main__':
    features = {
       'add':"FUNC ADD TASK",
       'update': "FUNC UPDATE TASK",
       'del':"FUNC DELETE TASK",
       'list':"FUNC LIST TASKS" 
    }
    main()