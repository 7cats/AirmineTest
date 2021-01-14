## Airmine test code task 
This is a program for Airmine test task1. It calculates the great circle distances between points.
This porjects includes the following files:
 1. this README.md  
2. places.csv  
3. task1.py  

### Requirement
- python ver3.8  
- package pandas  
- package math  
- package random  
- package decimal  

### Functions
##### calDist
This is the function for calculating the air distance between two location on the earth.  
Formula could be found [here](http://google.com)in https://en.wikipedia.org/wiki/Great-circle_distance#:~:text=The%20great%2Dcircle%20distance%2C%20orthodromic,line%20through%20the%20sphere's%20interior).

##### distDF
This is the function for calculating all distances between pairs of points using ***function calDist*** and stores all distances in a dataframe.

##### main
This is the main function which includes:
1. Take input **n**, if n is not provided, generate input.
2. Generate dataframe of distances and calculate the mean and closest pair.
3. Format the output

### Setup and use
1. Clone repository to local location
2. Run task1.py
Enter an integer after command line prompt: "Please enter an integer larger than 1:"  
If desired to use default dataset, enter anything else.
Program will generate output.
3. Output  
The output includes two parts.    
The first part is the distances between pairs of points. If a valid **n** is provided, random generated points' exact latitude and longitude will be used. Otherwise, the names of the location from places.csv are used.  
Rest of the output is the average distance of all pairs and the pair whose distance is the closest to the average.