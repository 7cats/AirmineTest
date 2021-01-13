# -*- coding: utf-8 -*-

"""
Airmine code test - Task 1
author: ZixinZhang
email: zhangzixin.dalian@gmail.com
date: 12/01/2021
"""
## Import packages
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import random, decimal

## calculation of distance between two points
def calDist(lat1 , lat2, lon1, lon2):
    diffLat = lat1 - lat2
    diffLon = lon1 - lon2
    r_earth = 6378.137 # earth radius
    distance = 2*asin(sqrt(sin(diffLat/2)**2 + cos(lat1) * cos(lat2) * sin(diffLon/2)**2))*r_earth
    distance = round(distance,2)
    return distance

## a DF that records distances
def distanceDF(places):
    ## from angle to radian
    radLat = list(map(radians, places.Latitude))
    radLon = list(map(radians, places.Longitude))
    ## calculation of distances between two points
    distDF = pd.DataFrame({'point1': [], 'point2': [], 'Distance': []})
    for i in range(len(radLat)): 
        for j in range(i + 1,len(radLat)):
            newDist = pd.DataFrame({'point1': [i], 'point2': [j],
                                   'Distance': [calDist(radLat[i], radLat[j], radLon[i], radLon[j])]})
            ## paste new distance
            distDF = pd.concat([distDF, newDist], ignore_index = True)
    ## Sort
    distDF = distDF.sort_values(by = 'Distance', ascending = True, ignore_index = True)
    return distDF
    
def main():
    ## Get input n. Check if it is integer
    print("Please enter an integer larger than 1: ")
    n = input()
    try:
        n = int(n)
        if n >= 1:
            print("{} points will be generated.".format(n))
        else:
            print("Integer is smaller than 1. Default datasource is used.")
            n = None
    except:
        # if input is not intege larger than 1, use places.csv data
        print("Input was not an integer number. Default datasource is used.")
        n = None

    random.seed(123) # set seed
    
    ## check if n is valid, if not, take places.csv as input
    if n is None:
        places = round(pd.read_csv("D:/Python/Airmine_Code_Test/Arimine/places.csv", sep = ','),2)
    else: 
    ## Yes, generate n ramdon points, round to 2 decimal
        places = {'Name':["Location{}".format(i) for i in range(1, n+1)],
             'Latitude':[decimal.Decimal(random.randrange(-9000,9000,1))/100 for i in range(1, n+1)],
             'Longitude':[decimal.Decimal(random.randrange(-18000,18000,1))/100 for i in range(1, n+1)]}
        places = pd.DataFrame(data = places)

    ## calculate the distance
    distDF = distanceDF(places)
    ## get mean and closest pair
    dist = distDF['Distance']
    distMean = distDF['Distance'].mean()
    distClosest = dist.iloc[(dist - distMean).abs().argsort()[:1]]
    
    ## format output    
    distOutput = pd.DataFrame({'Location_1': [], 'Location_2': [], 'Distance(km)': []})
    if n is None: # default dataset uses real location name
        for i in range(1, len(distDF)):
            newEntry = pd.DataFrame({
                'Location_1':[places.Name[distDF.point1[i]]],
                'Location_2':[places.Name[distDF.point2[i]]],
                'Distance(km)':[distDF.Distance[i]]})
            distOutput = pd.concat([distOutput, newEntry], ignore_index = True)
    else: # n from input uses lat&lon to show exact location
        for i in range(1, len(distDF)):
            newEntry = pd.DataFrame({
                'Location_1':["P({}, {})".format(places.Latitude[distDF.point1[i]], places.Longitude[distDF.point1[i]])],
                'Location_2':["P({}, {})".format(places.Latitude[distDF.point2[i]], places.Longitude[distDF.point2[i]])],
                'Distance(km)':[distDF.Distance[i]]})
            distOutput = pd.concat([distOutput, newEntry], ignore_index = True)
    ## print output
    print("Distances of pairs of points in ascending order:")
    print(distOutput.to_string(index = False))
    idPair = distClosest.index.astype(int)[0]
    distDF = distDF.values.tolist()
    print("Average Distance: {}km. Closest pair: point_{} - point_{} Distance: {}km".format(distMean, int(distDF[idPair][0]),int(distDF[idPair][1]),int(distDF[idPair][2])))
    return distOutput

if __name__ == "__main__":
    output = main()









