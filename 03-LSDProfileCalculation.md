# LSD profile calculations

Previous page: [02-LSDMaskCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/02-LSDMaskCalculation.md)

The LSD profiles are calculated in Colab notebook [03-LSD-calculations/03-LSD_profiles]()FIX LINK

We make use of the python [LSDpy](https://github.com/folsomcp/LSDpy). The option are as follow:

* normDepth=0.2 
* normLande=1.2 
* normWave=500.0
* removeContPol=1 
* trimMask=0 
* sigmaClipIter=0 
* sigmaClip=500 
* interpMode=1

We set the range of the LSD profile calculation and the pixel size for each star as follows:

* The range is 3 times the listed vsini, plus the maximal value of the listed vrad for the observations if max(vrad) + vsini > 3*vsini. 
* The pixel size is set to 20 points per vsini, with a minimum pixel size of 2.6. 

> NOTE: this last point could be changed for observations that have only HARPS data? What's the pixel size in mks for HARPS?

This is done in the python notebook (Part 1), and the values used for each star are recorded in the cvs file [03-LSD-calculations/Params-LSDProfiles-CalculatedByPython.csv](https://drive.google.com/file/d/1w68qhYsKYRiDHdMRtu7G1zb9WoDrQjSQ/view?usp=sharing) in the `LSD` folder. 

We calculate different sets of LSD profiles, with different combination of spectra (observed/hybrid) and mask (full/asif). The LSD profiles are saved in the `LSD` folder noted in the table below. The file format is `[star]_[obs].lsd`.


| spectra folder | mask folder   | name of LSD folder |
| ------- | ------- | ------------------ |
| Synth-hybrid-spectra | depth0.1_tellClean | hybrid\_\_maskdepth0.1\_tellClean |
| NormalizedSpectra | depth0.1_tellClean |normalized\_\_maskdepth0.1\_tellClean |
| Synth-hybrid-spectra | depth0.02_tellClean | hybrid\_\_maskdepth0.1\_tellClean |
| NormalizedSpectra | depth0.02_tellClean |normalized\_\_maskdepth0.1\_tellClean |
| Synth-hybrid-spectra | MaskCleanedAsif | hybrid\_\_CleanAsif+tellClean |
| NormalizedSpectra | MaskCleanedAsif | normalized\_\_CleanAsif+tellClean |

There are PDF files (named after the directory in the last column above) in the `LSD` directory that corresponds to each set of LSD profiles.

