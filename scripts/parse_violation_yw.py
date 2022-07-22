import numpy as np
import pandas as pd

# @BEGIN parse_violations

# @IN food_inspections_data
# @OUT parsed_violations 


def parse_violations(df):
    
    # @BEGIN subset_data @DESC Drop NA and Split on Pipe
    # @IN data @AS food_inspections_data
    # @OUT out1 @AS subset
    # @CALL dropna
    # @CALL split("|")
    dfv = df[["Inspection ID","License #","Violations","Results"]]
    dfv = dfv.dropna()
    split_v = dfv['Violations'].str.split("|",expand=True)

    for c in split_v.columns:
        colname = "Violation_"+str(c)
        dfv[colname] = split_v[split_v.columns[c]]
    dfv = dfv.drop(columns='Violations')
    # @END subset_data

    ID_col = dfv.columns.get_loc("Inspection ID")
    Lic_col = dfv.columns.get_loc("License #")
    res_col = dfv.columns.get_loc("Results")
    Vio_strt_col = dfv.columns.get_loc("Violation_0")
    
    # @BEGIN Indexing_Loop @DESC Create Dict of Violations per Inspection_ID
    # @IN data @AS subset
    # @OUT out2 @AS indexed_dict
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
            
    # @END Indexing_Loop

    # @BEGIN dict_to_dataframe @DESC Dict to DF with Comments Split
    # @IN data @AS indexed_dict
    # @OUT out3 @AS parsed_violations
    dff = pd.DataFrame(rows)
    vios = dff['Violation'].str.split(".", n=1, expand=True)
    dff = dff.drop(columns='Violation')
    dff['Violation #']=vios[0].apply(lambda x: int(x.strip()))
    dff['Violation Desc']=vios[1].str.split("- Comments:", n=1, expand=True)[0].apply(lambda x: x.strip())
    dff['Comments']=vios[1].str.split("- Comments:", n=1, expand=True)[1].apply(lambda x: x.strip())
    
    return dff
    # @END dict_to_dataframe

# @END parse_violations