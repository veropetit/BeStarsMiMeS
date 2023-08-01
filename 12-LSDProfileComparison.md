# LSD Profile Comparison

Previous: [11-MaskComparison.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/11-MaskComparison.md)

The `12-LSDComparisons.ipynb` is a notebook that creates a PDF that overplots our hybrid model with 0.02 line depth mask (labeled `fullMask`) with a hybrid model using Asif's clean and Asif's clean with tweak, and the observed data with Asif's clean and Asif's clean with tweak masks.

The 12-StatisticsCalculation is a notebook that calculated the SNR ratios of the LSD profiles.
> TODO code broken

## Hybrid/Spectra with Depth0.02/AsifCleanTweak/AsifClean masks. 

The [12-LSDComparison.pdf](https://drive.google.com/file/d/1-DXXo7vZz0fsg00lRT02WEB7zGAD_YOZ/view?usp=drive_link) PDF shows the comparison between these masks/spectra combinations. 

UPDATE
<img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/Comp4_hyb_data_d0.02_ACT-HD189687.png" style="height: 500px"/>

<img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/Comp4_hyb_data_d0.02_ACT-HD148184.png" style="height: 500px"/>


### Conclusions Drawn

#### Well Behaved Star Case
If both the hybrid data using the full mask and the Asif mask are the same, i.e. for the well behaved star case, we would expect the LSDs from the full line mask and Asif's mask to match one another as well as the observed data with Asif's mask (Left). However, if they don’t match the data we can deduce that our synthetic model spectrum isn’t accurate for that star (Right). 

<img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/Comp4_hyb_data_d0.02_ACT-HD189687.png" style="height: 500px"/>


#### Non-Well Behaved Star Case
For the non-well behaved star case, the full and Asif masks are not the same, we would therefore not expect the hybrid models to match each other (Full-green, Asif-orange) but would hope the Asif mask LSD fits the observed data with Asif mask. If the hybrid full mask model doesn’t fit we can’t definitively say whether it is because of an inaccurate model or because of different/more lines being used.

#### Overall Conclusions

Well behaved stars
* 10 of the 16 well behaved stars have a synthetic profile close to the observed profile when using our 0.02 depth mask. 
* 11 of the 16 well behaved stars have a synthetic profile close to the observed profile when using Asif's mask.
* 9 of the 16 well behaved stars have a synthetic profile close to the observed profile when using Asif's tweaked mask.
Using our mask with the synthetic spectra of the well behaved stars we have an accurate fit for just over half the sample. The differences are likely due to our synthetic spectra being incorrect for a few stars. The fit using Asif's mask is nearly the same as for our mask as expected since both mask have the same lines used. 

All stars
* 39 of the 78 stars have a synthetic profile close to the observed profile when using our 0.02 depth mask. 
* 51 of the 78 stars have a synthetic profile close to the observed profile when using Asif's mask.
* 41 of the 78 stars have a synthetic profile close to the observed profile when using Asif's tweaked mask.
Using our mask with the synthetic spectra we have an accurate fit for about half of the sample. For the other half, the obseved and synthetic spectra don't match, indicating that either the synethic spectra is wrong, or that the observed spectra is strange. For Asif's mask, the fit is slightly better as expected. Since the obseverved profile used in this is also using Asif's mask the lines used are the same which throws out a few cases where the primary difference was emissive lines.

A more in-depth look at each star's LSD comparison is done in the google slide, [LSDComparison](https://docs.google.com/presentation/d/1TpAvASuGnMbtFENl-HNuoDTj6M6Dal8Z1gm45aD-Shk/edit#slide=id.g25dc0458b49_0_509)



Next: [13-WhatDoTheBzLookLike.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/13-WhatDoTheBzLookLike.md)