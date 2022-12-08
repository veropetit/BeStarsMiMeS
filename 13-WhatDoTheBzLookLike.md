# First Look at Bz Calculations

Previous page: [12-LSDProfileComparison.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/12-LSDProfileComparison.md)

In the folder `04-Bz-calculations`, there are two notebooks that calculate Bz for our stars and create figures used in the analysis.

## Bz calculations
In the Colab Notebook [04-Bz-calculations](https://colab.research.google.com/drive/14DFc3BYPuHDJJu-sBEmGWcWd118CthJ0?usp=sharing), part 1 gives an example of the Bz calculation for a single observation. The first part of part 2, gives an example for one entire model and the second makes a Stokes V vs Null detection plot for debugging and identification of trouble stars/observations.

Here is an example of the plot for one of our models. Since Be stars have no apparent Stokes V signitures, any stars high on the y-axis of the plot should be followed up with visual inspection.
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/StokesVvsNulldetection_hybrid01.png" style="height: 250px"/>

Part 3 then calculates Bz for every observation and every model and saves the output figures to a pdf and the output tables as a csv files. The files created by this step are named after the model. 

Part 4 averages the all the observations for a particular star with each model, then outputs a csv file with the average Bz calculations for each star and each observation. The csv file as the same convention as part 3 with an `_final` at the end.

## Prelimiary Comparison with Normal B Stars

Comparison of the vsini distribution for the non-Be B-type and Be-type stars indicates that the 2 samples are in fact separate populations. 
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/BtypeBevsinihist.png" style="height: 250px"/>
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/magBtypeBevsinihist.png" style="height: 250px"/>


Here is an example of the plot of Be star and normal B-type star (left) and magnetic B-type star Bz upper limits (right) for the hybrid_maskdepth0.1_tellClean model.
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/3sigmaupperlim(0.1).png" style="height: 250px"/>
><img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/mag3sigmaupperlim(0.1).png" style="height: 250px"/>

It can be seen that the mean and median of the distribution of both the normal B-type and magnetic B-type star cases is lower than that of the Be stars. This indicates that detection of Be star magnetic fields is more difficult than that of non-Be B-type stars.

