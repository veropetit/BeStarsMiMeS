# Longitudinal Field Calculations

Previous Page: [03-LSDProfileCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/03-LSDProfileCalculation.md)

The longitudinal magnetic field strengths are calculated in the notebook [04-Bz-calculations](https://github.com/veropetit/BeStarsMiMeS/blob/master/04-Bz-calculations/04-Bz-calculations.ipynb)

## Bz calculations
In the Colab Notebook [04-Bz-calculations](https://colab.research.google.com/drive/14DFc3BYPuHDJJu-sBEmGWcWd118CthJ0?usp=sharing), part 1 gives an example for one entire model.

Part 2 then calculates Bz for every observation and every model and saves the output figures to a pdf and the output tables as a csv files. The files created by this step are named after the model. 

Part 3 then repeats part 2 for the subset of Be stars with little to no emission, called well behaved stars.

We make use of [specpolFlow](https://github.com/folsomcp/specpolFlow) and its Bz.py function to perform all calculations. The parameters are as follows:

* cog = vrad
* norm = auto
* lambda0 = 500nm
* geff = 1.2
* bzwidth = $\pm$ vsini
* velrange = vrad $\pm$ 1.5vsini

The outputs are saved as `.csv` files in `UpdatedFiles/04-Bz-calculations` with the format `{model}.csv`

Next page: [05-RavenSetup.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/05-RavenSetup.md)
