import simplekml
import pandas

df = pandas.read_csv("D:\IntelliJ Projects\GoogleEarthKML\sampleMarker.csv")

kml = simplekml.Kml()

for long, lat in zip(df["Longitude"], df["Latitude"]):
    kml.newpoint(coords=[(long, lat)])

kml.save("D:\IntelliJ Projects\GoogleEarthKML\sampleMarker.kml")




