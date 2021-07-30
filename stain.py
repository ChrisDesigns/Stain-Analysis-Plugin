#!/usr/bin/env python3

# Note must install plugin(s):
# https://sites.imagej.net/adaptiveThreshold/
# https://sites.imagej.net/Tboudier/

from ij import IJ
from ij.gui import Roi
from ij.io import OpenDialog

from ij.plugin import Stack_Statistics
from ij.plugin.frame import RoiManager

from loci.plugins import BF

od = OpenDialog("Choose image file", None)
file_name = od.getFileName()


# average radius of cell
simga = 5
# threashhold mean limit
# in the cause of ADAPTIVE_THRESH_GAUSSIAN_C, this was equal to gSig
thresh_mean = 5
# ignore components with smaller size
min_area_size = 30


if None != file_name:
    folder = od.getDirectory()
    path = folder + file_name

    imps = BF.openImagePlus(path)

    RM = RoiManager()  # create instance of ROI Manger
    rm = RM.getRoiManager() # activate ROI Manger

    for imp in imps:
        imp.show()
        # average the values
        IJ.run("Z Project...", "projection=[Average Intensity]")
        # apply a blur
        IJ.run("Gaussian Blur...", "sigma="+str(simga))
        # min-max normalization
        # not needed
        #
        # set to 8 bit image
        IJ.run("8-bit")
        # Run adaptive thresholding
        # Doesn't offer ADAPTIVE_THRESH_GAUSSIAN_C but mean will have to work
        IJ.run("adaptiveThr ", "using=Mean from="+ str(thresh_mean) +" then=0 output")
        # fill in the holes
        IJ.run("Fill Holes")
        # remove objects that are too small in area
        IJ.run("Gray Scale Attribute Filtering", "operation=Opening attribute=Area minimum="+ str(min_area_size) +" connectivity=8")
        # add the ROIs to the manager
        IJ.run("Create Selection")
        RM.addRoi(imp.getRoi())
        # From here the user can add / remove ROIs
        # if not they can split the big ROIs
        # then measue the ROIs values on the 


