import re
from colorama import Fore, Back, Style, init
from termcolor import colored
import sys
import os

init()

def file_search(regex, face_match, path, ignore_case, count): #regex=expresia regulata;
                                          #face_match=valoare booleana setata in functie de argumentul NOT;
                                          #path_to_file=path ul catre file ul in care vrem sa se caute regex
    match=False #presupunem ca regex nu face match cu niciun cuvant din file


    if os.path.isfile(path):
        file=open(path)
        print("-----", path)
        lines=file.readlines() #se citeste file ul linic cu linie
        for line in lines:
            matches_of_regex=re.findall(regex, line)
            if matches_of_regex:
                match=True
                if face_match==True:

                    for i in matches_of_regex:
                        lista=line.split(i, 1)
                        line=lista[0]+colored(i, 'red')+lista[1]
                    line=line.replace("\n", "")
                    print(line)
        if match==False and face_match==False:
            print("regex nu face match in file")

    elif os.path.isdir(path):

        for f in os.listdir(path):

            if os.path.isfile(path+"\\"+f):
                file_search(regex, face_match, path+"\\"+f)


list_of_arguments=sys.argv
#print(list_of_arguments)

if len(list_of_arguments)==1:
    print("please insert a regex and a file/folder")
    exit()
elif len(list_of_arguments)==2:
    print("please insert a file/folder")
    exit()
elif list_of_arguments[1]=="not" and type(list_of_arguments[2]) is str:
    file_search(list_of_arguments[2], False, list_of_arguments[3])
elif list_of_arguments[1]!="not" and os.path.isfile(list_of_arguments[2]) == False and  os.path.isdir(list_of_arguments[2])==False:
    file_search(re.compile(list_of_arguments[1]), True, list_of_arguments[2])

elif list_of_arguments[1]!="not" and (os.path.isfile(list_of_arguments[2]) or os.path.isdir(list_of_arguments[2])):
    file_search(re.compile(list_of_arguments[1]), True, list_of_arguments[2])


