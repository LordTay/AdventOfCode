import os
for i in range(1,32):
    path = "./Day%02d"%i
    if not os.path.exists(path):
        os.mkdir(path)
    file_path = path+"/solution.py"
    if not os.path.isfile(file_path):
        f = open(file_path,"w")
        f.write("#Solution of Day%d\n\n"% i)
        f.close()