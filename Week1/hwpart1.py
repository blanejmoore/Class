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
	
def gridrow():
    gridmidcountleft = 0
    gridmidcountright = 0
    
    gridrowleft()
    while gridmidcountleft < 4:
        gridrowmid()
        gridmidcountleft += 1
    gridrowleft()
    while gridmidcountright < 4:
        gridrowmid()
        gridmidcountright += 1
    gridrowright()

def gridcolumn():
    gridcolumnmidprint = 4
    gridcolumnmidcountleft = 0
    gridcolumnmidcountright = 0
    
    gridcolumnleft()
    while gridcolumnmidcountleft < 4:
        gridcolumnmid()
        gridcolumnmidcountleft += 1
    gridcolumnleft()
    while gridcolumnmidcountright < 4:
        gridcolumnmid()
        gridcolumnmidcountright += 1
    gridcolumnright()
    
def grid():
    gridtoplength = 0
    gridbotlength = 0
    gridrow()
    while gridtoplength < 4:
        gridcolumn()
        gridtoplength += 1
    while gridbotlength < 4:
        gridcolumn()
        gridbotlength += 1
    gridrow()

grid()    
