#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: April 1, 2022
#asks the user for the name of a CSV file, name of the output file, and creates a map with markers for all the traffic collisions from the input file.

import folium
import pandas as pd

csvFile = input('Enter CSV file name: ')       
cuny = pd.read_csv(csvFile)

mapCUNY = folium.Map(location=[40.768731, -73.964915])

output_File= input('Enter output file: ')

for index,row in cuny.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)

mapCUNY.save(outfile= output_File)
