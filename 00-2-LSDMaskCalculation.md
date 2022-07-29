# LSD mask calculations


## 1. Necessary VALD lines lists

The generation of LSD line masks requires VALD long lists. 

We obtained long-format line list using the extract stellar form in VALD, using the following input:

* Starting wavelength: 3700
* Ending wavelength: 9000
* Detection threshold: 0.01
* Microturbulence: 2
* Line list configuration: Default. 

The line list, renamed in a longlist_TXXXXXgXX format are located in the `VALD-LongList` folder in the Shared Google drive

## 2. Converting the line lists into masks. 

We used the `make_mask` tool provided by the [specpolflow](https://github.com/folsomcp/specpolFlow) python tools to convert the VALD line list into masks. We use the following options:

* depthCutoff=0.1 
* atomsOnly=True
* By default, the H 1 lines are not included. 

The initial masks are in the folder `Masks` with a filename format `T-----g--_depth0.1.mask`.

This is done by Part 1 of Colab notebook [01-Loop_over_individual_models](https://github.com/veropetit/BeStarsMiMeS/blob/master/01-Loop_over_individual_models.ipynb)

## 3. Removing regions of telluric contamination from the mask

The `make_mask` does not take into acount the regions in the spectrum that are contaminated by telluric lines (unlike Donati's LSD code?). 

We therefore identified such regions visually in Colab notebook [04-Telluric_contamination.ipynb](https://github.com/veropetit/BeStarsMiMeS/blob/master/04-Telluric_contamination.ipynb). 

In the notebook, there is a sample ESPaDOnS spectrum, with the wavelength ranges excluded from the masks shaded in grey. 

The wavelenght ranges are recoded in the GoogleSpreadsheet [04-ContaminatedregionsWL](https://docs.google.com/spreadsheets/d/19lS0Xg-2ZUs0ps8jZ-JM3pR1YIuC_lWvRMpFAM5VUYI/edit?usp=sharing).

We then create a new set of mask in which we remove the lines that falls in these regions (by setting the `isused` column in the mask object to zero). 

This is done in Part 2 of Colab Notebook [01-Loop_over_individual_models](https://github.com/veropetit/BeStarsMiMeS/blob/master/01-Loop_over_individual_models.ipynb).

The resulting masks are located on the Shared Drive in the folder `Masks/depth0.1_tellClean` with the same naming convention as the initial masks (`T-----g--_depth0.1.mask`). 

## 4. Masks tailored by Asif

Asif has tailored some masks to specifically match the observations, keeping only lines that are clearly seen and in absorption ***(is this accurate?)***.

These masks are located in the Shared Drive in the folder `MaskCleanedAsif`  with a name format `[star]_clean_[obs].mask_auto_twk`. Note that there are one mask *per observations*, unlike the masks above which are not tailored to individual observations of a given star. 




