import numpy as np
import pandas as pd

def parse_violations(df):
    
    dfv = df[["Inspection ID","License #","Violations","Results"]]
    dfv = dfv.dropna()
    split_v = dfv['Violations'].str.split("|",expand=True)
    
    for c in split_v.columns:
        colname = "Violation_"+str(c)
        dfv[colname] = split_v[split_v.columns[c]]
    dfv = dfv.drop(columns='Violations')
    
    ID_col = dfv.columns.get_loc("Inspection ID")
    Lic_col = dfv.columns.get_loc("License #")
    res_col = dfv.columns.get_loc("Results")
    Vio_strt_col = dfv.columns.get_loc("Violation_0")
    
    rows={"Inspection ID":[], "License #":[], "Results":[], "Violation":[]}

    for x in range(0,len(dfv)):
        insp, lic, res = dfv.iat[x,ID_col],dfv.iat[x,Lic_col], dfv.iat[x,res_col]
        violations = dfv.iloc[x,Vio_strt_col:list(np.where(np.array(dfv.iloc[x,Vio_strt_col:])!=None)[0]+4)[-1]]
        
        for v in violations:
            rows['Inspection ID'].append(insp)
            rows['License #'].append(lic)
            rows['Results'].append(res)
            rows['Violation'].append(v)
            
        if x%10000==0:
            print(x, "/", len(dfv))
            
    dff = pd.DataFrame(rows)
    vios = newdf['Violation'].str.split(".", n=1, expand=True)
    dff['Violation #']=vios[0]
    dff['Violation Desc']=vios[1]
    dff['Comments'] = dff['Violation'].map(lambda x: x.split("- Comments:")[1])
    dff = dff.drop(columns='Violation')
    return dff

    df = pd.read_csv("../data/Food_Inspections.csv")
    dff = parse_violations(df)
    #dff.to_csv("Violations_Parsed.csv",index=False)