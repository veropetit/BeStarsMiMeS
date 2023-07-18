# Longitudinal Field Calculations

Previous Page: [03-LSDProfileCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/03-LSDProfileCalculation.md)

The longitudinal magnetic field strengths are calculated in the notebook [04-Bz-calculations](https://github.com/veropetit/BeStarsMiMeS/blob/master/04-Bz-calculations/04-Bz-calculations.ipynb)

We make use of [specpolFlow](https://github.com/folsomcp/specpolFlow) and its Bz.py function. The parameters are as follows:

* cog = vrad
* norm = auto
* lambda0 = 500nm
* geff = 1.2
* bzwidth = $\pm$ vsini
* velrange = vrad $\pm$ 1.5vsini

The code was then ran for every star and for the various models described in [03-LSDProfileCalculation](https://github.com/veropetit/BeStarsMiMeS/blob/master/03-LSDProfileCalculation.md)

The outputs are saved as `.csv` files in `UpdatedFiles/04-Bz-calculations` with the format `{model}.csv`


 

Next page: [05-RavenSetup.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/05-RavenSetup.md)
