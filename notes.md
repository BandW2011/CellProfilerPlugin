# Notes
## To-Do:
1. ~~Put prefix into its own column~~
2. ~~Break up filename into these variables: u, v, j, x, y, each variable gets its own column~~
3. Input to spreadsheet (A1 to UV)
    
    * Get origin of user's input data as a field and get size of plate
    * Convert aplhanumeric user coords to UV coords
    * Get rows from coords in user spreadsheet and input them into the Image.csv
    * User spreadsheet should be in the format of a table with a format, or use loose format
    * Be able to say which cells get each compund, get the platemap
    * input a stock value if an error occurs
    * ignore extraneous data
    * rigid fields are wellid, contents, concentration, platetype, and actualwells
    * well coords, contents of that well, concentration, size of plate in wells, and actual number of wells
    * user friendly

---
constant format until after cXX  
CXX.ome.tif, cXX--XXX.ome.tif, CXX--XXX.ome.tif  
plotly? 5d data

---
Goal:
* Add features to the ExportToSpreadsheetPlus module
* Make it so that the user can input a spreadsheet (preferably a .csv file) into the module
* The spreadsheet should be made by the user, and should have a well coordinate (Alphanumeric), and information about the contents of the well
* Preferably, the columns should be wellid (coordinates), contents of the well, concentration, number of wells, and number of used wells
* The format of this spreadsheet has not been currently decided
* Should be user friendly
* The module will get the information from each wellid, convert it into MatrixScreen coords (U and V), and insert it into the Images.csv
