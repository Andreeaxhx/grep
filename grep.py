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
    nr_of_matches=0

    if os.path.isfile(path):
        file=open(path)
        print("-----", path)
        lines=file.readlines() #se citeste file ul linic cu linie
        for line in lines:
            if ignore_case:
                matches_of_regex=re.findall(regex, line, flags=re.IGNORECASE)
            else:
                matches_of_regex = re.findall(regex, line)
            if matches_of_regex:
                match=True
                if face_match==True:

                    for i in matches_of_regex:
                        lista=line.split(i, 1)
                        line=lista[0]+colored(i, 'red')+lista[1]
                    line=line.replace("\n", "")
                    print(line)
                    nr_of_matches+=1
        if count:
            print(colored("Number of matches:", "green"), nr_of_matches)
        if match==False and face_match==False:
            print("regex nu face match in file")

    elif os.path.isdir(path):

        for f in os.listdir(path):

            if os.path.isfile(path+"\\"+f):
                file_search(regex, face_match, path+"\\"+f, ignore_case, count)


list_of_arguments=sys.argv
#print(len(list_of_arguments))

if len(list_of_arguments)!=6:
    print("please insert all arguments")
    exit()
elif list_of_arguments[1]=="NOT":
    if list_of_arguments[4]=="-ignoreCase" and list_of_arguments[5]=="-count":
        file_search(list_of_arguments[2], False, list_of_arguments[3], True, True)
    elif list_of_arguments[4]=="-ignoreCase" and list_of_arguments[5]!="-count":
        file_search(list_of_arguments[2], False, list_of_arguments[3], True, False)
    elif list_of_arguments[4]!="-ignoreCase" and list_of_arguments[5]=="-count":
        file_search(list_of_arguments[2], False, list_of_arguments[3], False, True)
    elif list_of_arguments[4]!="-ignoreCase" and list_of_arguments[5]!="-count":
        file_search(list_of_arguments[2], False, list_of_arguments[3], False, False)
elif list_of_arguments[1]!="NOT":
    if list_of_arguments[4]=="-ignoreCase" and list_of_arguments[5]=="-count":
        file_search(list_of_arguments[2], True, list_of_arguments[3], True, True)
    elif list_of_arguments[4]=="-ignoreCase" and list_of_arguments[5]!="-count":
        file_search(list_of_arguments[2], True, list_of_arguments[3], True, False)
    elif list_of_arguments[4]!="-ignoreCase" and list_of_arguments[5]=="-count":
        file_search(list_of_arguments[2], True, list_of_arguments[3], False, True)
    elif list_of_arguments[4]!="-ignoreCase" and list_of_arguments[5]!="-count":
        file_search(list_of_arguments[2], True, list_of_arguments[3], False, False)