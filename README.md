Arcticdatacrunch
Version 1.0
Language: Python
Lang vers: 3.11.5
May 18, 2024
Author: Tom Lutzenberger
Contact: lynxbot@gmail.com

This program, written in Python 3.11.5, is my first attempt at using python running comparisons on data over time. The program reads, loads, compiles and compares data
from three different sources and merges them together into a data visualization presentation (chart). Utilizing the calculation tools in common Python libraries,
as well as the ability to generate charts for the analyzed data, the program uses Arctic measurement data samples to run and operation for end user results.

Ideally, future enhancements will allow the user to identify the files to compare, pointing the program to them using an additional feature of user input on 
file identification. Ideally, that would be with a GUI screen versus a CLI input from the user, but both would work. Then the same calculations can take place, 
changing as the user provides the location of the data files to compare. The current version does not have this feature right now. It uses a specified location 
in the script to point the program to the data source.

To make this program work, one just needs to place the python file in the same location as the data files. The specified samples are provided. Note that the program
looks for columns labeled "year" and "value" in lower case. If you change the headers to something else, the program will crash, being unable to adjust for different
column headers than what is expected in the code. So it's better to just stick with the standard for now. Future versions might include an enhancement to deal with
this problem as well.

If the source files are in a different location, make sure to update the Python code address with the new location so it can find the files to crunch. I found in 
testing that confirming the name of the files in CLI helps confirm what they should be in the code. Otherwise, you will get an error in execution saying the program
can't find the file name expected.

SOURCE SAMPLES REFERENCE:

The source files used as samples are standardized version from the original ice index files created by the National Snow and Ice Data Center and 
located at: https://nsidc.org/data/g02135/versions/3

And from greenhouse gas measurements created by NOAA at: https://gml.noaa.gov/ccgg/trends/gl_data.html
