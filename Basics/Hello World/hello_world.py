#
# Example file for HelloWorld
#
#Defines a function of main, which has one line to print, hello world
#Function within python are defined as so, python is reliant on correct indentation, and uses this in place of 
#brackets. The scope block here is defined by the tab once, and the begingin of the scope is defined by the colon.
def main():
    print("Hello World")


#Here we want to test and make use of the above defined function. To do this we will do a simply if statement
#This if statement uses the variable name. This is what the complier calls the file dependent on the manner in which it was called.
#As we carry out the exeuection of this file, from this file alone. It will be defined as main. The following if 
# statement confirms this and the runs the following function i.e. the earlier defined Main function 
# these lines become used as interesting or valuable points which distingusihing in which manor the function/python program was called.
# if the python file was called as a library/additional file, we may want only certain functions avaiable. If called as the main function
# either by opening the file and running it in debugger, or callng it from command line, we may have an intro function to run of sorts
#ie hello world on main. This is the difference of the python file, being used as an additional library or file, or as a program 
if __name__ == "__main__":
    main()
