# import os
# from os import listdir
# from os.path import isfile, join

# def list_directory(path='.'):
#     """
#     Print all files and directories at the given path.
#     Default: current directory.
#     """
#     try:
#         entries = listdir(path)         # os.listdir() lists all entries :contentReference[oaicite:1]{index=1}
#     except FileNotFoundError:
#         print(f"Error: The directory '{path}' does not exist.")
#         return
#     except PermissionError:
#         print(f"Error: Permission denied to access '{path}'.")
#         return

#     print(f"Contents of '{path}':")
#     for name in entries:
#         full = join(path, name)
#         if isfile(full):
#             print(f"  [File]     {name}")
#         else:
#             print(f"  [Directory] {name}")

# if __name__ == "__main__":
#     # Change '.' to any directory path you want to inspect
#     list_directory('./codding')


# # method 2
import os #we first take import the os

directory_path='/'#store a directory path in a variable

contents=os.listdir(directory_path)#to list the directory we store it cintents variable

print(contents)#printing