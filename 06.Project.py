inputfile = open("06. Project input file.txt" , "r")
outputfile = open("06.Project Output File.txt" , "w")
inputrecord = 0
mergerecord = 0
outputrecord = 0
line = inputfile.readline()
while line != "":
    if line == "Insert Merge File Here**\n":
        mergefile = open("06.Project Merge File.txt", "r")
        merge = mergefile.readline()
        while merge !="":
            outputfile.write(merge)
            outputrecord +=1
            merge = mergefile.readline()
            mergerecord += 1
        outputfile.write("\n")
        mergefile.close()
    else:
        outputfile.write(line)
        outputrecord +=1
        inputrecord +=1
        line = inputfile.readline()
inputfile.close()
outputfile.close()
print(inputrecord, "Input File Record")
print(mergerecord, "Merge File Record")
print(outputrecord, "Output File record")