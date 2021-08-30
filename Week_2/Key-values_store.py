import argparse, json, os

#Add key-value in dictionary
def add_to_dictionary(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]

#Fix file if it empty
def fix_file(storage_path):
    with open (storage_path , 'w') as storage:
        storage.write('{}')

parser = argparse.ArgumentParser()

#Create arguments
parser.add_argument("--key")
parser.add_argument("--val")

args = parser.parse_args()

#Get path to file 
storage_path = os.path.join('D:\Coding\Python\Coursera_Diving_Into_Python\Week_2\storage.data')

if(os.path.isfile(storage_path)):
    with open(storage_path, 'r') as storage:
        #Check file
        if storage.read() != '':
            storage.seek(0)
        else:
            fix_file(storage_path)

        #Load data to dictionary
        key_value_dictionary = json.load(storage)
        #print(key_value_dictionary)
    
    #Add key-value
    if (args.key and args.val):
        with open(storage_path, 'w') as storage:
            add_to_dictionary(key_value_dictionary, args.key, args.val)
            json.dump(key_value_dictionary, storage)#Save file
    
    #Output
    elif (args.key and not args.val):
        for value in key_value_dictionary[args.key]:
            if value != key_value_dictionary[args.key][-1]:
                print(value + ',', end =" ")
            else:
                print(value)
else:
    with open(storage_path, 'w') as storage: #If no file
        json.dump({}, storage)               #Create file with empty dictionary