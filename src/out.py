
"""
Created by: Kaushal Mamgain
Information Retreival
"""

def output(r_data,sorted_val,recall_denom,n): #Function that gives the desired output
    print("FOR ",n," MOST RELEVANT DOCUMENTS")
    r=0
    sum_p = 0
    sum_r = 0
    for key,value in sorted_val.items():
        count = 1
        count_relevant=0
        
        for i in range(0,len(value)):
            if count>n:
                break
            count = count + 1
            d=value[i][0]
            name = int(d[-4:])
            if name in r_data[key]:         #check for common words
                count_relevant+=1
        print("Query ", key)
        print("Precision ",(count_relevant/n)," Recall ",count_relevant/recall_denom[r]) #calculate precision and recall
        sum_p = sum_p + count_relevant/n       #calculate the sum of precision for each query
        sum_r = sum_r + count_relevant/recall_denom[r]  #calculate sum of recall
        r+=1
    print("Average precision",sum_p/10)                 #Average the precision
    print("Average recall",sum_r/10)                    #Average the recall
