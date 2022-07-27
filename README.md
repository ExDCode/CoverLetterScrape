# Cover Letter automation with Python, Excel and MS Word

1. Copy parent in DOM of the job posting from myExperience page that contains the tables into index.html file.
2. Run the python script, which will extract and update the excel table.
3. Open the Word document and all the information should be updated on launch (press yes to fetch some SQL to synch with the excel table). Template was made to print current date and all the info from the excel. Some info might be missing, and sometimes need t change Mr. to Ms., but it already saves so much time copy-pasting.

***
### Steps that led me to successfully finishing the project:

1. Figure out how **Content Control** works
```
-> you turn on the Dev Mode
    -> then add Text Content Control
    -> in properties define a tag and check 'multiple carriage'
    -> select the block and copy paste somewhere else (you can change properties to not show the content control box)
```
2. Add information from Excel through Mailing list in Word
3. Scrape information with Python and make an Excel file for Mailing list
(ended up not using Content Control at all, but still useful to know for templating purposes)
