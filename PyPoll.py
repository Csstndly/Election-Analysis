import csv
import os

# Assign a variable for the file to load and the path. If file unknown os.path.join("Resources", "election_results.csv")
file_to_load = 'election_results.csv'

# Create a filename variable to a direct or indirect path to the file./Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)





# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
txt_file = open(file_to_save, "w")

#header
txt_file.write("Counties in the Election")

# Write three counties to the file. Use \n to put counties on different line
txt_file.write("\nArapahoe\nDenver\nJefferson ")

# Close the file.
election_data.close()
txt_file.close()

