from changeToRst import *
import sys
import re
for i in range(1, len(sys.argv)):
    fileName = sys.argv[i]
    f = srcFile("C:\\Users\\benja\\Documents\\aptechWork\\rstProject\\ChangeSrcToRst\\"+fileName)
    f.makeRSTFiles()
    num = 0
    for fun in f.funList:
        fExp = open("C:\\Users\\benja\\Documents\\aptechWork\\rstProject\\ChangeSrcToRST\\expected\\"+fun.name+ ".rst", "r")
        output = ""
        curFun = -1
        num = num+1
        for x in fExp:
            output = output + x
        fExp.close()
        myF = open("C:\\Users\\benja\\Documents\\aptechWork\\rstProject\\ChangeSrcToRST\\output\\"+fun.name+".rst", "r")
        myOutput = ""
        for x in myF:
            myOutput = myOutput + x
        myF.close()
        if (output != myOutput):
            print(fun.name + " does not match")
            f = open("C:\\Users\\benja\\Documents\\aptechWork\\rstProject\\ChangeSrcToRST\\expected\\"+fun.name+ ".rst", "r")
            myF = open("C:\\Users\\benja\\Documents\\aptechWork\\rstProject\\ChangeSrcToRST\\output\\"+fun.name+".rst", "r")
            numLine = 1
            for x in f:
                y = myF.readline()
                if (x != y):
                    print("Line ", numLine)
                    print("Expected:\n" + x)
                    print("Got:\n" + y)
                numLine = numLine + 1
        else:
            print(fun.name + " does match!")
