Arcpy_Cursors
=============

####How to Use

Each of these scripts contains one of the cursors available from the arcpy site package. The script will only find the file geodatabase if you have the script and the .gdb file in the same directory.


###Documentation

Search Cursor: http://resources.arcgis.com/en/help/main/10.2/index.html#/SearchCursor/018w00000011000000/

Insert Cursor: http://resources.arcgis.com/en/help/main/10.2/index.html#/InsertCursor/018w0000000t000000/

Update Cursor: http://resources.arcgis.com/en/help/main/10.2/index.html#/UpdateCursor/018w00000014000000/


###Challenges

**1**. Try running the insert cursor script before the update cursor script. What changed in the attribute table after running the insert cursor? What changed in the attribute table after running the update cursor?

**2.** Write your own code using the scripts provided as guidance. Create a script which searches for the really scary animals in the attribute table, and puts an exclamation mark after the animal-type if that animal is particularly scary. *Hint*: you'll have to nest one cursor inside another!
