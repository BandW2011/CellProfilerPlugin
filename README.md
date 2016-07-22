# CellProfilerPlugin

This is a plugin for CellProfiler. Just copy the files to your CellProfiler directory.

This plugin was developed for CellProfiler 2.2.0 rev e82cb3c.

Currently this plugin adds the module ExportToSpreadsheetPlus, which offers the choice to insert the filename prefix into the Image.csv file, and insert tokens from image filepath strings if the string follows this format:

*image--L0000--S00--U04--V00--J14--E01--O00--X00--Y00--T0000--Z00--C00.ome.tif*

So something like this is output to the Image.csv:
![alt text]("https://raw.githubusercontent.com/BandW2011/CellProfilerPlugin/master/img/spreadsheetA.png")
