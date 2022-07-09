# Synthetic spectra calculations


## 1. Necessary VALD lines lists

Obtained extract stellar linelists (short format) for 34 temperatures from 10500 to 31000 K, log g 3.5 or 4.0. 

Adopted 2 km/s microturbulence

These temperatures/gravities correspond to the range of observed stellar parameters. 

At this moment I can’t recall where those parameters came from. (GAW: Be_2019/WORKING/VALD)

The line lists are in the `VALD-ShortList-AtmModels` folder of the Shared Google Drive. They are in the format `ap00k2_T-----G--.lst`
 

## 2. Compute the local synthetic spectra

For each unique model (see the `List of unique models` in the 00-NeededInformation), using `Synth3` to compute the local synthetic spectra at various angles. 

The executable code and user manual for `Synth3` can be found here:
[https://www.astro.uu.se/~oleg/synth3.html](https://www.astro.uu.se/~oleg/synth3.html)

In short, we need a VALD short list (see #1 above), as well as the accompanying model atmosphere that is listed towards the end of the line list file:


```
'He 1',       8996.9890,  23.0737, 2.0, -0.764, 0.000, 0.000, 0.000, 99.000, 0.010, '   3 wl:K   3 K   3 gf:K   3 K   3 K   3 K   3 K He            '
'castelli_ap00k2_T12000G40.krz',
'H :  0.92','He: -1.11', 'Li:-10.94','Be:-10.64','B : -9.49','C : -3.52','N : -4.12','O : -3.21',

```

The Kurucz atmopshere models, named appropriately, are in the same folder as the Short VALD list (see above). 

For each models, the following commands calculated the local intensity and creates a .mout file:

```
synth3.Darwin_Intel ap00k2_T-----G--.lst  T-----G--.mout
```

Gregg did this locally on his machine. 

The output files are in the `Synth-local-spectra` folder of the Shared Google Drive. 


## 3. Compute the disk-integrated spectra

For each observed star, we compute a disk-integrated spectrum using Oleg’s `s3div` incorporating the star’s observed vsini (GAW: Be_2019/WORKING/*dsk). 

The vsini used are listed in the `00-Information` spreadsheet. 

> TODO: check!! At this moment I can’t recall where the vsini came from. For the 2012 study it was from fitting the observed, cleaned LSD profiles. 
 
The executable code and manual for `s3div` are the same as for `Synth3` (see above). 

`s3div` takes the .mout file created above, and performs the disk integration with a specified vsini, vmacro. We can specify also the resolution of the output spectrum (in a grid with log(lambda) spacing), as well as the instrument resolution to convolve the spectrum with (e.g. 65000 for ESPaDOnS).

The command line syntax is as follow: 

```
s3di <input file> <output file> [ <v sin i> <vmacro> <Resol> <Instrum> ]
s3div  T15000G40.mout hd6226_1.dsk 120.00 2.0 167000 65000
```

As it turns out, Google Colab notebooks are able to run command line executable that lives on a mounted Google Drive (!!!!)

Therefore, the Synth executables (downloaded 2022-07-09) are in the folder `Synth-codes`. The colab notebook `03-Synth-calculations.ipynb` runs `s3div.Linux` in a loop over the stars, using the information in the spreadsheet. 

> I've only made the demo with a single star -- ask the undergrads to code up the necessary loop.

The output files (one per star in the sample) are in `Synth-diskint-spectra` folder of the Shared Drive. 


 