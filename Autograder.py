import os
import string
import re
import gzip
from subprocess import call

call(["mkdir", "sorted_dirs"]);
for (dirname, dirs, files) in os.walk('./submissions/'):
   for filename in files:
       if filename.endswith('.cc') :
            thefile = os.path.join(dirname,filename)
            string1 = re.search(r"[a-zA-Z]+",filename)
            #print(string1.group(0))
            os.system("mkdir ./sorted_dirs/"+string1.group(0))
            os.system("mv ./submissions/"+string1.group(0)+"_*.*"+" ./sorted_dirs/"+string1.group(0)+"/.")

for (dirname, dirs, files) in os.walk('./sorted_dirs/'):
   for filename in files:
       if filename.endswith('.h') :
            thefile = os.path.join(dirname,filename)             
            string0 = re.search(r"[a-zA-Z0-9]+",filename)
            split_string_list = filename.split("_")
            file_end = "\.h"
            string1 = [x for x in split_string_list if re.search(file_end,x)]
            string2 = ''.join(string1)
            string2 = re.sub(r"\-[0-9]","",string2)
            #print (string2)
            os.system("cp ./sorted_dirs/"+string0.group(0)+"/"+filename+" ./sorted_dirs/"+string0.group(0)+"/"+string2)

os.system("for d in sorted_dirs/*/; do cp Main.cpp \"$d\"; done")
os.system("cd sorted_dirs")

COUNT =0
def increment():
    global COUNT
    COUNT = COUNT+1

def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile)

for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if (filename.endswith('.h') and (("_") not in filename)) :
        increment()
	#uncomment below to preprend header file in main:w	        
        insert(dirname+"/Main.cpp", "#include \""+filename+"\" \n")	
#print(COUNT)

for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.cc') :
            thefile = os.path.join(dirname,filename)
            test_string = filename            
            object_name = test_string.replace(".cc",".o")
            os.system("g++ -c "+dirname+"/Main.cpp "+ thefile)
            os.system("g++ Main.o "+object_name)
            os.system("./a.out >> "+dirname+"_output.txt")
            os.system("echo \" \"; echo \" ====================== \" >> FinalResults.txt ")
            os.system("echo  Differences between Ideal_output.txt and" +dirname +"_output.txt  >> FinalResults.txt")
            os.system("diff -w Ideal_output.txt "+dirname+"_output.txt >> FinalResults.txt")
            os.remove('./a.out')
            print("File a.out removed")




           

           
