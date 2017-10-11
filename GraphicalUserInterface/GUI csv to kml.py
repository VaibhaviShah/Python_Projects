import pandas
import tkinter
from tkinter.filedialog import askopenfilename
import simplekml

def browseCSV():
    global infile
    infile = askopenfilename()

def kmlFunction(outfile="D:\IntelliJ Projects\GraphicalUserInterface\sampleMarker.kml"):
    df = pandas.read_csv(infile)
    kml=simplekml.Kml()
    for long, lat in zip(df['Longitude'], df['Latitude']):
        kml.newpoint(coords=[(long, lat)])
    kml.save(outfile)

root = tkinter.Tk()
root.title("KML Generator")
label = tkinter.Label(root, text='This program generates a KML File')
label.pack()
browseButton = tkinter.Button(root, text='Browse', command=browseCSV)
browseButton.pack()
kmlButton = tkinter.Button(root, text='Generate KML', command=kmlFunction)
kmlButton.pack()
root.mainloop()