import sys
from pathlib import Path
from PIL import Image

# grab first and second argument

image_dir = sys.argv[1]

output_dir = sys.argv[2]

# check is folder exist, if not create it

save_path = Path.cwd()/output_dir

try:
    save_path.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    print("Folder is already there")
else:
    print("Folder was created")

# loop trougt Pokedax 
for file in Path(f'./{image_dir}').glob("*"):
    with Image.open(file) as img:
        opened_file = img.filename.split("/")[-1]
        new_file = opened_file.split(".")[0]
        # # convert images to PNG
        # save files to new folder
        img.save(f'{save_path}/{new_file}.png', "png")

