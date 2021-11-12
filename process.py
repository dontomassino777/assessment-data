log_file = open("um-server-01.txt") #opens the data file to give us access to its data


def sales_reports(log_file): #creates a function called 'sales_reports' that takes in the data from 'um_server-01.text' as a parameter, stored as a variable 'log_file'
    for line in log_file: #loops through each line in the data stored in log_file
        line = line.rstrip() #makes a copy of each line with trailing characters removed, stored to the variable 'line'
        day = line[0:3] #grabs the characters of each line from index 0 to 3 and stores it to the variable 'day'.
        if day == "Mon": #conditional logic that checks whether those characters from 'day' are equal to 'Tue'
            print(line) #if they are, this line will print the line starting with characters 'Tue'


sales_reports(log_file) #calls the function 'sales_reports' with 'log_file' passed as argument
