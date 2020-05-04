import subprocess
import os
import sys
import mimetypes

if len(sys.argv) < 2:
    print('Usage [filepath]')
    sys.exit(1)

path_dir = '/home/kernel/Desktop/' + sys.argv[1]

file_list = os.listdir(path_dir)

cri = ('text/x-python', None)

for file_name in file_list:
    if mimetypes.guess_type(file_name) == cri:
        p = subprocess.Popen(["python3", file_name], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        p.wait()
