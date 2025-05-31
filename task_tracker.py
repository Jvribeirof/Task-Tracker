import sys
import os
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(sys.argv) > 2:
        raise IndexError('Pleas, select just one action')
    action = sys.argv[1]
    if action not in(features.keys()):
        raise ValueError('Please, select a action: [add,update,del,list]')
    else:
        print(features[action])

if __name__ == '__main__':
    features = {
       'add':"FUNC ADD TASK",
       'update': "FUNC UPDATE TASK",
       'del':"FUNC DELETE TASK",
       'list':"FUNC LIST TASKS" 
    }
    main()