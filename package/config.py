#config.py file

import google_connect.py
import csv_creation.py

#Requires Python 3

#You will need to obtain a Google Secrets file as a json file. Please place this in the Tokens folder.
#It is best practice to use a service Google account
#Directions on obtaining that file can be found at http://pbpython.com/pandas-google-forms-part1.html

#These lines import some spreadsheets from Google that are imported from Skyward each day.
#The imports first get a student list and then a staff list and then removed duplicates
#The two dataframes are then combined into one so that any lookups of the student user_id can be made from one dataframe
canvasStudentImport = importSheet("1801Student")
canvasStudentImport.drop_duplicates(inplace = True)
canvasStudentIndexed = canvasStudentImport.set_index(['login_id'])

canvasStaffImport = importSheet("1801Staff")
canvasStaffImport.drop_duplicates(inplace = True)
canvasStaffIndexed = canvasStaffImport.set_index(['login_id'])



canvasStaffandStudentsIndexed = pd.concat([canvasStudentIndexed, canvasStaffIndexed], axis=0)