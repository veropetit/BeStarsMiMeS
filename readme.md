## The premise of this project

- The incidence of magnetism in massive stars is ~10%.
- Be stars are B-type stars that have emission lines in the optical that originate from a Keplerian disk. 

- In the MiMeS survey, there were ~100 Be star observed. If they where like any other magnetic stars, there should be about 10 of them with detectable magnetic fields. However, we found none. This might indicate that the Be-phenomenon and magnetism are mutually exclusive.

- However, Be stars have a lot of emission in their spectral lines, and they usually have broad lines due to their rotation. Therefore, detecting magnetic field might be difficult. Maybe this lack is due to observation biases. So we need to figure out how strong of a magnetic field can be ‘hidden’ in the data.

- The issue is that the spectrum of a Be star is often full of emission. This emission should not affect the circular polarization, but it makes it difficult to get the shape of the lines profile (in direct intensity, or Stokes I). The shape of the line profile is important to calculate the longitudinal field and to do direct modeling. Therefore we know that the Be star do not have a magnetic field (no circular polarization), but it is difficult to know the upper limit for such a magnetic field.

- There are two ways around this:

    1. select only spectral lines that do not show evidence of emission (we do a line averaging called LSD) → the problem with that is that it decrease the signal-to-noise ratio in the circular polarization, because we exclude lines. 
    2. use a synthetic model for the photosphere of the star, to figure out what the line profile would have looked like in the absence of the emission from the Keplerian disk. 

- We are implementing the method #2. Some of the Be stars in the sample don’t have too much emission in their spectrum, which means that we can also compare with method #1 in these cases.

## The content of this repository

The ourpose of this repository is to gather all of the method and codes that are necessary to reproduce our results. 

The initial data and produced data are available on a Shared Google drive (to facilitate the use of Google Collaboratory). 
