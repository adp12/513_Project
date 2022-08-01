
import netCDF4
import numpy as np
from netCDF4 import ma
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import netCDF4
import numpy as np
from netCDF4 import ma
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# @BEGIN main


def main(db_pth = '.', fmodel = 'clm'):
   
    # @BEGIN Facility_Type
    
    # @IN g  @AS Food_Inspections
    # @OUT mask  @AS Leave_Only_Restaurants_in_Facility_Type_Column


    # @END Facility_Type
  

    # @BEGIN remove_rows_not_chicago
    
    # @IN mask  @AS Leave_Only_Restaurants_in_Facility_Type_Column
    # @OUT mask  @AS only_chicago_remains

    # @END remove_rows_not _chicago
    
 
    
    # @BEGIN trimcells
    
    # @IN mask  @AS only_chicago_remains
    # @OUT mask  @AS trimmedcells_Standard_restaurant_names

    # @END trimcells
   
    # @BEGIN 	Python_Integrity_Check_Keys
    # @IN mask  @AS trimmedcells_Standard_restaurant_names
    # @OUT mask  @AS Business_license_relation_check
    # @END date

    # @BEGIN 	Create_Table
    # @IN mask  @AS Business_license_relation_check
    # @OUT mask  @AS Restaurant_Table_Created
    # @END date

    # @BEGIN 	Inspection_Table
    # @IN mask  @AS Restaurant_Table_Created
    # @OUT mask  @AS Inspection_Table_Created
    # @END Inspection_Table
	
    # @BEGIN Subset_Violations
    
    # @IN g  @AS Food_Inspections
    # @OUT mask  @AS Expand_single_columns


    # @END Subset_Violations
	
   
    # @BEGIN Indexing_Violation
    
    # @IN g  @AS Expand_single_columns
    # @OUT mask  @AS Dict_violations

    # @END Indexing_Violations

    # @BEGIN Dataframe_violations
    
    # @IN g  @AS Dict_violations
    # @OUT mask  @AS Violaions_dF

    # @END Dataframe_violations
    # @BEGIN Violation_table
    
    # @IN g  @AS Violaions_dF
    # @OUT mask  @AS Violaions

    # @END Violation_table

    # @BEGIN Inspection_violations
    
    # @IN g  @AS Violaions_dF
    # @OUT mask  @AS Inspection_Details

    # @END Inspection_violations
# @END main