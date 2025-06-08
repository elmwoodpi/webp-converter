import sys
import configparser
import os
import time

from PIL import Image
from tkinter import filedialog as fd

config = configparser.ConfigParser()

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'config.ini')

config.read(filename)

file_type = config['Settings']['file_type']
delete_original_file = config['Settings']['delete_original_file']
kill_program_immediately = config['Settings']['kill_program_immediately']

def kill_program():
    if kill_program_immediately == "True":
        exit
    else:
        time.sleep(5)
        exit

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    parts = file_path.split('\\')
    import_filename = parts[-1]

    print('CONVERTING: ', import_filename)

    file_name = import_filename.split('.')
    selected_file_type = file_name[1]
    selected_file_type = "." + selected_file_type
    file_name = file_name[0]
    imi = Image.open(import_filename)

    print("SELECTED FILE TYPE: ", selected_file_type)

    if selected_file_type == file_type:
        print("File is already the same format.")
    elif file_type != None:
        export_filename = file_name + file_type
        imi.save(export_filename)
        if delete_original_file == "True":
            os.remove(file_path)
            print("FILE REMOVED")
        else:
            print("Original file retained.")
        print('IMAGE CONVERTED SUCCESFULLY')
        kill_program()
    else:
        print("No file type specified. Check the config file.")
        kill_program()
else:
    print('No file selected.')
    kill_program()
