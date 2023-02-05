import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(BASE_DIR+"/annotations"):
    os.makedirs(BASE_DIR+"/annotations")

for i in range(0,100):
    path = BASE_DIR+"/annotations/"+ str(i)
    print(path)
    os.mkdir(path)
