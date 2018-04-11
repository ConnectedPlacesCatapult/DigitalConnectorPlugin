# Tombolo Digital Connector QGIS plugin
A plugin for viewing, modifying and running Tombolo Digital Connector QGIS plugin. Tombolo Digital Connector is an open source software that allows automatic fetching, cleaning and combining spatial data from different sources and different specifications. For more information please visit [Digital Connector](https://github.com/FutureCitiesCatapult/TomboloDigitalConnector). 

Currently, the Digital Connector QGIS plugin has the following functionalities:
* It allows the user to run pre-build recipes without interacting with the terminal window and loads back the resulting geojson
* It allows altering the existing recipes in a more intuitive way
* It allows saving the modified recipes in a seperate file
* It allows visualising the existing/modified recipes in a UML-based format

NOTE - This repo is under development. There may be bugs.

## Installation
Currently the plugin is not on QGIS Python Plugins Repository. To install it:
* Clone the repo in /your_path_to_qgis/.qgis2/python/plugins
* Compile the resources file using pyrcc4
```pyrcc4 resources.py resources.qrc ```
* Run the tests (``make test``)
* Test the plugin by enabling it in the QGIS plugin manager

## Usage
* Open QGIS and click on the plugin manager located on the toolbar

![Alt text](/img/1.png)

* In the popup window, type **Digital Connector Plugin** and enable the plugin by clicking on the checkbox next to it

![Alt text](/img/2.png)

* In the main plugin window, browse to the local copy of Tombolo Digital Connector by clicking ``...``

![Alt text](/img/3.png)

* All existing recipes in the Digital Connector's example folder will be loaded in a dropdown box

![Alt text](/img/5.png)

* Clicking the **View recipe** button will render the UML version of the recipe. This allows the user to explore how the different subjects/datasources/fields are linked together

![Alt text](/img/7.png)

* By clicking the **Edit recipe** button a popup window will appear the wraps the recipe's subjects/datasources/fields in dropdown boxes 

![Alt text](/img/8.png)

* Expanding this allows the user to directly edit the contents of the recipe. By clicking the **Save** button the recipe can be saved locally

![Alt text](/img/9.png)

* By clicking the **Run** button the Digital Connector's command ``gradle -runExport`` is invoked.  

![Alt text](/img/5.png)

* Once the process is complete, the output file will be loaded automatically in QGIS's Layer Panel  

![Alt text](/img/11.png)

## What's Next:

  * Investigate the feasibility of implementing collapsable widgets for the nested field structure
  * Further extent GUI
  * Print terminal info on execution window
  * ...

