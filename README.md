# Stain-Analysis-Plugin
Extract Calcium Stain and Astrocytes to quantify cell activity

### Installation:

Being that the `stain.py` is a Jython macro script, that can be executed by [Fiji](https://fiji.sc/), the only thing needed is to download the file and run it via the menu
`Plugins > Macros > Run >  Select stain.py`

To download the file, it can be downloaded with the github download button or through git via 
```sh
git clone https://github.com/ChrisDesigns/Stain-Analysis-Plugin
```

It is important that users do have the proper plugins to use this script, they can be found and added through Fiji's plugin manager. They are as follows:
- [adaptiveThreshold](https://sites.google.com/site/qingzongtseng/adaptivethreshold/)
- [3D ImageJ Suite](https://imagej.net/plugins/3d-imagej-suite/)



### Influcence:

The program was influence by [CaImAn](https://github.com/flatironinstitute/CaImAn), whose ROI extraction technique is closely resembled. It is import to note that this macro does not offer all the functionalities of this toolbox but rather only ROI extraction.


### Analysis:

To performace a light intensity analysis using the generated ROIs, you can keep them as one ROI or split them seperately. Then when you want to process them select them the ROI manaqger and right click "Multi Measue", this will allow for you  to measure in accordance to ROI in reference to each slice.
