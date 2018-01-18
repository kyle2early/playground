import csv

##function to count types for each thermoplastic
plastics = list(csv.reader(open("plasticnews.csv_20180115_2032PM")))

def no_resins(commodity):
  count=0
  for row in plastics:
    if row[6]== commodity:
      count +=1
  return count

hdpe_count = no_resins("HDPE")
print("hdpe:", hdpe_count)
