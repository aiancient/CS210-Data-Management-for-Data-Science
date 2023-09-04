import csv
import re

for line in open("tfidf_docs.txt"):
    ans = line.split('.',1)[0]
    ansf = ans + 'result.txt'
    with open(ansf,'w',newline='') as csvfile:  
        writer = csv.writer(csvfile)          
   
        with open(line.strip()) as irisfile:
            
            reader = csv.reader(irisfile)
            
            for eachLine in reader:
                eachLine[0]
                re.sub(r"[^a-zA-Z0-9_]+"," ",eachLine[0])