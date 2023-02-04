import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
import indoor3d_util

anno_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta\\anno_paths.txt'))]
anno_paths = [os.path.join(indoor3d_util.DATA_PATH, p) for p in anno_paths]

if not os.path.exists(BASE_DIR+"\\data"):
    os.makedirs(BASE_DIR+"\\data")
if not os.path.exists(BASE_DIR+"\\data\\npy"):
    os.makedirs(BASE_DIR+"\\data\\npy")

output_folder = os.path.join(BASE_DIR, 'data') 
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Note: there is an extra character in the v1.2 data in Area_5/hallway_6. It's fixed manually.
for anno_path in anno_paths:
    print(anno_path)
    
    elements = anno_path.split('/')
    out_filename = 'npy/'+ elements[-1]+'.npy' # Area_1_hallway_1.npy
    indoor3d_util.collect_point_label(anno_path, os.path.join(output_folder, out_filename), 'numpy')
    #indoor3d_util.collect_point_label(anno_path, out_filename, 'numpy')
    
