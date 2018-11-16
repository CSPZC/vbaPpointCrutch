import os
import sys 

if len(sys.argv)==2:
    print('no params')
    sys.exit(1)

dir = sys.argv[1]
mask= sys.argv[2]

files = os.listdir(dir); 

res = filter(lambda x: x.endswith(mask), files);

print res