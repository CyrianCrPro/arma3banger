import os
import shutil
from glob import glob
from pathlib import Path

list_folder = glob("./mods/*")
print("renaming folders")
print(list_folder)
for folder_name in list_folder:
    renamed_folder = folder_name.replace("@","").lower()
    shutil.move(src=folder_name, dst=renamed_folder)

    # ensure Addons folder exist and rename it to lowercase
    addons_folder_path = Path(renamed_folder)/"Addons"
    if addons_folder_path.is_dir():

        shutil.move(src=addons_folder_path, dst=str(addons_folder_path).replace("Addons", "addons"))

print("Done")