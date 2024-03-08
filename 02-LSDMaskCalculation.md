

Previous page: [01-SyntheticProfileCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/01-SyntheticProfileCalculation.md)

---

# LSD mask calculations


## 1. Necessary VALD lines lists

The generation of LSD line masks requires VALD long lists. 

We obtained long-format line list using the extract stellar form in VALD, using the following input:

* Starting wavelength: 3700
* Ending wavelength: 9000
* Detection threshold: 0.01
* Microturbulence: 2
* Line list configuration: Default. 

The line list, renamed in a longlist_TXXXXXgXX format are located in the `UpdatedFiles/00-InputMaterial/VALD-LongList` folder in the Shared Google drive

## 2. Converting the line lists into masks. 

We used the `make_mask` tool provided by the [specpolflow](https://github.com/folsomcp/specpolFlow) python tools to convert the VALD line list into masks. We use the following options:

* depthCutoff=0.1 and 0.02
* atomsOnly=True
* By default, the H 1 lines are not included. 

The initial masks are in the folder `UpdatedFiles/02-MaskCalculations/VALDlist2Mask`, in a subfolder named after the depth parameter, with a filename format `T-----g--_depth___.mask` (e.g. `T20000g40_depth0.02.mask`).

This is done notebook [02-VALDlist2Mask](https://github.com/veropetit/BeStarsMiMeS/blob/master/02-Mask-calculations/02-VALDlist2mask.ipynb)

## 3. Removing regions of telluric and H-wing contamination from the mask

The `make_mask` does not remove lines in the regions in the spectrum that are contaminated by telluric lines (unlike Donati's LSD code?). 

We therefore identified such regions visually in an ESPaDOnS spectrum. 

The wavelength ranges are recoded in the GoogleSpreadsheet [02-ContaminatedregionsWL](https://docs.google.com/spreadsheets/d/19lS0Xg-2ZUs0ps8jZ-JM3pR1YIuC_lWvRMpFAM5VUYI/edit#gid=0)

Additionally, we exclude regions 800+2*vsini km/s around the Balmer series, as well as regions aroung the Balmer gap for which the normalization is difficult (especialy when using the synthetic spectra -- the continnum is drepressed). We also check the vsini width that will be used when making the LSD profiles, if there would be overlap with the Balmer series we extended the exclusion regions accordingly.

The notebook [02-ContaminatedRegionsVisualization](https://github.com/veropetit/BeStarsMiMeS/blob/master/02-Mask-calculations/02-ContaminatedRegionsVisualization.ipynb) provides a visualization of the removed regions. To change the star to be displayed, just change the name and obervation number. 


With this list of regions to exclude, we create a new set of mask in which we remove the lines that falls in these regions (by setting the `isused` column in the mask object to zero). 

This is done in Colab Notebook [02-MaskCleaning](https://github.com/veropetit/BeStarsMiMeS/blob/master/02-Mask-calculations/02-MaskCleaning.ipynb).

The resulting masks are located on the Shared Drive in the folder `UpdatedFiles/02-Mask-calculations/MaskCleaning/depth----_tellClean` with the same naming convention as the initial masks (`T-----g--_depth0.1.mask`). 

## 4. Masks tailored by Asif and Coralie


Asif and Coralie have also tailored some masks to specifically match the observations, keeping only lines that are clearly seen and in absorption ***(is this accurate?)***.

There are two sets of masks: 'cleaned' and 'cleaned and tweaked' (see [11-MaskComparison](https://github.com/veropetit/BeStarsMiMeS/blob/master/11-MaskComparison.md) for more information).
These masks are located in the Shared Drive in the folder `UpdatedFiles/00-InputMaterial/AsifMaskClean` and `UpdatedFiles/00-InputMaterial/AsifMaskCleanTweak`  with a name format `[star]_clean_[obs].mask` and `[star]_clean_[obs].mask_auto_twk`. Note that there are one mask *per observations*, unlike the masks above which are not tailored to individual observations of a given star. 


## 5. Removing lines in telluric regions in the Masks tailored by Asif. 



But just in case, we passed the mask through the same process described in #3 above. 

Furthermore, we noted that the depth of some lines that are used in the mask (the last column of the file mask has a "1" in it) have a depth set to zero (probably coming from the 'tweaking' process?). 
We filtered the mask to set the last column to 0 in these cases. 

These mask are located in the folder `UpdatedFiles/02-Mask-calculations/MaskCleaning/AsifMaskClean_tellClean/` and `UpdatedFiles/02-Mask-calculations/MaskCleaning/AsifMaskCleanTweak_tellClean/` 

Additionally, these masks include some lines with depths smaller than 0.02. Another set of masks was created that removes all lines with depths less than 0.02. These masks are located in the folder `UpdatedFiles/02-Mask-calculations/MaskCleaning/AsifMaskSuperClean_tellClean/` and `UpdatedFiles/02-Mask-calculations/MaskCleaning/AsifMaskSuperCleanTweak_tellClean/` 
---
Next page: [03-LSDProfileCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/03-LSDProfileCalculation.md)


