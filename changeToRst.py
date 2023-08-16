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
    def __init__(self):
        #self.fileName = sys.argv[1]
        self.fileName = "ols.src"
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
        f = open(self.outFile, "w")
        f.write(self.fun.name)
        f.write("\n")
        for i in range(0, len(self.fun.name) * 4):
            f.write("=")
        f.write("\n\nPurpose\n----------------\n\n")
        f.write(self.fun.purpose)
        f.write("\n\nFormat\n----------------\n")
        f.write(".. function:: ")
        f.write(self.fun.format)
        f.write("\n")
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
                if re.search(r"\/\*\n", x) or re.search(r"\*{2}>\s+\S+\n", x):
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
                while (re.search(r"[*]{2}\s*\n", x) or re.search(r"[*]{2}\s*Inputs*:\n", x)):
                    x = f.readline()
                #if (re.search(r"[--]", x)):
                #    continue
                input = []
                count = 0
                y = x
                temp = ""
                x = f.readline()
                temp = x
                x = re.sub("\*\*\s+", "", x)
                while not (re.search(r"\*{2}\s\s+\S+\s\s+", x) or re.search(r"Output", x)):
                        x = re.sub("\*\*\s+", "", x)
                        y = y + x
                        x = f.readline()
                z1 = re.search(r"\*{2}\s+", x).group()
                z2 = len(z1)
                while (re.search(r"\*", temp)):
                    y = re.sub("\*\*\s+", "", y)
                    y = re.sub(r"Input[s]*:\s*", "", y)
                    input = re.split(r"\s\s\s*", y)
                    n = input[0]
                    s = input[-1].replace(".\n", "")
                    if (re.search(r"\w+,\s", s)):
                        t = re.search(r"\w+,\s", s).group()
                    elif (re.search(r"\S+\sor\s\S+", s)):
                        if (re.search(",", s)):
                            z = re.findall(r"[^,]+,", s)
                            t = "".join(z)
                        else:
                            z = re.search(r"\S+\sor\s\S+", s)
                            t = z.group()
                        s = re.split(t, s)[-1]
                        s = s.replace(" ", "", 1)
                    else:
                        t = re.split(r"\s", s)[0]
                    t = t.replace(",", "")
                    s = s.replace("'", "*")
                    s = s.replace("\n", "")
                    if (re.search(t, s)):
                        s = s.replace(t, t.lower())
                    t = t.lower()
                    if (len(s) == 0):
                        s = "Data."
                    self.fun.paramList.append(param(n, t, s))
                    count = count + 1
                    if (re.search(r"Output", temp) or re.search(r"Output", x) or re.search(r"Output", y)):
                        break
                    #x = f.readline()
                    while (re.search(r"\*{2}\n", x)):
                        x = f.readline()
                    if not (re.search(r"\*{2}\s+\S+\s\s+\S+", x) or re.search(r"Output", x) or re.search(r"Example", x)):
                        temp = f.readline()
                    while not (re.search(r"Output", temp) or re.search(r"Example", temp)):
                        if (not ((len(re.search(r"\*{2}\s+", temp).group())) > z2)) and not re.search(r"\*{2}\n", temp):
                            break
                        temp = re.sub(r"\*{2}\s+", "", temp)
                        x = x + temp
                        temp = f.readline()
                    x = x.replace("\n", "")
                    y = x
                    if not (re.search(r"\*{2}\n", temp)):
                        x = temp
                        if (re.search(r"Output", x)):
                            continue
                        temp = f.readline()
                for i in range(count, len(pL)):
                    #if (re.search(r"\]", pL[i])):
                    s = "Optional argument"
                    n = pL[i]
                    n = n.replace(" ", "")
                    n = n.replace(",", "")
                    n = n.replace("[", "")
                    n = n.replace("]", "")
                    self.fun.paramList.append(param(n, "", s))
                x = temp

            if re.search(r"Output\w*:", x):
                y = x
                while (re.search(r"[*]{2}\n", y)):
                    y = f.readline()
                if (re.search(r"[--]", y)):
                    continue
                if (re.search("Output:*\n", y)):
                    y = f.readline()
                temp = f.readline()
                if (re.search(r"[*]{2}\s+\S+\s\s+", temp)):
                    y = temp
                if (re.search(r"\*{2}\n", y)):
                    y = temp
                    temp = ""
                x2 = re.sub(r"Output", "      ", x)
                x2 = re.sub(r"s:", "  ", x2)
                x2 = re.sub(r":", " ", x2)
                z1 = re.search(r"\*{2}\s+", x2).group()
                z2 = len(z1)
                if (re.search(r"Outputs*:*\n", y)):
                    y = f.readline()
                #FIXME make output collect text until an equally indented variable appears
                while (re.search(r"[\*]", x) and re.search(r"[^**\n]", x) and not re.search(r"Remarks", x)):
                    while not (re.search(r"Example", temp) or re.search(r"\*\/\n", temp) or re.search(r"Remarks", y)):
                        y = y + temp
                        temp = f.readline()
                        if (not ((len(re.search(r"\*{2}\s+", temp).group())) > z2)) and not re.search(r"\*{2}\n", temp):
                            break
                    y = re.sub(r"Output.*:", "", y)
                    if (re.search(r"[*]{2}\n", y)):
                        y = re.sub(r"[*]{2}\n", "",  y)
                    input = re.split(r"\s+", y, 2)
                    n = input[1]
                    s = input[-1].replace(".\n", "")
                    if (re.search(r"\s*[^,]+,", s)):
                        t = re.search(r"\s*[^,]+,", s).group()
                    elif (re.search(r"\S+\sor\s\S+", s)):
                        z = re.search(r"\S+\sor\s\S+", s)
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
                    if not (not ((len(re.search(r"\*{2}\s+", temp).group())) > z2)) and not re.search(r"\*{2}\n", temp):
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
                for i in self.fun.paramList:
                        if re.search(i.name, self.fun.remarks):
                            self.fun.remarks = self.fun.remarks.replace(" " + i.name + " ", " *" + i.name + "* ")
                for i in self.fun.returnList:
                        self.fun.remarks = self.fun.remarks.replace(" " + i.name + " ", " *" + i.name + "* ")
                #print(self.fun.remarks)
            if not (re.search(r"[*]", x)):
                f.close()
                return self.fun
            
            if ((re.search(r"Example", x) or re.search(r"Example", y)) or ((len(self.exList) > 0) and (re.search(self.fun.name, x)))):
                while (True):
                    if (re.search(r"\**\n", x)):
                        while (re.search(r"\*{2}\n", x) or re.search(r"^\n$", x)):
                            x = f.readline()
                    if (re.search(r"\*\/\n", x)):
                        return self.fun
                        break
                    if (re.search(r"See Also", x)):
                        self.fun.remarks = self.fun.remarks + x
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
                    comments = re.sub(r"\s*Example\s.{1}:\n", "", comments)
                    ex = example()
                    input = ""
                    if (re.search(r"Example", y)):
                        y = re.sub(r"Examples:", "          ", y)
                        y = re.sub(r".+Example\s*\d*:*\s*", "", y)
                        z1 = re.search(r"[*]*\s\s+", y)
                        input = input + y
                        y = f.readline()
                        while(re.search(r"\*{2}\n", y)):
                            y = f.readline()
                    else:
                        z1 = re.search(r"[*]*\s\s+", y)
                    while not re.search(" " + self.fun.name + r"\W", y):
                        #if (re.search(r"[*]{2}\s\s+", y)):
                            #y = re.sub(re.escape(z1.group()), "    ", y)
                        input = input + y
                        y = f.readline()
                    #if (re.search(r"[*]{2}\s\s+", y)):
                            #y = re.sub(re.escape(z1.group()), "    ", y)
                    #input = input + y
                    input = input.replace("**", "")
                    #input = re.sub(re.escape(z1.group()), "", input)
                    ex.setIn(input)
                    y = y.replace("**", "")
                    varName = re.search("\S+", y)
                    output = ""
                    while(re.search(r"\*{2}\n", y)):
                        y = f.readline()
                    #y = f.readline()
                    x = ""
                    while not (re.search(r"\*{2}\n", x)):
                        y = y + x
                        x = f.readline()
                    x = ""
                    #FIXME: thinks its over after new line when thats not always the case
                    count = 0
                    #for i in self.fun.returnList:
                    y = y.replace("'", "*")
                    if (re.search(r",\s{1}\S+\s", y)):
                        z1 = re.search(r",\s{1}\S+\s", y)
                        z2 = ", *" + varName.group() + "* "
                        y = re.sub(z1.group(), z2, y)
                    y = y + "\n::\n"
                    if (re.search(r"[*]{2}\s\s+", y)):
                        y = re.sub(re.escape(z1.group()), "", y)
                    count = 0
                    output = y
                    y = f.readline()
                    while not (re.search(";", y) or re.search(r"\s\s+Example", y) or re.search(r"\=", y) or re.search(r"Globals", y)):
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
                    y = y.replace(" };", "")
                    #output = output + y
                    output = output.replace("**", "")
                    output = output.replace(",", "")
                    output = output.replace("*/\n", "")
                    output = re.sub(r"\n\n\n+", "\n", output)
                    ex.setOut(output)
                    ex.setCom(comments)
                    self.exList.append(ex)
                    x = y
            if (re.search(r"Global", x)):
                while not (re.search(r"\*{2}\n", x)):
                    x = f.readline()
            if (re.search(r"See Also", x)):
                self.fun.remarks = self.fun.remarks + x
        return self.fun
                



f = srcFile()
f.makeRSTFiles()