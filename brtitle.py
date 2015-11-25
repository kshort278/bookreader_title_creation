#!/usr/bin/env python

#This program was written to create new BookReader files and title pages for the William K. Everson Collection website.
#It is project-specific and will not run correctly without template files.
#It uses template files and writes the new information to a new file created by the program.
#Each title will have 3 files: a BookReader HTML file, a BookReader JavaScript File, and a PHP title page
#Most of the variables in the functions are entered by the user when the program runs.
#The program only writes new lines for variables that are unique to each presskit.
#The program finds the correct line to write each variable too, then generates a new file.
#The functions are makeHtmlFile, makeBR, makeTitle, user_input, and the main function.
#Author: Kathy Short
#Version: 1.1


#function to create new html files for the BookReader for each title
#takes two parameters, the file name and the film name
#the file name is usually the film title without spaces or capitalization.
def makeHtmlFile(file, film):
    
    #import linecache module to get specific line numbers in a file
    import linecache
    
    #the source file is the template html file
    source_file = "temp.html"
    
    #the target file is an index.html file in the film title directory
    target_file = file+'/index.html'

    #reads source_file
    s = open(source_file, 'r')
    
    #writes to target_file
    t = open(target_file, 'w')

    
    #set count to zero
    #counter will keep track of lines written to new file
    count = 0

    #for each line in the source_file, do this:
    for line in s:
        
        #finds the line containing the title tag in the head of the HTML file
        if '<title>'in line:
            
            #rewrites the line to include the film title 'BookReader' using the film parameter based on user_input
            line = '\t<title>'+film+' BookReader</title>\n'
            t.write(line)
            
            #add to line count
            count+=1
            
        #if the line doesn't contain the title tag, find line 33   
        elif line == linecache.getline(source_file, 33):
            
            #write link to javascript file to line 33 in s using the file paramter based on user_input
            line = '<script type="text/javascript" src="'+file+'.js"></script>\n'
            t.write(line)
            
            #add to line count
            count+=1
            
        #keeps all other lines the same and writes them to target_file
        else:
            t.write(line)
            
            #add to line count
            count+=1
            
    #close both files           
    s.close()
    t.close()
    
    #print the number of lines printed to the target_file using the count variable
    print("%d LINES PRINTED TO %s. " % (count,target_file))
   
#function to create JavaScript files for the BookReader for each title
#takes five parameters, the image width, image height, number of pages, file name, and film name
def makeBR(img_width, img_height, num_pages, file_name, film_name):

    #import linecache module to get specific line numbers
    import linecache

    #the source file is a template js file
    source_file = "temp.js"

    #the target file is the film specific js file written to the film directory
    target_file = file_name+'/'+file_name+'.js'

    #reads source file
    s = open(source_file, 'r')

    #writes to target file
    t = open(target_file, 'w')
    
    #set count to zero
    count = 0

    #for each line in the source_file, do this:
    for line in s:

        #finds line 11 in the source_file
        if line == linecache.getline(source_file, 11):

            #rewrites line 11 using img_width parameter based on user_input
            line = '\treturn '+img_width+";\n"
            t.write(line)

            #add to line count
            count+=1

        #finds line 16 in the source_file    
        elif line == linecache.getline(source_file, 16):

            #rewrites line 16 to include img_height parameter based on user_input
            line = '\treturn '+img_height+";\n"
            t.write(line)

            #add line to count
            count+=1

        #finds line 29 in the source_file
        elif line == linecache.getline(source_file, 29):

            #writes line to include file_name to find each title's images based on user_input
            line = "\tvar url = 'http://www.nyu.edu/projects/wke/press/images/"+file_name+"/page'+leafStr.replace(re, imgStr) + '.jpg';\n"
            t.write(line)

            #add line to count
            count+=1

        #finds line 82 in the source_file    
        elif line == linecache.getline(source_file, 82):

            #writes line 82 to include number of pages parameter based on user_input
            line = "br.numLeafs = '"+num_pages+"';\n"
            t.write(line)

            #add line to count
            count+=1

        #finds line 86 in the source_file    
        elif line == linecache.getline(source_file, 86):

            #writes line 86 to include film name parameter based on user_input
            line = "br.bookTitle= '"+film_name+"';\n"
            t.write(line)

            #add line to count
            count+=1

        #finds line 88 in the source_file
        elif line == linecache.getline(source_file, 88):

            #writes line 88 to include file_name parameter based on user_input
            line = "br.bookUrl  = 'http://www.nyu.edu/projects/wke/press/titles/"+file_name+".php';\n"
            t.write(line)

            #add line to count
            count+=1

        #write all other lines of the source_file to the target_file as is
        else:
            t.write(line)

            #add each line to count
            count+=1

    #close source_file and target_file
    s.close()
    t.close()

    #print the number of lines written to the target_file using the count variable
    print("%d LINES PRINTED TO %s. " % (count,target_file))

#function to create title pages using PHP
#takes four parameters, the file name, the film title, the film director, and the film year
#each title page provides film info and links to the presskit in several different formats including PDF, JPG/HTML, and BookReader
def makeTitle(file_name, film_name, director, year):

    #concatenates film director and year and stores it in the variable film_info
    film_info = ' ('+director+', '+year+')'

    #concatenates file_name variable in link to Bookreader file and stores it in book_link variable
    book_link = '<a href="../BookReader/'+file_name+'/index.html">BookReader format</a><br>\n'

    #concatenates file_name variable in link to PDF file and stores it in PDF_link variable
    pdf_link = '<a href="../'+file_name+'/'+file_name+'.pdf">PDF format</a></p>\n'

    #files that contain includes for navigation and footer content stored in PHP files
    #the navigation file is stored in the top_file variable
    top_file = "top.php"

    #the footer file is stored in the bottom_file variable
    bottom_file = "bot.php"

    #creates a film title page in the titles directory and stores it as the target_file variable
    target_file = "titles/"+file_name+".php"

    #variable to read top_file
    top = open(top_file, 'r')

    #variable to read bottom_file
    bot = open(bottom_file, 'r')

    #variable to write to target_file
    t  = open(target_file,'w')

    #set line count to zero
    count = 0

    #for each line in top_file:
    for line in top:

        #if line contains HTML title tag, write film_name variable to title line
        if '<title>'in line:
            line = '\t<title>Press Kits - '+film_name+'</title>\n'
            t.write(line)
            
        #else, write all other lines in the file as is
        else:
            t.write(line)
        #add each line to count
        count+=1

    #close top_file
    top.close()

    #concatenate Film Title line and store as line_one variable
    line_one = '<p>&nbsp;</p>\n<h3 class="headings">Film Title: '+film_name+film_info+'</h3>\n'

    #concatenate Formats line and store as line_two variable
    line_two = '<p><em>Available Formats</em><br>\n'+book_link+pdf_link+'<p>&nbsp;</p>\n'

    #concatenate line_one and line_two variables and store as new_text variable
    new_text= line_one+line_two

    #write new text to target_file
    t.write(new_text)

    #for each line in the bottom_file, write line to target_file       
    for line in bot:
        t.write(line)

        #add each line to count
        count+=1
        
    #close bottom_file and target_file
    bot.close()
    t.close()

    #print number of lines printed to target_file using the count variable
    print("%d LINES PRINTED TO %s. " % (count,target_file))


#called by main function
#where user inputs all the information for each title
def user_input():
    #import os module to get file path and make a new directory
    import os

    #import sys module to quit program
    import sys

    #user inputs the name  of the file and it is stored in the file_title variable
    file_title = input('Enter the name of the file : ')

    #if the user types exit, the program will quit
    if file_title == 'exit':
        sys.exit(0)

    #if the user types in anything besides 'exit', then:    
    else:

        #if the file path for the title doesn't exist, then make a directory for the title
        if not os.path.exists(file_title):
            os.makedirs(file_title)

            
        #user inputs the name of the film and it is stored in the film_title variable
        #the file_title and film_title are usually the same
        #except that the file_title is written in all lowercase, no spaces
        #the film_title is capitalized with spaces since it will be written to the page that the site users will see
        film_title = input('Enter the name of the film as it should be written on title page: ')

        #if the user types exit, the program will quit
        if film_title == 'exit':
            sys.exit(0)
            
        #else, the program continues    
        else:

            #user inputs the name of the director and it is stored in the film_director variable
            film_director = input('Enter the name of the director: ')

            #if the user types exit, the program will quit
            if film_director == 'exit':
                sys.exit(0)

            #else, the program continues    
            else:

                #user inputs the year the film was made and it is stored in the film_year variable
                film_year = input('Enter the year: ')

                #if the user types exit, the program will quit
                if film_year == 'exit':
                    sys.exit(0)

                #else, the program continues    
                else:

                    #user inputs an approximate average image width of all the images in the presskit and it is stored in the width variable
                    width = input('Enter image width: ')

                    #if the user types exit, the program will quit
                    if width == 'exit':
                        sys.exit(0)

                    #else the program continues    
                    else:

                        #user inputs an approximate average image height of all the images in the presskit and it is stored in the height variable
                        height = input('Enter image height: ')

                        #if the user types exit, the program will quit
                        if height == 'exit':
                            sys.exit(0)

                        #else the program continues
                        else:

                            #user inputs the number of pages in the press kit and it is stored in the pages variable
                            pages = input('Enter the number of pages in the press kit: ')

                            #if the user types exit, the program will quit
                            if pages == 'exit':
                                sys.exit(0)

    #calls the makeHTMLFile function with file_title, film_title as arguments                              
    makeHtmlFile(file_title, film_title)

    #calls the makeBR function with width, height, pages, file_title, and film_title as arguments
    makeBR(width, height, pages, file_title, film_title)

    #calls the makeTitle function with file_title, film_title, film_director, and film_year as arguments
    makeTitle(file_title, film_title, film_director, film_year)
    

#main function of program
#first function called
def main():

    #first line printed when program runs
    #states purpose of program and how to quit
    print('This program will create title pages and BookReader files for the William K. Everson press kit collection. Type exit to quit.')

    #calls the user_input function
    user_input()

    #after running through the program, it calls the main function again so that the user can enter a new title
    #stops when user quits program
    main()
main()
