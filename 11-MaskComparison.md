# Mask Comparison

Previous: [10-WhatDoTheSpectraLookLike.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/10-WhatDoTheSpectraLookLike.md)

In the folder 11-MaskComparison, there is a Colab notebook that can, in Part 1, read select one specific observation and create a comparison of the available masks. At the end of Part1, there is also a cell to output a few rows of the mask files, for a direct numerical comparison. 

In Part 2, the notebook creates a histrogram of number of lines per depth, for a comparison between the mask we are using with the hybrid method and the mask Cleaned and Cleaned/Tweaked by Asif and Coralie. For the latter, we don't count the lines for which the depth has been set to zero. 

In Part 3, the notebook creates a multi-page PDF with all of the histograms, that are located in `UpdatedFiles/11-MaskComparison/`. The AsifMaskClean comparison is in `Mask_depth_hist_AsifClean.pdf` and the AsifMaskCleanTweak comparision is in `Mask_depth_hist_AsifCleanTweak.pdf`.

## Findings

There are a few differences between the AsifMaskClean and our masks in terms of the depths. It might be that we are using a slightly different temperature, or that we are using more recent VALD list to create our masks (Coralie can advise?)

The AsifCleanTweak masks have a lot of lines that are in use (last column set to 1) but that have a depth of zero. In many cases, there are a cluster of close lines, with only one of them having non-zero depth after the tweaking -- not sure how this impacts the LSD profile calculation. 

As expected, the masks that have been cleaned for 'well-behaved' stars have a similar # of lines. 

<img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/MaskHisto-HD189687.png" style="height: 500px"/>

But for stars with a lot of emission in the spectrum, the number of lines is greater in our mask, also as expected. 

<img src="https://github.com/veropetit/BeStarsMiMeS/blob/master/DocumentationImages/MaskHisto-HD148184.png" style="height: 500px"/>

Next: [12-LSDProfileComparison.md](https://github.com/veropetit/BeStarsMiMeS/blob/master/12-LSDProfileComparison.md)