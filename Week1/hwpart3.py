"""
Class: Python Certification Course - Intro to Python
Created By: Blane Moore
Created On: 10/2/2013
Description: Create a function that creates a grid using +, -, and | characters
"""

def gridrowleft():
    print '+',

def gridrowmid():
    print '-',

def gridrowright():
    print '+'

def gridcolumnleft():
    print "|",
	
def gridcolumnmid():
    print " ",
	
def gridcolumnright():
    print "|"
    	
def gridrow(r):
    gridmidcountleft = 0
    gridmidcountright = 0
    if r <= 0:
        print "Nice Try.  You can't have a grid less than or equal to 0"
    elif r == 1:
        gridrowleft()
    elif r == 2:
        gridrowleft()
        gridrowright()
    elif r > 2 and r % 2 == 0:
        gridrowleft()
        while gridmidcountleft < r-2:
            gridrowmid()
            gridmidcountleft += 1
        gridrowright()
    else:
        gridrowleft()
        while gridmidcountleft < r/2-1:
            gridrowmid()
            gridmidcountleft += 1
        gridrowleft()
        while gridmidcountright < r/2-1:
            gridrowmid()
            gridmidcountright += 1
        gridrowright()	

def gridcolumn(c):
    gridcolumnmidcountleft = 0
    gridcolumnmidcountright = 0
    if c <= 0:
        print "Nice Try.  You can't have a grid less than or equal to 0"
    elif c == 1:
        gridcolumnleft()
    elif c == 2:
        gridcolumnleft()
        gridcolumnright()

    else:
        gridcolumnleft()
        while gridcolumnmidcountleft < c/2-1:
            gridcolumnmid()
            gridcolumnmidcountleft += 1
        gridcolumnleft()
        while gridcolumnmidcountright < c/2-1:
            gridcolumnmid()
            gridcolumnmidcountright += 1
        gridcolumnright()
   
def print_grid(r,c):
    gridtoplength = 0
    gridbotlength = 0
    if r <= 0 or c <=0 :
        print "Nice Try.  You can't have a grid less than or equal to 0"
    elif r == 1 and c == 1:
        gridrow(r)
    elif(r > 1 and c == 1):
        gridrow(r)
        gridcolumn(c)
    elif(r == 1 and c > 1):
        gridrow(r)
        gridcolumn(c)
    elif r == 2 or c == 2:
        gridrow(r)
        gridrow(r)
    elif (r == 2 and c > 2) or (r > 2 and c == 2):
        gridrow(r)
        gridcolumn(c)
    else: 
        gridrow(r)
        while gridtoplength < r/2-1:
            gridcolumn(c)
            gridtoplength += 1
        gridrow(r)
        while gridbotlength < r/2-1:
            gridcolumn(c)
            gridbotlength += 1
        gridrow(r)
    """
    else:
        gridrow(r)
        while gridtoplength < c/2-1:
            gridcolumn(c)
            gridtoplength += 1
        gridrow(r)
        while gridbotlength < c/2-1:
            gridcolumn(c)
            gridbotlength += 1
        gridrow(r)
    """


print_grid(9,7)


