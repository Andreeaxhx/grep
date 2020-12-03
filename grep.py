import re, sys, os
from colorama import init
from termcolor import colored
from argparse import ArgumentParser

init()

def parser():
    parser=ArgumentParser(description="Equivalent of grep command in linux")
    parser.add_argument("pattern", type=str, help="search for patterns in each file")
    parser.add_argument("file", metavar="FILE", help="the file to search")
    parser.add_argument("-reg", action="store_true", help="regex pattern")
    parser.add_argument("-R", "-r", "--recursive", action="store_true", help="recursive search")
    parser.add_argument("-L", "--files-without-match", action="store_true", help="some pattern does NOT match the file")
    parser.add_argument("-c", "--count", action="store_true", help="number of lines that match the pattern")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="case-insensitive option")

    return parser

def file_search(pattern, file_path, regex, recursive, files_without_match, count, ignore_case): #regex=expresia regulata;
                                          #face_match=valoare booleana setata in functie de argumentul NOT;
                                          #path_to_file=path ul catre file ul in care vrem sa se caute regex
    match=False #presupunem ca regex nu face match cu niciun cuvant din file
    nr_of_matches=0

    if os.path.isfile(file_path):
        file=open(file_path)
        print("-----", file_path)
        lines=file.readlines() #se citeste file ul linic cu linie
        for line in lines:
            if ignore_case:
                matches_of_regex=re.findall(pattern, line, flags=re.IGNORECASE)
            else:
                matches_of_regex = re.findall(pattern, line)
            if matches_of_regex:
                match=True
                if files_without_match:

                    for i in matches_of_regex:
                        lista=line.split(i, 1)
                        line=lista[0]+colored(i, 'red')+lista[1]
                    line=line.replace("\n", "")
                    print(line)
                    nr_of_matches+=1
        if count:
            print(colored("Number of matches:", "green"), nr_of_matches)
        if match==False and files_without_match==False:
            print("regex nu face match in file")

    elif os.path.isdir(file_path):

        for f in os.listdir(file_path):

            if os.path.isfile(file_path+"\\"+f):
                file_search(pattern, file_path+"\\"+f, regex, recursive, files_without_match, count, ignore_case)


parser=parser()
arguments=parser.parse_args()
pattern=arguments.pattern
file=arguments.file

file_search(pattern, file, arguments.reg, arguments.recursive, arguments.files_without_match, arguments.count, arguments.ignore_case)
