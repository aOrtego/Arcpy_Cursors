""" Demonstrate usage of the DA module's SearchCursor with a SQL statement. """

import os

import arcpy

## Parameters
feature_class = os.path.join(os.getcwd(), "Cursor Demo.gdb", "Animals")
field_names   = ["OID@", "AnimalName", "AnimalType"]
sql_statement = "ScarinessRank = 5"

## Search Cursor
with arcpy.da.SearchCursor(feature_class, field_names, sql_statement) as sc:
    print "The animals with a scariness rank of 5 are..."
    for row in sc:
        print "OID: {0}  -- {1} the {2}".format(*row)

