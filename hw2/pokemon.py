import csv
total = 0
count = 0

with open('pokemon1.txt','w') as outfile:
    with open("pokemonTrain.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # the below statement will skip the first row
        next(csv_reader)
        for lines in csv_reader:
            total+=1
            if(float(lines[2])>=40.0 and lines[4]=='fire'): 
                count+=1
        ans = "Percentage of fire type pokemon at or above level 40 = %d" % (round(100*(count/total)))
        outfile.write(ans)
        
with open('pokemonResult.csv','w',newline='') as csvfile:  
    writer = csv.writer(csvfile, delimiter=',')          
   
    with open('pokemonTrain.csv') as irisfile:
        
        reader = csv.reader(irisfile)
        
        row = next(reader)                               
        writer.writerow(row)                             
        
        for lines in reader:
            if(lines[4]=='NaN'):
                if(lines[5]=='fighting'):
                    lines[4]='normal'
                if(lines[5]=='water'):
                    lines[4]='fire'
                if(lines[5]=='flying'):
                    lines[4]='fighting'
                if(lines[5]=='fire'):
                    lines[4]='grass'
            writer.writerow(lines)
        
        
with open('pokemonResult.csv','w',newline='') as csvfile:  
    writer = csv.writer(csvfile, delimiter=',')          
   
    with open('pokemonTrain.csv') as irisfile:
        
        reader = csv.reader(irisfile)
        
        row = next(reader)                               
        writer.writerow(row)                             
        
        for lines in reader:
            if(float(lines[2])>40):
                if(lines[6]=='NaN'):
                    lines[6]='69.2'
                if(lines[7]=='NaN'):
                    lines[7]='86.3'
                if(lines[8]=='NaN'):
                    lines[8]='79.5'
            if(float(lines[2])<=40):
                if(lines[6]=='NaN'):
                    lines[6]='69.4'
                if(lines[7]=='NaN'):
                    lines[7]='87.0'
                if(lines[8]=='NaN'):
                    lines[8]='77.1'
                
            writer.writerow(lines)
        
        
from collections import OrderedDict
ansDict = {}

with open('pokemon4.txt','w',newline='') as csvfile:  
    writer = csv.writer(csvfile, delimiter=',')          
   
    with open('pokemonTrain.csv') as irisfile:
        
        reader = csv.reader(irisfile)
        
        row = next(reader)                                                           
        
        for lines in reader:
            typee = lines[4]
            if(typee=='NaN'):
                continue
            personality = lines[3]
            if (typee not in ansDict):
                ansDict[typee] = []
            typeList = ansDict.get(typee)
            if(personality not in typeList): 
                typeList.append(personality)
                typeList.sort()
        ordDict = OrderedDict(sorted(ansDict.items()))
        
        writer.writerow(["Pokemon type to personality mapping:"])
        writer.writerow([])
        for key in ordDict: 
            outrow = []
            outrow.append(key + ": ")
            for value in ordDict[key]:
                outrow.append(value + " ")
            writer.writerow(outrow)
            
            
totall = 0
countt = 0

with open('pokemon5.txt','w') as outfile:
    with open("pokemonTrain.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # the below statement will skip the first row
        next(csv_reader)
        for lines in csv_reader:
            if(float(lines[9])==3.0 and lines[8]!='NaN'): 
                print(lines[8],lines[9])
                countt+=1
                totall+=float(lines[8])
        ans = "Average hit point for pokemon of stage 3.0 = %d" % (round((totall/countt)))
        outfile.write(ans)