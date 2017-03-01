# README #
**Python Version- 3.5**
This script converts the Banner report that is currently output to the new format required by OCLC. Stop-gap until the new report style can be loaded into Banner. We are not pulling any new information, so it's mostly just to make sure the necessary fields are there. Also, it does checking to make sure we haven't duplicated barcodes or ids.

Use
===
Works off a CLI (command-line interface). The only argument is the path to the file gotten from Banner. The current setup is to have a **data** sub-directory where you can drop in the csv from Banner.

###Exampe Usage
\>\> python conversion.py 'data/opac\_students1.txt'

**Output**: A tsv file formatted for OCLC to send to the FTP server.

If either the barcode or idAtSource (essentially their student username) field is duplicated, it will not write the second one to the file and print out the ID that is in error. You can investigate the file to find what is causing the mixup and edit the script as needed to work around it.

###Example of error
Bob and Becky Hendrix both come to Westfield. Given naming conventions, there is a collision. So we use Bob's first initial in his username. I.E. bshendrix for Bob, bhendrix for Becky.

But an error occured in making the Banner file and both were listed as bhendrix. The tool would alert you that there is a problem with a bhendrix, and you can grep through the Banner and outputted CSVs to find what the error(s) are and account for them.