import numpy as np
import os

with open('starList.dat') as f:
    star = f.read().splitlines()

for s in star:

    os.system('cp /home/auddoula/BeWork/{}/{}_input.text input_info/'.format(s,s))


os.system('cp /home/auddoula/BeWork/bd-13_4933/bd-134933_input.text input_info/')
# because the naming of the files in not consistant, cannot batch it for this star.
