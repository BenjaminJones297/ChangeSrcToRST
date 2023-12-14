# @author Benjamin Jones
# Last updated 8/1/2023
# FIXME: fix input, output for join.src format
# FIXME: Input testing
# FIXME: Unit testing
import sys
import re

class function:
    def __init__(self):
        self.name = "func"
        self.format = ""
        self.paramNameList = []
        self.paramList = []
        self.returnList = []
        self.returnNameList = []
        self.remarks = ""
        self.purpose = ""

class returnVal:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.sum = ""
    def __init__(self, name, type, summary):
        self.name = name
        self.type = type
        self.sum = summary
    def toString(self):
        return "    :return " + self.name + ": " + self.sum + "\n    :rtype " + self.name + ": " + self.type + "\n\n"

class param:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.sum = ""
    def __init__(self, name, type, summary):
        self.name = name
        self.type = type
        self.sum = summary
    def toString(self):
        return "    :param " + self.name + ": " + self.sum + "\n    :type " + self.name + ": " + self.type + "\n\n"

class example:
    def __init__(self):
        self.input = ""
        self.output = ""
        self.comments = ""
    def setIn(self, input):
        self.input = input
    def setOut(self, output):
        self.output = output
    def setCom(self, com):
        self.com = com
    def toString(self):
        return self.comments + self.input + "\n" + self.output
    
class srcFile:
    def __init__(self, fileName):
        self.fileName = fileName
        #self.fileName = sys.argv[1]
        #self.fileName = "C:\\Users\\benja\\Documents\\aptechWork\\rstProject\\ChangeSrcToRST\\between.src"
        self.outFile = ""
        self.fun = function()
        self.funList = []
        self.exList = []
    def writeVar(self):
        out = ""
        for i in range (0, len(self.fun.paramList)):
            out = out + self.fun.paramList[i].toString()
        for i in range (0, len(self.fun.returnList)):
            out = out + self.fun.returnList[i].toString()
        return out
    def writeExample(self):
        out = ""
        count = 1
        for i in self.exList:
            out = out + "\n\nExample " + count.__str__() + "\n+++++++++++\n\n::\n\n"
            count = count + 1
            out = out + i.toString()
        return out
    # writes file
    def write(self):
        f = open("C:\\Users\\benja\\Documents\\aptechWork\\rstProject\\ChangeSrcToRST\\output\\"+self.outFile, "w")
        f.write(self.fun.name)
        f.write("\n")
        for i in range(0, len(self.fun.name) * 4):
            f.write("=")
        f.write("\n\nPurpose\n----------------\n\n")
        f.write(self.fun.purpose)
        f.write("\n\nFormat\n----------------\n")
        f.write(".. function:: ")
        f.write(self.fun.format)
        f.write("\n\n")
        f.write(self.writeVar())
        f.write("Examples\n----------------")
        f.write(self.writeExample())
        f.write("\nRemarks\n-------\n\n")
        f.write(self.fun.remarks)
        f.close()
    
    def makeRSTFiles(self):
        numFun = self.find_num_func()
        for i in range(1, numFun + 1):
            self.fun = self.find_vars(i)
            self.funList.append(self.fun)
            self.outFile = self.fun.name + ".rst"
            self.write()
        return

    def find_num_func(self):
        f = open(self.fileName, "r")
        numFun = 0
        for x in f:
            if re.search(r"Purpose", x):
                return 1
            if (re.search(r"^\n", x)):
                count = 0
                for x in f:
                    if (re.search(r"\*\/", x)):
                        count = count + 1
                        while not (re.search(r"\/\*", x)):
                            if (re.search(r"Gauss code", x)):
                                while not (re.search(r"\*", x)): # skip ahead to the gauss code so you can skip over it
                                    x = f.readline()
                                while (re.search(r"\*", x)): # if it says gauss code skip over that
                                    x = f.readline()
                            if (x == ''):
                                return count
                            x = f.readline()
                f.close()
                return count
            if (re.search(r"Procedure\s+Purpose", x)):
                y = f.readline()
                y = f.readline()
                break
        while not (re.search(r"[*]{2}\n", y)):
            numFun = numFun + 1
            y = f.readline()
        f.close()
        return numFun
    
    def find_vars(self, num):
        anExample = False
        y = ""
        self.fun = function()
        f = open(self.fileName, "r")
        self.exList = []
        pL = []
        curEx = 0
        end = False
        curFun = -1
        for x in f:
            while (curFun != num):
                if re.search(r"\/\*\n", x):
                    curFun = curFun + 1
                if (curFun == num):
                    break
                x = f.readline()
            # if it says Purpose:
            if re.search(r"Purpose:.+.\n", x):
                self.fun.purpose = x
                y = f.readline()
                # then keep going through lines until we have a period followed by a newline
                while not (re.search(r"\.\n", y) or re.search(r"[\*{2}\n]$", y)):
                    self.fun.purpose = self.fun.purpose + y
                    y = f.readline()
                if not re.search(r"\*{2}\n", y):
                    self.fun.purpose = self.fun.purpose + y
                self.fun.purpose = self.fun.purpose.replace("**", "")
                self.fun.purpose = self.fun.purpose.replace("\n", "")
                self.fun.purpose = self.fun.purpose.replace(" Purpose: ", "")
                self.fun.purpose = re.sub(r'\s\s+', ' ', self.fun.purpose)
                if (re.search("^\s", self.fun.purpose)):
                    self.fun.purpose = self.fun.purpose.replace(" ", "", 1)
                #print(self.fun.purpose)
            if re.search(r"Format:", x):
                if (re.search(r"Format:*\n", x)):
                    x = f.readline()
                y = f.readline()
                if (re.search(r"=\n$", x)):
                    x = x + y
                elif (re.search(r";", y) and not re.search(r"\[", y)):
                    y = y.replace(");\n", "")
                    #temp = re.sub(x, r"", tempY)
                    temp = y.replace(x.replace(");\n", ""), "")
                    new = temp.replace(",", "[,", 1)
                    new = new + "]);\n"
                    x = re.sub(temp, new, y)
                elif (re.search(r";", y)):
                    x = y
                self.fun.format = x
                self.fun.format = re.sub(r"[*]{2}", "", self.fun.format)
                self.fun.format = re.sub(r"\s+Format: ", "", self.fun.format)
                self.fun.format = self.fun.format.replace(";", "")
                self.fun.format = re.sub(r"\s\s+", "", self.fun.format)
                self.fun.format = self.fun.format.replace("\n", "")
                y = re.split(r"[=]", x)
                z = re.split(r"[(]", y[-1])
                title = z[0]
                title = title.replace(" ", "")
                title = title.replace("*", "")
                title = title.replace("\n", "")
                self.fun.name = title
                #print(title)
                #print(self.fun.paramList)
                pL = re.split(",\s*", z[1])
                temp = re.split(r"[);\n]", pL[-1])
                pL[-1] = temp[0]
                self.fun.paramNameList = pL
                y = ""
                
            if re.search(r"Input\w*:", x):
                if (len(self.fun.name) < 1):
                    return function()
                while (re.search(r"[*]{2}\s*\n", x) or re.search(r"[*]{2}\s*Inputs*:\n", x)): # skip ahead after the just input line and any empty lines
                    x = f.readline()
                #if (re.search(r"[--]", x)):
                #    continue
                input = []
                count = 0
                y = x
                temp = ""
                x = f.readline() # x is the second line now
                temp = x # temp us a copy of the second line
                while not (re.search(r"\*{2}\s\s+\S+\s\s+", x) or re.search(r"Output", x)): # keep adding x to y and making x the next line until we get to output or we get to another line with some spaces and some characters and more spaces
                        x = re.sub("\*\*\s+", "", x)
                        y = y + x
                        x = f.readline()
                z1 = re.search(r"\*{2}\s+", x).group() # leading spaces and *s
                z2 = len(z1)
                while (re.search(r"\*", temp)): # while there is a * in temp, (the next variable after x that we just added)
                    y = re.sub("\*\*\s+", "", y)
                    y = re.sub(r"Input[s]*:\s*", "", y) # format the first line
                    input = re.split(r"\s\s\s*", y) # break into varname, description
                    n = input[0] # n = name
                    s = input[-1].replace("\n", "") # s = description w/o \n
                    if not (re.search(r"\S+\s+\S+\s+\S+\s+\S+", s)): # if it is not a full sentence, (3 words or less, then no comma)
                        s = s.replace(".", "")
                    if (re.search(r"\w+,\s", s)): # if there is a comma t is that word, hoping its the type
                        if (re.search(r"\S+\sor\s\S+", x)):
                            z = re.search(r"\S+\sor\s\S+", s) # if comma and an or
                            t = z.group() # make those two words the type
                        else:
                            t = re.search(r"\w+,\s", s).group()
                    elif (re.search(r"\S+\sor\s\S+", s)): # otherwise if there is an or in there
                        if (re.search(",", s)): # and a comma
                            z = re.findall(r"[^,]+,", s) # find every part with a comma
                            t = "".join(z) # and throw them together
                        else:
                            z = re.search(r".*or\s\S+", s) # if no comma and an or
                            t = z.group() # make those two words the type
                        s = re.split(t, s)[-1]
                        s = s.replace(" ", "", 1)
                    else:
                        t = re.split(r"\s", s)[0]
                    t = t.replace(",", "")
                    s = s.replace("'", "*")
                    s = s.replace("\n", "")
                    if (re.search(t, s)): # if type is in description still
                        s = s.replace(t, t.lower()) # make it lower case
                    t = t.lower() # make type lower case
                    if (len(s) == 0): # if no description default is Data.
                        s = "Data."
                    self.fun.paramList.append(param(n, t, s))
                    count = count + 1 # count num of params
                    # temp is next one so we are done if it says output
                    if (re.search(r"Output", temp) or re.search(r"Output", x) or re.search(r"Output", y)):
                        break
                    #x = f.readline()
                    while (re.search(r"\*{2}\n", x)):
                        x = f.readline()
                    if not (re.search(r"\*{2}\s+\S+\s\s+\S+", x) or re.search(r"Output", x) or re.search(r"Example", x)):
                        temp = f.readline()
                    while not (re.search(r"Output", temp) or re.search(r"Example", temp)): # if we aren't done bc the next line is output or an example
                        if (not ((len(re.search(r"\*{2}\s+", temp).group())) > z2)) and not re.search(r"\*{2}\n", temp): # if after formatting temp is just the blank stuff we should break
                            break
                        temp = re.sub(r"\*{2}\s+", "", temp) # if temp exists but is output or example take *s off
                        #x = x + temp # add it on to x
                        temp = f.readline()
                    x = x.replace("\n", "") # take off nl of x
                    y = x # y is now the current we just added
                    if not (re.search(r"\*{2}\n", temp)):
                        y = temp # now y is the next one
                        if (re.search(r"Output", y)):
                            temp = re.sub(r"\*{2}\s+", "", temp)
                            continue
                        temp = f.readline() # and temp is the following one
                for i in range(count, len(pL)): # if we didnt find the expected num of params add some optional ones
                    #if (re.search(r"\]", pL[i])):
                    s = "Optional argument"
                    n = pL[i]
                    n = n.replace(" ", "")
                    n = n.replace(",", "")
                    n = n.replace("[", "")
                    n = n.replace("]", "")
                    self.fun.paramList.append(param(n, "", s))
                x = temp # x is latest line

            if re.search(r"Output\w*:", x):
                # FIXME indentation not correct and the sentence with code above should not be in result
                y = x # y is curline
                while (re.search(r"[*]{2}\n", y)): # skip ahead until its not just **\n
                    y = f.readline()
                if (re.search(r"[--]", y)):
                    continue
                if (re.search("Output:*\n", y)): # if we know are at output skip that
                    y = f.readline()
                temp = f.readline() # temp is line after
                if (re.search(r"[*]{2}\s+\S+\s\s+", temp)):
                    y = temp
                    temp = ""
                if (re.search(r"\*{2}\n", y)):
                    y = temp
                    temp = ""
                y = ""
                while (re.search(r"\*\*\n", temp)): # if its just newlines skip until its not
                    temp = f.readline()
                if not (re.search(r"utput:*\s+\w+", x)):
                    x = temp
                x2 = re.sub(r"Output", "      ", x)
                x2 = re.sub(r"s:", "  ", x2)
                x2 = re.sub(r":", " ", x2) # if it was included on input line take that off
                z1 = re.search(r"\**\s+", x2).group()
                z2 = len(z1)
                if (re.search(r"Outputs*:*\n", y)):
                    y = f.readline()
                #FIXME make output collect text until an equally indented variable appears
                while (re.search(r"[\*]", x) and re.search(r"[^**\n]", x) and not re.search(r"Remarks", x) and not re.search(r"Example", x) and not re.search(r"\*\/\n", x)):
                    while not (re.search(r"Example", temp) or re.search(r"\*\/\n", temp) or re.search(r"Remarks", y)):
                        y = y + temp
                        temp = f.readline()
                        if (re.search(r"\*\/\n", temp)):
                            break
                        if (not ((len(re.search(r"\*{2}\s+", temp).group())) > z2)) or re.search(r"\*{2}\n", temp):
                            break
                    y = re.sub(r"Output.*:", "", y)
                    if (re.search(r"[*]{2}\n", y)):
                        y = re.sub(r"[*]{2}\n", "",  y)
                    input = re.split(r"\s+", y, 2) # format into **, name, des
                    n = input[1]
                    s = input[-1].replace(".\n", "")
                    if (re.search(r"\s*[^,]+,", s)):
                        t = re.search(r"\s*[^,]+,", s).group()
                    elif (re.search(r"\S+\sor\s\S+", s)):
                        z = re.search(r".*or\s\S+", s)
                        t = z.group()
                    else:
                        t = re.split(r"\s", s)[0]
                    if (re.search(r"\s\w+x\w+\s", s)):
                        t = t + re.search(r"\s\w+x\w+\s\S+", s).group()
                        #s = re.sub(t, "", s)
                    elif (re.search(" matrix", s)):
                        #s = s.replace(t + " matrix", "")
                        t = t + " matrix"
                    #s = re.split(t, s)[-1]
                    if (re.search(r"^\s", s)):
                        s = s.replace(" ", "", 1)
                    s = s.replace(",", "", 1)
                    t = t.replace("'", "*")
                    t = t.replace(",", "")
                    s = s.replace(t, t.lower())
                    if not (re.search(r"\w{1}x\w{1}", t)):
                        t = t.lower()
                    s = s.replace("'", "*")
                    s = s.replace("**", "")
                    s = re.sub(r"\s\s+", " ", s)
                    if (len(n) == 0):
                        n = "Data."
                    if (re.search(r"\n$", s)):
                        s = re.sub("\n", "", s)
                    self.fun.returnList.append(returnVal(n, t, s))
                    if (re.search(r"\*{2}\s+", temp)):
                        if (not (len(re.search(r"\*{2}\s+", temp).group())) > z2) or re.search(r"\*{2}\n", temp):
                            y = f.readline()
                            temp = y 
                    x = temp
                    y = ""
                #print(self.fun.returnList)
            if re.search(r".+Remarks:", x):
                y = x
                if (re.search(r"Remarks:\n", y)):
                    while (re.search(r"[*]{2}\n", y)):
                        y = f.readline()
                    y = f.readline()
                y = y.replace("Remarks:", "        ")
                y = re.sub(r"^[*]{2}\s\s+", "", y)
                # then keep going through lines until we have a period followed by a newline
                while not (re.search(r"[*]{1}[/]{1}\n", y) or re.search(r"Example", y)):
                    self.fun.remarks = self.fun.remarks + y
                    y = f.readline()
                    y = re.sub(r"^[*]{2}\s\s+", "", y)
                self.fun.remarks = self.fun.remarks.replace("**  ", "")
                self.fun.remarks = self.fun.remarks.replace("**", "")
                #x = y
                for i in self.fun.paramList:
                        if re.search(i.name, self.fun.remarks):
                            self.fun.remarks = self.fun.remarks.replace(" " + i.name + " ", " *" + i.name + "* ")
                for i in self.fun.returnList:
                        self.fun.remarks = self.fun.remarks.replace(" " + i.name + " ", " *" + i.name + "* ")
                #print(self.fun.remarks)
            #if not (re.search(r"[*]", x)):
            #   f.close()
            #   return self.fun
            
            if (re.search(r"Example", x) or re.search(r"Example", y)):
                x = y
                while (not (re.search(r"^\n", x) or re.search(r"\*\/\n", x))):
                    if (re.search(r"\*\*\n", x)):
                        while (re.search(r"\*{2}\n", x) or re.search(r"^\**\s*\n$", x)):
                            x = f.readline()
                            if not (re.search(r"\*", x)):
                                return self.fun
                    if (re.search(r"\*\/\n", x) or re.search(r"^\**\s*\n$", x)):
                        return self.fun
                        break
                    if (re.search(r"See also", x)):
                        #self.fun.remarks = self.fun.remarks + x
                        break
                    if (re.search(r"Global", x)):
                        break
                    anExample = True
                    if (re.search(self.fun.name, x)):
                        y = x
                    if (re.search(r"Example\S*:*\n", x)):
                        y = f.readline()
                    comments = ""
                    while (re.search(r"[*]{2}\n", y)):
                        if (re.search(r"\\{2}", y)):
                            comments = comments + y
                        y = f.readline()
                    y = y.replace("**","  ")
                    comments = re.sub(r"\s*Example\s.{1}:\n", "", comments)
                    ex = example()
                    input = ""
                    if (x == ""):
                        x = f.readline()
                        y = x
                    if (re.search(r"Example", x)):
                        temp = x
                    if (re.search(r"Example", x)):
                        y = re.sub(r"Examples:", "          ", y)
                        #y = re.sub(r".+Example\s*\d*:*\s*", "", y)
                        y = re.sub(r"Example:*\n", "", y)
                        z1 = re.search(r"[*]*\s\s+", y)
                        input = input + y
                        y = f.readline()
                        while(re.search(r"\*{2}\n", y)):
                            y = f.readline()
                    else:
                        z1 = re.search(r"[*]*\s\s+", y)
                    # if it sees the functions name we are done
                    while not re.search(" " + self.fun.name + r"\W", y):
                        if (re.search(r"[*]{2}\s\s+", y)):
                            y = re.sub(re.escape(z1.group()), "    ", y)
                        input = input + y
                        y = f.readline()
                    input = input + y
                    #if (re.search(r"[*]{2}\s\s+", y)):
                            #y = re.sub(re.escape(z1.group()), "    ", y)
                    #input = input + y
                    input = input.replace("**", "  ")
                    input = input.replace("'", "*")
                    #input = re.sub(re.escape(z1.group()), "", input)
                    ex.setIn(input)
                    y = y.replace("**", "")
                    varName = re.search("\w+", y)
                    output = ""
                    while(re.search(r"\*{2}\n", y)):
                        y = f.readline()
                    y = f.readline()
                    x = ""
                    while not (re.search(r"\*{2}\n", x)):
                        y = y.replace("**\n","")
                        y = y + x
                        x = f.readline()
                    x = ""
                    #FIXME: thinks its over after new line when thats not always the case
                    count = 0
                    #for i in self.fun.returnList:
                    y = y.replace("'", "*")
                    y = y.replace("**","")
                    if (re.search(r",\s{1}\W+\s", y)):
                        z1 = re.search(r",\s{1}\W+\s", y)
                    z2 = "*" + varName.group() + "*"
                    y = re.sub(re.escape(varName.group()), z2, y)
                    y = y + "\n::\n"
                    if (re.search(r"[*]{2}\s\s+", y)):
                        y = re.sub(re.escape(z1.group()), "", y)
                    count = 0
                    output = y
                    y = f.readline()
                    #y = f.readline()
                    while not (re.search(";", y) or re.search(r"\s\s+Example", y) or re.search(r"Globals", y)):
                        if not (re.search(r"\*", y)):
                            break
                        y = y.replace("**", "")
                        if re.search(r"[\= \{]", y):
                            y = re.sub(r"[*]{2}\s+\S+\s{1}\=\s{1}\{\s", "        ", y)
                        if (re.search(r"[*]{2}\s\s+", y)):
                            y = re.sub(re.escape(z1.group()), "    ", y)
                        if (re.search(r"After the code above", y)):
                            y = re.sub(r"[*]{2}\s+", "", y)
                        output = output + y
                        if (re.search(r"^\s*\n", y) or re.search(r"[*]{2}\s*\n", y)):
                            if (count == 1):
                                break
                            count = 1
                        y = f.readline()
                    y = y.replace("**", "")
                    #y = y.replace(" };", "")
                    output = output + y
                    output = output.replace("**", "")
                    output = output.replace("'", "*")
                    output = output.replace(",", "")
                    if (re.search(r"\(\S+\s.+\)", output)):
                        z1 = re.search(r"\(\S+\s.+\)", output).group()
                        z2 = re.sub(" ", ", ", z1)
                        output = re.sub(z1, z2, output)
                        output = output.replace("(", "", 1)
                        output = output.replace(")", "", 1)
                    output = output.replace("*/\n", "")
                    output = re.sub(r"\n\n\n+", "\n", output)
                    ex.setOut(output)
                    ex.setCom(comments)
                    self.exList.append(ex)
                    y = f.readline()
                    while (re.search(r"\*\*\n", y)):
                        y = f.readline()
                    x = y
                if (not re.search(r"\*", x) or re.search(r"\*\/\n", x)):
                    return self.fun
            if (re.search(r"Global", x)):
                while not (re.search(r"\*{2}\n", x)):
                    x = f.readline()
            if (re.search(r"See also", x)):
                self.fun.remarks = self.fun.remarks + re.sub(r"\*\*\s+", "", x)
        return self.fun
for n in range(1, len(sys.argv)):
    print(sys.argv[n])
    f = srcFile("C:\\Users\\benja\\Documents\\aptechWork\\RSTProject\\ChangeSrcToRST\\"+sys.argv[n])
    f.makeRSTFiles()