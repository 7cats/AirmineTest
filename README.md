## Airmine test code task 
### Description
This is a program for Airmine test task1. It calculates the great circle distances between points.
### File list
1. this README.md
2. places.csv
3. task1.py

### Functions
##### calDist
This is the function for calculating the air distance between two location on the earth.
Formula could be found in https://en.wikipedia.org/wiki/Great-circle_distance#:~:text=The%20great%2Dcircle%20distance%2C%20orthodromic,line%20through%20the%20sphere's%20interior).

##### distDF
This is the function for calculating all distances between pairs of points using **function calDist** and stores all distances in a dataframe.

##### main
This is the main function which includes:
1. Take input n, if n is not provided, generate input.
2. Generate dataframe of distances and calculate the mean and closest pair.
3. Format the output

### Requirement
python ver3.8
packages pandas, math, random and decimal