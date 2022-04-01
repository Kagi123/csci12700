#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: April 1, 2022
#asks the user for the name of a CSV file, name of the output file, and creates a map with markers for all the traffic collisions from the input file.

import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

mapCUNY.save(outfile='nycMap.html')
