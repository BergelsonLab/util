import sys
import os
import shutil

def walk_tree(start, out):
    for root, dirs, files in os.walk(start):
        for file in files:
            if file.endswith(".eaf"):
                dir = os.path.basename(root)
                new_name = dir[:5]+"_PB_"+file[3:]
                shutil.copy(os.path.join(root, file),
                            os.path.join(out, new_name))

if __name__ == "__main__":

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    walk_tree(input_dir, output_dir)
