import os
import csv

entries=os.listdir(r'C:\Users\lenovo\divided\val')
from datetime import date
today = date.today()
with open("attend.csv", "w",newline='') as csv_file:
    filewriter = csv.writer(csv_file, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Gr.No.',entries])
    filewriter.writerow([str(date.today()),p])
    #filewriter.writerow(output)    