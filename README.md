# CellProfilerPlugin

This is a plugin for CellProfiler. Just copy the plugins directory to your CellProfiler directory.

This plugin was developed for CellProfiler 2.2.0 rev e82cb3c.

Currently this plugin adds the module ExportToSpreadsheetPlus, which offers the choice to insert the filename prefix into the Image.csv file, and insert tokens from image filepath strings if the string follows the format that I believe is used by Matrix Screener:

*image--L0000--S00--U04--V00--J14--E01--O00--X00--Y00--T0000--Z00--C00.ome.tif*

The plugin:

![Uh Oh! The image isn't here!](https://raw.githubusercontent.com/BandW2011/CellProfilerPlugin/master/img/screenshotA.png "Yes, this is a screenshot!")

So something like this is output to the Image.csv:

![Uh Oh! The image isn't here!](https://raw.githubusercontent.com/BandW2011/CellProfilerPlugin/master/img/spreadsheetA.png "Yes, this is a spreadsheet!")
