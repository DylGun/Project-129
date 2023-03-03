import csv
import pandas as pd
data = []
data1 = []

with open("dwarf_stars.csv") as f:
    planet = csv.reader(f)
    for i in planet:
        data.append(i)

with open("bright_stars.csv") as f:
    bright = csv.reader(f)
    for i in bright:
        data1.append(i)

