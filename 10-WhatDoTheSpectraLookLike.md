# A first look at the data

In the folder `10-Spectra-Data-vs-hybrid-plots and Halpha and TESS`, there are a few notebooks that creates the figures used in the analysis below. 

## Look at the spectra and check the accuracy of vsini

The Colab Notebook [10-NormalizedSpectra]()FIX LINK Part 1 makes a PDF called [10-NormalizedSpectra_CII_dataonly.pdf](https://drive.google.com/file/d/12uQEITrQssGc2uVQjlkbxOn9OMSIWnii/view?usp=share_link) with graphs of a portion of the first observation for each star between 420 and 455 nm. 

It also zooms on the CII 426 nm line profile, and makes a plot that is corrected for the radial velocity listed for that observation in the 00-Information spreadsheet (`vradCorrected` column), and adds two vertical lines at the vsini (`Adopted-vsin` column) listed in the spreadsheet. 


In the main Shared Drive, there is a Google Slides document called [Report on the spectra and model comparison](https://docs.google.com/presentation/d/1lHtzSIiz-eaCwGxALbdUbKNwxVJCBCuztwmTjRraakA/edit?usp=sharing). In this report, we have recorded our first analysis of the spectra. 

1. We have identifed by eye the best 5 stars that have 'well-behaved' spectra (no emission, visible and symmetric spectral lines. 

	> For later, the typical example will be HD 189687 
	>
	><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/NormalizedSpectra_CII_dataonly-HD189687.png" style="height: 500px"/>

2. We have identified by eye the best 5 stars that have obvious Be-like spectra (lots of emission all over the place, not too noisy). 

	> For later, the typical example will be HD 148184 (double peak emission)
	>
	><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/NormalizedSpectra_CII_dataonly-HD148184.png" style="height: 500px"/>


3. We have also identified stars for which the vsini we have listed seems to be wrong. 

	> We need to cycle back to this and make appropriate modification to the spreadsheet, with a record of the change in the spreadsheet and the slides. 
	
## Look at the comparison between the observation and the computed noisy synthetic spectra. 

The Colab Notebook [10-NormalizedSpectra]() Part 2 makes a PDF called [NormalizedSpecta_CII_DataVSynth.pdf](https://drive.google.com/file/d/1VhZMLk1IcdSYZOmOP7tYBC5F3YuT4-QH/view?usp=sharing) with the same graphs as above, but with the noisy synth model spectrum overplotted. 

In the [Report on the spectra and model comparison](https://docs.google.com/presentation/d/1lHtzSIiz-eaCwGxALbdUbKNwxVJCBCuztwmTjRraakA/edit?usp=sharing) document, we also identify cases where:

1. The match between the model and the observation looks wrong
2. The noise level of the synthetic model did not seem to match that of the observation itself

	> We need to cycle back to this and make appropriate modification to the spreadsheet, with a record of the change in the spreadsheet and the slides. 
	
## A note on binarity:

BELOW NEEDS TO BE UPDATED WITH PROPER LOCATION

One of the star (HD 35411) really looks like a double-lined spectroscopic binary. 

The notebook [Binaries]()FIX LINK has both the line profile and TESS light curves of this star.
	
See also below for binarity indication in the TESS lightcurves. 
	
## The status of the Be disk during the observations. 

In UPDATE NOTEBOOK NAME AND LOCATION, we make graphs of the Halpha line profiles of each stars, overplotted with our synthetic model. The PDF is called [HydrogenAlphaSpectralLine.pdf](https://drive.google.com/file/d/1-R4aPO_D18BwZV-Od_E1YU0JuNaYgOvJ/view?usp=share_link). 

The type of emission for each star is noted in the 00-Information spreadsheet, in the column `Halpha shape`. 
The Google Slides (HalphaCharacterization)[https://docs.google.com/presentation/d/1wyPI9kbeioUcQsewTiVvA9LkyhTY_sCioh58Gt9i2cQ/edit?usp=sharing] provides a key and typical profiles images. 

**NOTE**: It seems that HD 164284 has observations with and without the disk present -- good target to test the hybrid method with. 

<img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/HydrogenAlphaSpectralLine-HD164284" style="height: 500px"/>

## Using the TESS LC to check for potential binaries and to check the Be status of the target. 

The Colab Notebook [TESS Observations]()FIX LINK makes a PDF called [TESS observations.pdf](https://drive.google.com/file/d/12xSyInSpHGMBI4hGfU8uQ88Zz_H2lqXc/view?usp=share_link). The pdf plots the light curves, periodogram, and zoomed periodogram for each TESS observation with a cadence of 2 minutes or less. 

By observing TESS observations of our Be stars, we can identify obvious binaries or otherwise strange stars. There are 2 obvious eclipsing binaries in our sample, HD 35411 and HD 76838, which can be identified by their characteristic periodic flux dips at regular intervals. 

Additionally there are a few other less obvious binaries that are flagged due to regular periodic dips or sinusoidal variation. Some of these stars may just be pulsators rather than binaries which is why looking at the Halpha spectra might help indentify if it is a binary,

Finally there is one star that is an obvious non-Be star due to three observed stellar flares that typically occur on low mass stars.

The binarity of these systems can sometimes also be seen in the Halpha line, which is especially useful for the non-obvious binaries. See the A note on binarity section above.




