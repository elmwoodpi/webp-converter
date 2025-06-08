# webp-converter
Lightweight Python application to instantly convert .webp files to .png for editing programs like Davinci Resolve.

While the process of converting a .webp to a .png (or any other file for that matter) is relatively simple, it is a process that is annoyingly repetitive. 
This program allows you to drag the .webp into the .bat file, and will create a .png in the same location.

## Conversion
The conversion process is entirely automatic and requires no user interfacing. Simply drag and drop your file of choice (it does not *have* to be .webp. It also works with .jpg as well) onto the **webp-convert.bat** file, and the image will be replaced in its original directory with the format of choice.

## Installation
It is reccomended to install and use Python 3.13, however recent older versions should still be suitable.

## Configuration
The config.ini file allows the user to change two parameters: the type of file to convert *to* and whether or not the original file should be deleted or retained. 

In a clean version of webp-converter, it will automatically delete the original file and convert to .png. These settings may be changed in the config.ini file.

IMPORTANT: Currently, the application does not treat the delete_original_file variable as a boolean. This means that in order for it to delete the original file upon conversion, it MUST be written as "True"

The same issue applies to kill_program_immediately.

## Known Issues and problems

As of v.0.0.1 (6/7/25 build), the program itself, while lightweight, lacks sufficient testing. This means that it is not gurantueed to work with, or convert to all image formats. For example, you could convert a .png to a .ogg, and it will likely succesfully complete the operation. These shortfalls will be addressed in future builds, as this program was designed with the original intention of simply converting .webp to .png for video editing purposes.

## Changelogs
N/A