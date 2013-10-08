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
    	
def gridrow(s):
    gridmidcountleft = 0
    gridmidcountright = 0
    if s <= 0:
        print "Nice Try.  You can't have a grid less than or equal to 0"
    elif s == 1:
        gridrowleft()
    elif s == 2:
        gridrowleft()
        gridrowright()
    elif s > 2 and s % 2 == 0:
        gridrowleft()
        while gridmidcountleft < s-2:
            gridrowmid()
            gridmidcountleft += 1
        gridrowright()
    else:
        gridrowleft()
        while gridmidcountleft < s/2-1:
            gridrowmid()
            gridmidcountleft += 1
        gridrowleft()
        while gridmidcountright < s/2-1:
            gridrowmid()
            gridmidcountright += 1
        gridrowright()	

def gridcolumn(s):
    gridcolumnmidcountleft = 0
    gridcolumnmidcountright = 0
    if s <= 0:
        print "Nice Try.  You can't have a grid less than or equal to 0"
    elif s == 1:
        gridcolumnleft()
    elif s == 2:
        gridcolumnleft()
        gridcolumnright()
    elif s > 2 and s % 2 == 0:
        gridcolumnleft()
        while gridcolumnmidcountleft < s-2:
            gridcolumnmid()
            gridcolumnmidcountleft += 1
        gridcolumnright()
    else:
        gridcolumnleft()
        while gridcolumnmidcountleft < s/2-1:
            gridcolumnmid()
            gridcolumnmidcountleft += 1
        gridcolumnleft()
        while gridcolumnmidcountright < s/2-1:
            gridcolumnmid()
            gridcolumnmidcountright += 1
        gridcolumnright()
   
def print_grid(s):
    gridtoplength = 0
    gridbotlength = 0
    if s <= 0:
        print "Nice Try.  You can't have a grid less than or equal to 0"
    elif s == 1:
        gridrow(s)
    elif s == 2:
        gridrow(s)
        gridrow(s)
    elif s > 2 and s % 2 == 0:
        gridrow(s)
        while gridtoplength < s/2-1:
            gridcolumn(s)
            gridtoplength += 1
        while gridbotlength < s/2-2:
            gridcolumn(s)
            gridbotlength += 1
        gridrow(s)
    else:
        gridrow(s)
        while gridtoplength < s/2-1:
            gridcolumn(s)
            gridtoplength += 1
        gridrow(s)
        while gridbotlength < s/2-1:
            gridcolumn(s)
            gridbotlength += 1
        gridrow(s)

print_grid(10)    

