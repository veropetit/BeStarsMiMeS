# A first look at the data

## Look at the spectra and check the accuracy of vsini

The Colab Notebook [03-NormalizedSpectra]() Part 1 makes a PDF called [03_NormalizedSpectra.pdf]() with graphs of a portion of the first observation for each star between 420 and 455 nm. 

It also zooms on the CII 426 nm line profile, and makes a plot that is corrected for the radial velocity listed for that observation in the 00-Information spreadsheet (`vradCorrected` column), and adds two vertical lines at the vsini (`Adopted-vsin` column) listed in the spreadsheet. 


In the main Shared Drive, there is a Google Slides document called [Report for BeStarMiMeS notebook 3](https://docs.google.com/presentation/d/1lHtzSIiz-eaCwGxALbdUbKNwxVJCBCuztwmTjRraakA/edit?usp=sharing). In this report, we have recorded our first analysis of the spectra. 

1. We have identifed by eye the best 5 stars that have 'well-behaved' spectra (no emission, visible and symmetric spectral lines. 

	> For later, the typical example will be HD 189687

2. We have identified by eye the best 5 stars that have obvious Be-like spectra (lots of emission all over the place, not too noisy). 

	> For later, the typical example will be HD 148184 (double peak emission)

3. We have also identified stars for which the vsini we have listed seems to be wrong. 

	> We need to cycle back to this and make appropriate modification to the spreadsheet, with a record of the change in the spreadsheet and the slides. 
	
## Look at the comparison between the observation and the computed noisy synthetic spectra. 

The Colab Notebook [03-NormalizedSpectra]() Part 2 makes a PDF called [03\_NS-Synth\_v\_Real.pdf]() with the same graphs as above, but with the noisy synth model spectrum overplotted. 

In the [Report for BeStarMiMeS notebook 3](https://docs.google.com/presentation/d/1lHtzSIiz-eaCwGxALbdUbKNwxVJCBCuztwmTjRraakA/edit?usp=sharing) document, we also identify cases where:

1. The match between the model and the observation looks wrong
2. The noise level of the synthetic model did not seem to match that of the observation itself

	> We need to cycle back to this and make appropriate modification to the spreadsheet, with a record of the change in the spreadsheet and the slides. 
	
## A note on binarity:

One of the star (INSERT HD NUMBER HERE) really looks like a double-lined spectroscopic binary. 

> Insert information here, or link to a report/notebook ?
	
See also below for binarity indication in the TESS lightcurves. 
	
## The status of the Be disk during the observations. 

In WILL BE MOVED TO NOTEBOOK 03? we make graphs of the Halpha line profiles of each stars, overplotted with our synthetic model. The PDF is called [HydrogenAlphaSpectralLine.pdf](). 

The type of emission for each star is noted in the 00-Information spreadsheet, in the column NAME OF COLUMN. 
The Google Slides NAME provides a key and typical profiles images. 

**NOTE**: It seems that HD 164284 has observations with and without the disk present -- good target to test the hybrid method with. 


## Using the TESS LC to check for potential binaries and to check the Be status of the target. 

