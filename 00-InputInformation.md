# Input information

## Input tables

The GoogleSpreadsheet in the SharedDrive > BeStars Notebooks > [00-InputInformation](https://docs.google.com/spreadsheets/d/1M6y1Wnsrc-w5FjUMfKaSFa_-foIDAaMe8W4lYNWnWyk/edit?usp=sharing) has the following sheets:


* `Stars` List of all the stars in the sample with star-dependant information (e.g. vsini, Teff, etc)
* `Observations` List of all the observation in the sample, with observation-dependant information (e.g. filename, vrad, etc) 
* `ListOfModels` List of all the unique synthetic model used. 



The Colab Notebook [00-InputInformation](https://github.com/veropetit/BeStarsMiMeS/blob/master/00-InputInformation.ipynb) has some demonstration of
* how we mount the Shared Drive to Colab, 
* how we clone e.g. the [specpolflow](https://github.com/folsomcp/specpolFlow) python tools to use in the notebook
* how we load the 00-Information spreadsheet into a Panda Dataframe and various ways to manipulate Pandata dataframes. 

> NOTE: the notebook could use a bit of cleaning. 


## Gathering the data from the MiMeS server. 

Asif has a `BeWork` folder on the MiMeS server. There is one folder per star (see notes about potentially missing stars in the 00-InputInformation spreadsheet). 

In each folder there is a star_input.text file, which lists the observation 'ID' on the MiMeS server that corresponds to the nomenclature in the 00-InputInformation spreadhseet (i.e. star_1.s, star_2.s)

In Vero's home account (BeStars directory), there is a script (`get_input_info.py`) that reads in the list of stars 'starList.dat', and gathers these _info.text files, and make a copy in the folder `input_info` (PUT ON GOOGLE DRIVE). 

```python
import os

with open('starList.dat') as f:
    star = f.read().splitlines()

for s in star:
    os.system('cp /home/auddoula/BeWork/{}/{}_input.text input_info/'.format(s,s))

os.system('cp /home/auddoula/BeWork/bd-13_4933/bd-134933_input.text input_info/')
# because the naming of the files in not consistant, cannot batch it for this star.

```

In Asif's directory, there is a symbolic link, named after the ID of the observation on the MiMeS server, that points to the same observation that has been normalized by Jason Grunhut. 

The script get_symlink_info.py does two things:
1. it creates a new file per star in the `input_info` folder named `star_symlink.text` that saves the location the symbolic links points to, for record keeping. 
2. it copies the symlinks to the folder `BeStars/norm_spectra` in Vero's home account, and renames then according to the nomenclature used by Asif for his LSD profiles (star_1.s, star_2.s, etc). 

Then, all of the normalized spectra are easily accessible from a single directory. Futhermore, because scp follow the symbolic link, I copied all of the normalized spectra with that naming scheme to my group's cluster (might be a bit big to host on the Google Drive for working in Colab -- I will upload the spectra for the first 3 stars on the list to be able to test the codes in colab, then we can run scripts directly on the server instead?)

```python
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
```

---
Next: [00-1-SyntheticProfileCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/00-1-SyntheticProfileCalculation.md)
