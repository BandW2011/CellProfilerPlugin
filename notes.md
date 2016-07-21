# Notes

1. ~~Put prefix into its own column~~
2. Break up filename into these variables: u, v, j, x, y, each variable gets its own column
3. Match up matrixscreener coords into plate coords (A1 to UV)

* Prompt user for the begining coords, make sure it can correlate to the plate
* Alphanumeric is what is on the plates
* UV is how its referenced by CP
* Aspirin in each spot, give me the 5 wells that aspiriin is in
* Be able to say which cells get each compund, get the platemap
* MatrixScreen encodes UV
* The platemap wont give blanks


USER SETS OFFSET (BEGINNING AND RANGES), THIS WILL DETERMINE SIZE OF ACTUALWELL
LEARN HOW TO THROW ERRORS
MATCH AS WELL AS POSSIBLE, IGNORE ERRORS, PREVENT USERS FROM ENTERING TOO HIGH OF A NUMBER
IGNORE EXTRANEOUS DATA
stock value if errors, print text if that error occurs

constant fomrat until after cXX
CXX.ome.tif, cXX--XXX.ome.tif, CXX--XXX.ome.tif
plate coords, xy is uv
xy is position within well

get plate map from file address? "map to it using alphanumerals" matrixscreener?
edit export spreadsheet that has these things? in the same image csv would also be "fine with me"
wellid, contetns, concentration, platetype, actualwells:
A1,     aspirin,  10mM,          96,        32
5 columns, instruction sheet, make USER FRIENDLY
get the compound id in the easiest way possible

plotly? 5d data




GET HELP FROM DEVS OR SLACK

