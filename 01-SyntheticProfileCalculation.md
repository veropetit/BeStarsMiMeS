# Synthetic spectra calculations


## 1. Necessary VALD lines lists

Obtained extract stellar linelists (short format) for 34 temperatures from 10500 to 31000 K, log g 3.5 or 4.0. 

Adopted 2 km/s microturbulence

These temperatures/gravities correspond to the range of observed stellar parameters. 

At this moment I can’t recall where those parameters came from. (GAW: Be_2019/WORKING/VALD)

The line lists are in the `VALD-ShortList` folder of the Shared Google Drive. 

> TODO: Put the files in the folder. 

## 2. Compute the local synthetic spectra

For each unique model (see the `List of unique models` in the 00-NeededInformation), using `Synth3` to compute the local synthetic spectra. 

> TODO: add reference to Synth here. 

```
Enter command line here, or name of script?
```

The output files are in the `Synth-local-spectra` folder of the Shared Google Drive. 

> TODO: put the files in the folder.

## 3. Compute the disk-integrated spectra

For each observed star, computed a disk-integrated spectrum using Oleg’s `s3div` incorporating the star’s observed vsini (GAW: Be_2019/WORKING/*dsk). 

The vsini used are listed in the NAME OF TABLE. 

> TODO: check!! At this moment I can’t recall where the vsini came from. For the 2012 study it was from fitting the observed, cleaned LSD profiles. 
 
> TODO: add ref to s3div here

```
Enter command here, or link to script?
```

The output files (one per star in the sample) are in `Synth-disk-integrated-spectra` folder of the Shared Drive. 


 