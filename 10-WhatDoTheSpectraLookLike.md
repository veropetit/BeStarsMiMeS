# A first look at the data

Previous page: [05-RavenSetup.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/05-RavenSetup.md)

In the folder `10-Spectra-Data-vs-hybrid-plots and Halpha and TESS`, there are a few notebooks that creates the figures used in the analysis below. 

## Look at the spectra and check the accuracy of vsini

The notebook [10-NormalizedSpectra](https://github.com/veropetit/BeStarsMiMeS/blob/master/10-Spectra-Data-vs-hybrid-plots%20and%20Halpha%20and%20TESS/10-Normalized-spectra.ipynb) Part 1 makes a PDF called [NormalizedSpectra_CII_dataonly.pdf](https://drive.google.com/file/d/1umft-pxUyWMxOcuqlPwVOb6XcZtFbo39/view?usp=sharing) with graphs of a portion of the first observation for each star between 400 and 435 nm. 

It also zooms on the CII 426 nm line profile and the HeI 402 nm line profile, and makes a plot of each that is corrected for the radial velocity listed for that observation in the 00-Information spreadsheet (`vradCorrected` column), and adds two vertical lines at the vsini (`vsini-estimate` column) listed in the spreadsheet. 


In the main Shared Drive, there is a Google Slides document called [Report on the spectra and model comparison](https://docs.google.com/presentation/d/1lHtzSIiz-eaCwGxALbdUbKNwxVJCBCuztwmTjRraakA/edit?usp=sharing). In this report, we have recorded our first analysis of the spectra.

1. We have identifed by eye the best 5 stars that have 'well-behaved' spectra (no emission, visible and symmetric spectral lines). 

	> For later, the typical example will be HD 189687 
	>
	><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/NormalizedSpectra_CII_dataonly-HD189687.png" style="height: 500px"/>

2. We have identified by eye the best 5 stars that have obvious Be-like spectra (lots of emission all over the place, not too noisy). 

	> For later, the typical example will be HD 148184 (double peak emission)
	>
	><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/NormalizedSpectra_CII_dataonly-HD148184.png" style="height: 500px"/>


3. We have also identified stars for which the vsini we have listed seems to be wrong. 

	> Patrick has reestimated the vsini by eye and the results have been recorded in the `vsini-estimate` column. Stars with `very bad` listed could not be estimated and their vsini will remain `adopted-vsini`. The results are shown in the [vsinicorrections.pdf](https://drive.google.com/file/d/1-8hWHfCDbZbzotqSyBnnhvNA7b4e7DVU/view?usp=sharing)
	
## Look at the comparison between the observation and the computed noisy synthetic spectra. 

The notebook [10-NormalizedSpectra](https://github.com/veropetit/BeStarsMiMeS/blob/master/10-Spectra-Data-vs-hybrid-plots%20and%20Halpha%20and%20TESS/10-Normalized-spectra.ipynb) Part 2 makes a PDF called [NormalizedSpecta_CII_DataVSynth.pdf](https://drive.google.com/file/d/1unQ_iq1EzPsgkd5N4Zg21b8zWVC9wurE/view?usp=sharing) with the same graphs as above, but with the noisy synth model spectrum overplotted. 

In the [Report on the spectra and model comparison](https://docs.google.com/presentation/d/1lHtzSIiz-eaCwGxALbdUbKNwxVJCBCuztwmTjRraakA/edit?usp=sharing) document, we also identify cases where:

1. The match between the model and the observation looks wrong
2. The noise level of the synthetic model did not seem to match that of the observation itself

	> We need to cycle back to this and make appropriate modification to the spreadsheet, with a record of the change in the spreadsheet and the slides. 
	
## A note on binarity:

In the `InputInformation` spreadsheet there are two columns that indicate binarity. The `SB-flag` column indicates whether a star is a spectroscopic binary, and the `SB9 catalog` column gives the spectroscopic binary classification according to the SB9 catalog.
	
See also below for binarity indication in the TESS lightcurves. 
	
## The status of the Be disk during the observations. 

In `UpdatedFiles/10-Spectra-Data-vs-hybrid-plots and Halpha and TESS/10-Normalized-spectra.ipynb`, we make graphs of the Halpha line profiles of each stars, overplotted with our synthetic model. The PDF is called [NormalizedSpectra_Halpha_dataonly.pdf](https://drive.google.com/file/d/1untISEcdpwD9ll4wgdN-yDPajA3Zij9F/view?usp=drive_link). 

The type of emission for each star is noted in the 00-Information spreadsheet, in the column `Halpha shape`. 
The Google Slides [HalphaCharacterization](https://docs.google.com/presentation/d/1wyPI9kbeioUcQsewTiVvA9LkyhTY_sCioh58Gt9i2cQ/edit?usp=sharing) provides a key and typical profiles images. 

**NOTE**: It seems that HD 164284 has observations with and without the disk present -- good target to test the hybrid method with. 

<img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/HydrogenAlphaSpectralLine-HD164284.png" style="height: 500px"/>

## Using the TESS LC to check for potential binaries and to check the Be status of the target. 

The notebook `10-TESS-Observations.ipynb` makes a PDF called [TESS observations.pdf](https://drive.google.com/file/d/1up3vy7V5IXmt5DXdSLCRLO5u9Gc529iJ/view?usp=drive_link)FIX LINK. The pdf plots the light curves, periodogram, and zoomed periodogram for each TESS observation with a cadence of 2 minutes or less. 

By observing TESS observations of our Be stars, we can identify obvious binaries or otherwise strange stars. There are 2 obvious eclipsing binaries in our sample, HD 35411 and HD 76838, which can be identified by their characteristic periodic flux dips at regular intervals. 

Additionally there are a few other less obvious binaries that are flagged due to regular periodic dips or sinusoidal variation. Some of these stars may just be pulsators rather than binaries which is why looking at the spectra might help indentify if it is a binary,

[Labadie-Bartz J. et al. 2022](https://iopscience.iop.org/article/10.3847/1538-3881/ac5abd#ajac5abdapp3) has some notes on a handful of stars in our sample that are summarized in the table below. 

| HD | TIC   | Labadie-Bartz J. et al. 2022 Notes | 
| ------- | ------- | ------------------ |
| 76838 | 30562668 | Firmly Nonclassical, rejected from sample, Embedded in a nubula |
| 221507 | 224244458 | Firmly Nonclassical, rejected from sample. HgMnSi star |
| 52918 | 269087549 | Possible Nonclassical, rejected from sample | 
| 50820 | 282808223 | Possible Nonclassical, kept in sample, variable emission |
| 110335 | 405520863 | Possible Nonclassical, kept in sample, constant Halpha with exactly the same profile between 2014 and 2015 |
| 58978 | 139385056 | Be star of interest, Be+sdO binary |

Jon also made notes on individual stars in the `JonNotes` column of the spreadsheet.


---
Next page: [11-MaskComparison.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/11-MaskComparison.md)