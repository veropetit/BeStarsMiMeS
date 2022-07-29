import os

with open('starList.dat') as f:
    star=f.read().splitlines()

for s in star[0:-1]:
# need to remove the entry for bd-134933
# because of a mismatch in naming.
# done manually below
    with open('input_info/{}_input.text'.format(s)) as f:
        obs=f.read().splitlines()
    out = open('input_info/{}_symlink.text'.format(s), "w")
    nobs = len(obs)
    for i,o in enumerate(obs):
        link=o.split()[2]
        test = os.popen('ls -l /home/auddoula/BeWork/{}/{}.s'.format(s,link)).read()
        out.write(test)
        os.system('cp -P /home/auddoula/BeWork/{}/{}.s norm_spectra/{}_{}.s'.format(s,link,s,i+1))
    out.close()

#for bd-...
print('It will spit out two errors for bd-134933 -- this is normal')
with open('input_info/bd-134933_input.text') as f:
    obs=f.read().splitlines()
out = open('input_info/bd-134933_symlink.text', "w")
nobs = len(obs)
for i,o in enumerate(obs):
    link=o.split()[2]
    test = os.popen('ls -l /home/auddoula/BeWork/bd-13_4933/{}.s'.format(link)).read()
    out.write(test)
    os.system('cp -P /home/auddoula/BeWork/bd-13_4933/{}.s norm_spectra/bd-134933_{}.s'.format(link,i+1))
out.close()

#also a naming issue with hd91120
# the input info has already the .s in the filename
# unlike the other...
print('It will spit out two errors for hd91120 -- this is normal')
s='hd91120'
with open('input_info/{}_input.text'.format(s)) as f:
    obs=f.read().splitlines()
out = open('input_info/{}_symlink.text'.format(s), "w")
nobs = len(obs)
for i,o in enumerate(obs):
    link=o.split()[2]
    test = os.popen('ls -l /home/auddoula/BeWork/{}/{}'.format(s,link)).read()
    out.write(test)
    os.system('cp -P /home/auddoula/BeWork/{}/{} norm_spectra/{}_{}.s'.format(s,link,s,i+1))
out.close()
