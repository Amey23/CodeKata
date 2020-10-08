def CodeLineCount(filename):
  file = open(filename);
  allLines = file.readlines();
  file.close();
  codeCount = 0;
  for eachLine in allLines:
     #print(eachLine)
     if eachLine != " " :
       eachLine = eachLine.replace(" ","");
     if eachLine.startswith('//') or eachLine.startswith('/*') or eachLine.startswith('*/')or eachLine.startswith('*'):
       continue
     else :
       if eachLine == "":
         continue
       else :
         codeCount += 1;
  print(codeCount)

#call function
CodeLineCount("demo.java")

