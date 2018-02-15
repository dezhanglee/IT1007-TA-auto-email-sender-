import csv

#read from a csv with multiple columns,
#first column is key, the rest is the content.


def read_csv(csvfilename):
    
    dct={} #to store the dict entries
    
    with open(csvfilename) as csvfile:
        
        file_reader = csv.reader(csvfile)
        
        for row in file_reader:
            
            dct[row[0]]=row[1:]
            
    return dct

#De Zhang - 1/9/2017 
