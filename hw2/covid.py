import csv

with open('covidResult.csv','w',newline='') as csvfile:  
    writer = csv.writer(csvfile, delimiter=',')          
   
    with open('covidTrain.csv') as irisfile:
        
        reader = csv.reader(irisfile)
        
        row = next(reader)                               
        writer.writerow(row)                             
        
        for lines in reader:
            if '-' in lines[1]:
                first, second = lines[1].split('-')
                lines[1] = round((float(first)+float(second))/2)
            
            day, month, year = lines[8].split('.')
            lines[8] = month+"."+day+"."+year
            
            day2, month2, year2 = lines[9].split('.')
            lines[9] = month2+"."+day2+"."+year2
           
            day3, month3, year3 = lines[10].split('.')
            lines[10] = month3+"."+day3+"."+year3
            
            if(lines[6]=='NaN'):
                if(lines[4]=='Anhui'):
                    lines[6]=32.20
                if(lines[4]=='Beijing'):
                    lines[6]=39.92
                if(lines[4]=='Gansu'):
                    lines[6]=35.48
                if(lines[4]=='Guangdong'):
                    lines[6]=22.53
                if(lines[4]=='Guangxi'):
                    lines[6]=22.56
                if(lines[4]=='Guizhou'):
                    lines[6]=27.30
                if(lines[4]=='Hokkaido'):
                    lines[6]=43.09
                if(lines[4]=='Hong Kong'):
                    lines[6]=22.36
            
            if(lines[7]=='NaN'):
                if(lines[4]=='Anhui'):
                    lines[7]=117.10
                if(lines[4]=='Beijing'):
                    lines[7]=116.32
                if(lines[4]=='Gansu'):
                    lines[7]=104.92
                if(lines[4]=='Guangdong'):
                    lines[7]=114.00
                if(lines[4]=='Guangxi'):
                    lines[7]=108.41
                if(lines[4]=='Guizhou'):
                    lines[7]=107.14
                if(lines[4]=='Hokkaido'):
                    lines[7]=142.84
                if(lines[4]=='Hong Kong'):
                    lines[7]=114.16
                    
            if(lines[3]=="NaN"):
                if(lines[4]=='Aichi Prefecture'):
                    lines[3]='Nagoya City'
                if(lines[4]=='Anhui'):
                    lines[3]='Bozhou City'
                if(lines[4]=='Beijing'):
                    lines[3]='Shijingshan District'
                if(lines[4]=='Gansu'):
                    lines[3]='Chengguan District Lanzhou City'
                if(lines[4]=='Guangdong'):
                    lines[3]='Shehzhen City'
                if(lines[4]=='Guangxi'):
                    lines[3]='Fangchenggang'
                if(lines[4]=='Guizhou'):
                    lines[3]='Tongren City'
                if(lines[4]=='Hokkaido'):
                    lines[3]='Nakafurano'
                if(lines[4]=='Hong Kong'):
                    lines[3]='Hong Kong'
                    
            if(lines[11]=="NaN"):
                if(lines[4]=='Aichi Prefecture'):
                    lines[11]='fever'
                if(lines[4]=='Anhui'):
                    lines[11]='fever'
                if(lines[4]=='Beijing'):
                    lines[11]='fever'
                if(lines[4]=='Gansu'):
                    lines[11]='fever'
                if(lines[4]=='Guangdong'):
                    lines[11]='cough'
                if(lines[4]=='Guangxi'):
                    lines[11]='fever'
                if(lines[4]=='Guizhou'):
                    lines[11]='discomfort'
                if(lines[4]=='Hokkaido'):
                    lines[11]='fever'
                if(lines[4]=='Hong Kong'):
                    lines[11]='fever'
            print(lines[3],lines[4])
            writer.writerow(lines)