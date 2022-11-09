

Previous page: (01-SyntheticProfileCalculation.md)[https://github.com/veropetit/BeStarsMiMeS/blob/master/01-SyntheticProfileCalculation.md]

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

The line list, renamed in a longlist_TXXXXXgXX format are located in the `00-InputMaterial/VALD-LongList` folder in the Shared Google drive

## 2. Converting the line lists into masks. 

We used the `make_mask` tool provided by the [specpolflow](https://github.com/folsomcp/specpolFlow) python tools to convert the VALD line list into masks. We use the following options:

* depthCutoff=0.1 and 0.02
* atomsOnly=True
* By default, the H 1 lines are not included. 

The initial masks are in the folder `02-MaskCalculations/VALDlist2Mask`, in a subfolder named after the depth parameter, with a filename format `T-----g--_depth___.mask` (e.g. `T20000g40_depth0.02.mask`).

This is done Colab notebook [02-VALDlist2Mask]()FIX LINK!

## 3. Removing regions of telluric and H-wing contamination from the mask

The `make_mask` does not remove lines in the regions in the spectrum that are contaminated by telluric lines (unlike Donati's LSD code?). 

We therefore identified such regions visually in an ESPaDOnS spectrum. 

The wavelenght ranges are recoded in the GoogleSpreadsheet [02-ContaminatedregionsWL]()FIX LINK.

Additionally, we exclude regions 1000 km/s aroung the Balmer series, as well as regions aroung the Balmer gap for which the normalization is difficult (especialy when using the synthetic spectra -- the continnum is drepressed)

The notebook [02-ContaminatedRegionsVisualization]()FIX LINK provides a visualization of the removed regions. To change the star to be displayed, just change the name and obervation number. 


With this list of regions to exclude, we create a new set of mask in which we remove the lines that falls in these regions (by setting the `isused` column in the mask object to zero). 

This is done in Colab Notebook [02-MaskCleaning]()FIX LINK.

The resulting masks are located on the Shared Drive in the folder `02-Mask-calculations/MaskCleaning/depth----_tellClean` with the same naming convention as the initial masks (`T-----g--_depth0.1.mask`). 

## 4. Masks tailored by Asif and Coralie


Asif and Coralie have also tailored some masks to specifically match the observations, keeping only lines that are clearly seen and in absorption ***(is this accurate?)***.

There are two sets of masks: 'cleaned' and 'cleaned and tweaked' (see [11-MaskComparison](https://github.com/veropetit/BeStarsMiMeS/blob/master/11-MaskComparison.md) for more information).
These masks are located in the Shared Drive in the folder `00-InputMaterial/AsifMaskClean` and `00-InputMaterial/AsifMaskCleanTweak`  with a name format `[star]_clean_[obs].mask` and `[star]_clean_[obs].mask_auto_twk`. Note that there are one mask *per observations*, unlike the masks above which are not tailored to individual observations of a given star. 


## 5. Removing lines in telluric regions in the Masks tailored by Asif. 


We kinda assume that the lines in the telluric regions were remove by Asif in the tailoring process
> Check this with them

But just in case, we passed the mask through the same process described in #3 above. 

Furthermore, we noted that the depth of some lines that are used in the mask (the last column of the file mask has a "1" in it) have a depth set to zero (probably coming from the 'tweaking' process?). 
We filtered the mask to set the last column to 0 in these cases. 

These mask as located in the folder `Masks/Asif_tellClean/` 
 
---
Next page: (03-LSDProfileCalculation.md)[https://github.com/veropetit/BeStarsMiMeS/blob/master/03-LSDProfileCalculation.md]


