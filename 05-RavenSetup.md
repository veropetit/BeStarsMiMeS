Previous page: [04-LongitudinalFieldCalculation.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/04-LongitudinalFieldCalculation.md)


The LSD profiles and information about each star and all of its observations are then compiled and a set of `dataPackets` are created in the notebook [05-RavenSetup](https://github.com/veropetit/BeStarsMiMeS/blob/master/04-Bz-calculations/05-RavenSetup.ipynb) using the `create_Packet` function within pyRaven.

These `dataPackets` are saved as `.h5` files and are what is loaded into pyRaven to calculated Bpole. 

The `dataPackets` require the following information, all of which are input into the `create_Packet` function:
* star_name - the name of the star (string)
* nobs - the number of observations (integer)
* obs_names - the names of the observations (string)
* vrad - list of the radial velocity of each observation (in km/s)
* Ic - list of continuum normalization values
* wint_data - a list of the intensity weigth used to calculate the LSD profiles used
* wpol_data - a list of the polarization weigth used to calculate the LSD profiles used
* wint_rav - the unique intensity weigth that will be used to scale the LSD profile for pyRaven
* wpol_rav - the unique polarization weigth that will be used to scale the LSD profile for pyRaven
* fitrange - size of the area to be used in the fit (just the line, no continuum) (float, in km/s)
* vsini - the vsini of the star (float, in km/s)
* original - list of lsd profiles for all of the observation

`original` can be obtained using the pyRaven function `read_lsds_from_sfiles`, which takes in a list of file names and converts them into a list of lsd profiles to be input into the `create_Packet` function. 

The packet then automatically creates two other lsd objects for a total of 3 objects. 
* original -  the LSDprof object containing the original LSD profiles (passed to the function at initialization)
* scaled - the LSDprof object containing the LSD profiles that have been corrected for radial velocity, normalized to the continuum, and re-scaled to a common LSD weigth. This calculation is done during initialization, using the meta information provided
* cutfit - the re-scaled LSD profiles that have been cut to only contain the velocity region to be fitted by pyRaven (for ease of computation). This calculation is done during initialization, using the meta information provided.

The notebook then writes the `dataPackets` to `.h5` files for input into pyRaven later on. 

**Note:** Add bit about the models used and output locations. Waiting on completion. 

Next page: [10-WhatDoTheSpectraLookLike.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/10-WhatDoTheSpectraLookLike.md)