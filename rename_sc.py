import os

input_dir = "../all_bl_renamed"

for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith(".csv"):
            if "wordmerge" in file:
                os.rename(os.path.join(root, file),
                          os.path.join(root, file.replace("_wordmerged", "")))
