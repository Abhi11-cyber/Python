try:
 # Open the file "abhi1st_threshold.py" for reading
 f = open("GC.threshold.py", "r")
 
 # Read the contents of the file
 contents = f.read()
 
 # Close the file
 f.close()
 
 # Print the contents of the file
 print(contents)
 
except FileNotFoundError:
 print("Error: The file 'test.txt' does not exist.")
 
except:
 print("An error occurred.")