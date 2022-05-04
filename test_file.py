from my_utils import get_file_names

files = get_file_names()
for file in files:
    if file.endswith(".py"):
        python_file_found = True
        break
else:
    python_file_found = False
