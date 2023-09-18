import sys
import clipboard
import json

FILE_NAME = 'clipboard_data.json'

def save_data(filename, value):
    with open(filename,'w') as f:
        json.dump(value, f)

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(FILE_NAME)

    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(FILE_NAME, data)
        print('Data Saved!!')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard!')
        else:
            print('Key does not exist!')

    elif command == 'list':
        print(data)
    else:
        print('Unknown command!!')
else:
    print('Please pass exactly one command!!')
