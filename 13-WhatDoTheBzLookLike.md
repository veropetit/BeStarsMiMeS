# First Look at Bz Calculations **TODO**

Previous page: [12-LSDProfileComparison.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/12-LSDProfileComparison.md)

In the folder `13-BStarComparison`, there is a notebook that create figures used in the analysis of Be vs B stars and of model comparisons.

## Prelimiary Comparison with Normal B Stars

Part 1.1 of the notebook creates a histogram of 3 sigma Bz upper limits of the Be and B type stars. Here is an example of the plot of Be star and normal B-type star (left) and magnetic B-type star Bz upper limits (right) for the hybrid_maskdepth0.1_tellClean model.
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/3sigmaupperlim(0.1).png" style="height: 250px"/>
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/mag3sigmaupperlim(0.1).png" style="height: 250px"/>

It can be seen that the mean and median of the distribution of both the normal B-type and magnetic B-type star cases is lower than that of the Be stars. This indicates that detection of Be star magnetic fields is more difficult than that of non-Be B-type stars.

Comparison of the vsini distribution for the non-Be B-type and Be-type stars was done in section 1.2 of the notebook. It indicates that the 2 samples are in fact separate populations. 
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/BtypeBevsinihist.png" style="height: 250px"/>
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/magBtypeBevsinihist.png" style="height: 250px"/>

Section 2 creates histograms for the 3 sigma upperlimits with the well behaved subsample indicated. This pdf is saved in `13-BStarCoparison/3SigmaBz_hist.pdf`. 

These histograms show that the well behaved and the non-well behaved Be stars have a similar distribution. This indicates that magnetic field detection on Be stars is still more difficult that B stars even without the presense of emission.

Section 3 performs some comparisons between the hybrid and observed spectra using different models. 

3.1 makes two pdfs, one is a plot of sigma Bz of observed vs hybrid spectra for each mask (`SigmaBz_hybridvnorm.pdf`). The second is the same but for Bz (`Bz_hybridvnorm.pdf`).

