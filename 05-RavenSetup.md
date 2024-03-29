Previous page: [04-LongitudinalFieldCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/04-LongitudinalFieldCalculation.md)


The LSD profiles and information about each star and all of its observations are then compiled and a set of `dataPackets` are created in the notebook [05-RavenSetup](https://github.com/veropetit/BeStarsMiMeS/blob/master/04-Bz-calculations/05-RavenSetup.ipynb) using the `create_Packet` function within pyRaven.

These `dataPackets` are saved as `.h5` files and are what is loaded into pyRaven to calculated Bpole. 

The `dataPackets` require the following information, all of which are input into the `create_Packet` function:
* star_name - the name of the star (string)
* nobs - the number of observations (integer)
* obs_names - the names of the observations (string)
* vrad - list of the radial velocity of each observation (in km/s)
* Ic - list of continuum normalization values
* wint_data - a list of the intensity weight used to calculate the LSD profiles used
* wpol_data - a list of the polarization weight used to calculate the LSD profiles used
* wint_rav - the unique intensity weight that will be used to scale the LSD profile for pyRaven
* wpol_rav - the unique polarization weight that will be used to scale the LSD profile for pyRaven
* fitrange - size of the area to be used in the fit (just the line, no continuum) (float, in km/s)
* vsini - the vsini of the star (float, in km/s)
* original - list of lsd profiles for all of the observation

`original` can be obtained using the pyRaven function `read_lsds_from_sfiles`, which takes in a list of file names and converts them into a list of lsd profiles to be input into the `create_Packet` function. 

The packet then automatically creates two other lsd objects for a total of 3 objects. 
* original -  the LSDprof object containing the original LSD profiles (passed to the function at initialization)
* scaled - the LSDprof object containing the LSD profiles that have been corrected for radial velocity, normalized to the continuum, and re-scaled to a common LSD weight. This calculation is done during initialization, using the meta information provided
* cutfit - the re-scaled LSD profiles that have been cut to only contain the velocity region to be fitted by pyRaven (for ease of computation). This calculation is done during initialization, using the meta information provided.

The notebook then writes the `dataPackets` to `.h5` files for input into pyRaven later on. 

Currently (07/31/2023), the normalized and hybrid models with 0.02 depth have both been completed. The output `.h5` files are saved in `UpdatedFiles/05-RavenSetup/{model}`. Pdfs with plots of the three cuts have also been created for the two models and are saved in `UpdatedFiles/05-RavenSetup` as `05-{model}_DataPacket.pdf` where `{model}` is the respective model

The notebook `05-RavenFitting.ipynb` fits a Voigt function to the LSD profile of each star to calculate fundamental parameters such as the line strength parameter, kappa, and the macroturbulence. This notebook creates a pdf with plots of the LSD profile and the fitted model, these files are `05-RavenSetup/hybrid0.02FitModel.pdf` and `05-RavenSetup/normSuperCleanFitModel.pdf`. Additionally, this notebook creates `.json` param files to be used in the Bayesian analysis and a `.csv` file with all of the fit parameters. The param files are located in `05-RavenSetup/param_hybrid` and `05-RavenSetup/param_norm` depending on if the fit was performed on the hybrid 0.02 depth LSD profile or the normalized super clean Asif LSD profile. 

The final notebook, `05-GridChoice.ipynb`, calculates the grid ranges for the Bayesian fit. The ranges are added to the param `.json` files for each star created in the previous step. The Bpole grid is calculated by finding the maximum Bpole value that would be less than 4 standard deviations of the Stokes V profile. The obliquity grid is between 0 and 180, the phase is between 0 and 360. The inclination grid is limited by the vsini of the star. Assuming a equitorial critical velocity of 500 $km\, s^{-1}$, we can limit the possible inclination values using the following equation:
$$
i_{\text{min}} = \arcsin{\left(\frac{\text{vsini}}{500}\right)}\frac{180}{\pi}
$$
The inclination grid is then between $i_{\text{min}}$ and $180-i_{\text{min}}$.

Next page: [10-WhatDoTheSpectraLookLike.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/10-WhatDoTheSpectraLookLike.md)