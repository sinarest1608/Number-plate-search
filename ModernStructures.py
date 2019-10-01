'''
End of file for docs
This module helps formatting fetched data into pandas dataframe and json formats.
Dependencies : pandas, json
'''
import pandas as pd
import json
def makedf(s):
    l = s.split("\n")
    name = l[2]
    vehName = l[6]
    regNo = l[10]
    regDate = l[14]
    data = [['Name',name], ['Vehicle Name',vehName], ['Registration Number',regNo],['Registration date',regDate]]
    df = pd.DataFrame(data)
    return df

def makejson(s):
    l = s.split("\n")
    name = l[2]
    vehName = l[6]
    regNo = l[10]
    regDate = l[14]
    data = [['Name',name], ['Vehicle Name',vehName], ['Registration Number',regNo],['Registration date',regDate]]
    S = json.dumps(data)
    return S

'''
---------------------------------
1. To use : import ModernStructures
2. To invoke methods simple write ModernStructures.methodname(foo)
3. Store the return type in a compatible variable!
------------------------------------------------
Methods:
1. D = makedf(s)
Description : Takes a string s and processes it
to return a dataframe that is stored in D in this case.
---------------------------------
2. print(S)
Description : Takes a string s and processes it
to return a json object that is stored in S in this case.
---------------------------------
'''
