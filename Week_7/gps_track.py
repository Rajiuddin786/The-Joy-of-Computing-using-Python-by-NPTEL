import csv
import gmplot as gm


gmap = gm.GoogleMapPlotter(23.12345,55.123432,17)

gmap.coloricon = "https://www.googlemapsmarkers.com/v1/%s/"

with open('cooridinate.csv','r') as file:
    reader = csv.reader(file)
    k=0

    for row in reader:
        lat,log=float(row[0]),float(row[1])

        if k == 0:
            gmap.marker(lat,log,'yellow')
            k=1
        else:
            gmap.marker(lat,log,'blue')

gmap.marker(lat,log,'red')

gmap.draw("mymap.html")