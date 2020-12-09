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

def search(pattern, file_path, is_file, regex, recursive, files_without_match, count, ignore_case): #regex=expresia regulata;
                                          #face_match=valoare booleana setata in functie de argumentul NOT;
                                          #path_to_file=path ul catre file ul in care vrem sa se caute regex
    match=False #presupunem ca regex nu face match cu niciun cuvant din file
    nr_of_matches=0

    if os.path.isfile(file_path):
        file=open(file_path, "r")
        lines=file.readlines() #se citeste file ul linie cu linie
        for line in lines:
            if regex:
                if ignore_case:
                    matches = re.findall(pattern, line, flags=re.IGNORECASE)
                else:
                    matches = re.findall(pattern, line)
                if matches:
                    match=True
                    if files_without_match==False:
                        for i in matches:
                            lista=line.split(i, 1)
                            line=lista[0]+colored(i, 'red')+lista[1]
                        line=line.replace("\n", "")
                        if count==False:
                            if is_file and files_without_match==False:
                                print(line)
                            elif files_without_match==False:
                                print(colored(file_path, 'magenta')+":"+line)
                        nr_of_matches+=1
            else:
                if ignore_case:
                    pattern_low=pattern.lower()
                    line_low=line.lower()

                    if line_low.find(pattern_low)>=0:
                        index = line_low.find(pattern_low)
                        match=True
                        nr_of_matches+=1
                        #line=line.replace(pattern, colored(pattern, 'red'));
                        line=line[:index]+colored(line[index:index+len(pattern)], 'red')+line[index+len(pattern):]
                        line=line.replace("\n", '')
                        if count == False:
                            if is_file and files_without_match==False:
                                print(line)
                            elif files_without_match==False:
                                print(colored(file_path, "magenta")+":"+line)
                else:
                    if line.find(pattern)>=0:
                        match=True
                        nr_of_matches+=1
                        line=line.replace(pattern, colored(pattern, "red"))
                        line=line.replace("\n", '')
                        if count == False:
                            if is_file and files_without_match==False:
                                print(line)
                            elif files_without_match==False:
                                print(colored(file_path, "magenta")+":"+line)

        if count:
            if is_file:
                if files_without_match==False:
                    print(nr_of_matches)
            else:
                if files_without_match == False:
                    print(colored(file_path, "magenta")+ ":" + str(nr_of_matches))
        if match==False and files_without_match==True:
            print(colored(file_path, 'magenta'))

    elif os.path.isdir(file_path) and recursive:
        for f in os.listdir(file_path):
            if os.path.isfile(file_path+"\\"+f):
                search(pattern, file_path+"\\"+f, False, regex, recursive, files_without_match, count, ignore_case)
            elif os.path.isdir(file_path+"\\"+f):
                search(pattern, file_path + "\\" + f, False, regex, recursive, files_without_match, count, ignore_case)
    elif os.path.isdir(file_path) and not recursive:
        print("grep: %s: Is a directory" % file_path)
        if count and files_without_match==False:
            print(0)

parser=parser()
arguments=parser.parse_args()
pattern=arguments.pattern
file=arguments.file
is_file=os.path.isfile(file)

search(pattern, file, is_file, arguments.reg, arguments.recursive, arguments.files_without_match, arguments.count, arguments.ignore_case)
