# Longitudinal Field Calculations

Previous Page: [03-LSDProfileCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/03-LSDProfileCalculation.md)

The longitudinal magnetic field strengths are calculated in the Colab notebook [04-Bz-calculations](https://github.com/veropetit/BeStarsMiMeS/blob/master/04-Bz-calculations/04-Bz-calculations.ipynb)

We make use of [specpolFlow](https://github.com/folsomcp/specpolFlow) and its Bz.py function. The unchanged parameters are as follows:

* cog = I
* norm = auto
* lambda0 = 500nm
* geff = 1.2
* bzwidth = $\pm$ vsini
* velrange = 1.5( vrad $\pm$ vsini)

The code was then ran for every star and for the various models described in [03-LSDProfileCalculation](https://github.com/veropetit/BeStarsMiMeS/blob/master/03-LSDProfileCalculation.md)
 

Next page: [10-WhatDoTheSpectraLookLike.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/10-WhatDoTheSpectraLookLike.md)
