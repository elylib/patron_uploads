# README #
**Python Version- 3.5**
This script converts the Banner report or info from payroll that is currently output to the new format required by OCLC. We are not pulling any new information, so it's mostly just to make sure the necessary fields are there. Also, it does checking to make sure we haven't duplicated barcodes or ids, and translates the xlsx file to tsv without deleting leading zeros or mucking with dates.

You do not need to convert the files to tsv or anything before running this script. It assumes the file from Banner or payroll is an Excel file.

Use
===
Works off a CLI (command-line interface). The arguments are:

#### file_location
The path to the file. This path can be relative to the directory the script is running from (see below). This path can also be an absolute path.

#### fac_staff_or_students
Whether you are generating a report for students or faculty/staff. Acceptable values are _students_ or _faculty_

### Example Usage
`>> python conversion.py data/opac_students1.xlsx students`

**Output**: A tsv file formatted for OCLC to send to the FTP server.

If either the barcode or idAtSource (essentially their student username) field is duplicated, it will not write the second one to the file and print out the ID that is in error. You can investigate the file to find what is causing the mixup and edit the script as needed to work around it.

### Example of error
Bob and Becky Hendrix both come to Westfield. Given naming conventions, there is a collision. So we use Bob's first initial in his username. I.E. bshendrix for Bob, bhendrix for Becky.

But an error occured in making the Banner file and both were listed as bhendrix. The tool would alert you that there is a problem with a bhendrix, and you can grep through the Banner and outputted CSVs to find what the error(s) are and account for them.

These kind of errors are much more common with faculty and staff. That file does not have user IDs, so we generate a provisional one using the first letter of the given name and full family name. This leads to duplicates and occasional mistakes when someone has punctuation or a space in their last name. In these cases investigate the directory to get and correct the error.