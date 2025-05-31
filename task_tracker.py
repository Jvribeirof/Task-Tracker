import sys
def main():
    action = sys.argv[1]
    if action not in features.keys():
        print('Please, select a action: [add,update,del,list]')
    print(features[action])

if __name__ == '__main__':
    features = {
       'add':"FUNC ADD TASK",
       'update': "FUNC UPDATE TASK",
       'del':"FUNC DELETE TASK",
       'list':"FUNC LIST TASKS" 
    }
    main()