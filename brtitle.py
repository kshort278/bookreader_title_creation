#!/usr/bin/env python

# This program was written to create new BookReader files and title pages for the William K. Everson Collection website.
# It is project-specific and will not run correctly without template files.
# It uses template files and writes the new information to a new file created by the program.
# Each title will have 3 files: a BookReader HTML file, a BookReader JavaScript File, and a PHP title page
# Most of the variables in the functions are entered by the user when the program runs.
# The program only writes new lines for variables that are unique to each presskit.
# The program finds the correct line to write each variable too, then generates a new file.
# The functions are makeHtmlFile, makeBR, makeTitle, user_input, and the main function.
# Author: Kathy Short
# Version: 0.1


# function to create new html files for the BookReader for each title
# takes two params: the file name and the film name
# the file name is usually the film title without spaces or capitalization.
def makeHtmlFile(file, film):
    
    import linecache
    
    source_file = "temp.html"    
    target_file = file+'/index.html'

    s = open(source_file, 'r')    
    t = open(target_file, 'w')
    count = 0

    for line in s:
        if '<title>'in line:
            line = '\t<title>'+film+' BookReader</title>\n'
            t.write(line)
            count+=1            
        elif line == linecache.getline(source_file, 33):            
            line = '<script type="text/javascript" src="'+file+'.js"></script>\n'
            t.write(line)
            count+=1            
        else:
            t.write(line)
            count+=1
            
    s.close()
    t.close()    
    print("%d LINES PRINTED TO %s. " % (count,target_file))
   
#function to create JS files for the BookReader for each title
#takes five params: image width, image height, number of pages, file name, and film name
def makeBR(img_width, img_height, num_pages, file_name, film_name):
    import linecache

    source_file = "temp.js"
    target_file = file_name+'/'+file_name+'.js'

    s = open(source_file, 'r')
    t = open(target_file, 'w')    
    count = 0

    for line in s:
        if line == linecache.getline(source_file, 11):
            line = '\treturn '+img_width+";\n"
            t.write(line)
            count+=1
        elif line == linecache.getline(source_file, 16):
            line = '\treturn '+img_height+";\n"
            t.write(line)
            count+=1
        elif line == linecache.getline(source_file, 29):
            line = "\tvar url = 'http://www.nyu.edu/projects/wke/press/images/"+file_name+"/page'+leafStr.replace(re, imgStr) + '.jpg';\n"
            t.write(line)
            count+=1
        elif line == linecache.getline(source_file, 82):
            line = "br.numLeafs = '"+num_pages+"';\n"
            t.write(line)
            count+=1
        elif line == linecache.getline(source_file, 86):
            line = "br.bookTitle= '"+film_name+"';\n"
            t.write(line)
            count+=1
        elif line == linecache.getline(source_file, 88):
            line = "br.bookUrl  = 'http://www.nyu.edu/projects/wke/press/titles/"+file_name+".php';\n"
            t.write(line)
            count+=1
        else:
            t.write(line)
            count+=1

    s.close()
    t.close()
    print("%d LINES PRINTED TO %s. " % (count,target_file))

#function to create title pages using PHP
#takes four params: the file name, the film title, the film director, and the film year
#each title page provides film info and links to the presskit in several formats
def makeTitle(file_name, film_name, director, year):
    film_info = ' ('+director+', '+year+')'
    book_link = '<a href="../BookReader/'+file_name+'/index.html">BookReader format</a><br>\n'
    pdf_link = '<a href="../'+file_name+'/'+file_name+'.pdf">PDF format</a></p>\n'
    top_file = "top.php"
    bottom_file = "bot.php"
    target_file = "titles/"+file_name+".php"

    top = open(top_file, 'r')
    bot = open(bottom_file, 'r')
    t  = open(target_file,'w')
    count = 0

    for line in top:
        if '<title>'in line:
            line = '\t<title>Press Kits - '+film_name+'</title>\n'
            t.write(line)            
        else:
            t.write(line)
        count+=1
        
    top.close()
    
    line_one = '<p>&nbsp;</p>\n<h3 class="headings">Film Title: '+film_name+film_info+'</h3>\n'
    line_two = '<p><em>Available Formats</em><br>\n'+book_link+pdf_link+'<p>&nbsp;</p>\n'
    new_text= line_one+line_two
    t.write(new_text)
    count+=2
    
    for line in bot:
        t.write(line)
        count+=1
        
    bot.close()
    t.close()
    print("%d LINES PRINTED TO %s. " % (count,target_file))


#called by main function
#where user inputs all the information for each title
def user_input():
    import os
    import sys

    file_title = input('Enter the name of the file : ')
    if file_title == 'exit':
        sys.exit(0)
    else:
        if not os.path.exists(file_title):
            os.makedirs(file_title)

            
        #user inputs the name of the film and it is stored in the film_title variable
        #the file_title and film_title are usually the same
        #except that the file_title is written in all lowercase, no spaces
        #the film_title is capitalized with spaces since it will be written to the page that the site users will see
        film_title = input('Enter the name of the film as it should be written on title page: ')

        if film_title == 'exit':
            sys.exit(0)            
        else:
            film_director = input('Enter the name of the director: ')
            if film_director == 'exit':
                sys.exit(0)  
            else:
                film_year = input('Enter the year: ')
                if film_year == 'exit':
                    sys.exit(0)
                else:
                    #approx average image width of all the images in the presskit 
                    width = input('Enter image width: ')
                    if width == 'exit':
                        sys.exit(0)
                    else:
                        #approx average image height of all the images in the presskit
                        height = input('Enter image height: ')
                        if height == 'exit':
                            sys.exit(0)
                        else:
                            pages = input('Enter the number of pages in the press kit: ')
                            if pages == 'exit':
                                sys.exit(0)

    makeHtmlFile(file_title, film_title)
    makeBR(width, height, pages, file_title, film_title)
    makeTitle(file_title, film_title, film_director, film_year)
    
def main():
    print('This program will create title pages and BookReader files for the William K. Everson press kit collection. Type exit to quit.')
    user_input()
    main()
main()
