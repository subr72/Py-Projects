#=================================================================
#EXANPLE
#First, create file pic.json and put in your  text ASCII format
#Then, create(or download) a file with code(below), such as main.py or convert.py
#Put your file and program on Desktop(or in any other folder)
#Start program, and wait...
#Done! Your code was saved at output.json
#==================================================================

import os
import time
import math
print("  .--.    .----. .----. .-. .-.   .-----.  .---.    .----.  .---.  .----.  .----. ")
print(" / {} \  { {__-` | }`-' { | { |   `-' '-' / {-. \   | }`-' / {-. \ } {-. \ } |__} ")
print("/  /\  \ .-._} } | },-. | } | }     } {   \ '-} /   | },-. \ '-} / } '-} / } '__} ")
print("`-'  `-' `----'  `----' `-' `-'     `-'    `---'    `----'  `---'  `----'  `----' ")
print("                                                                                  ")
print(".----.  .---.  .-. .-. .-.   .-..----. .---.  .-----. .----. .---.  ")
print("| }`-' / {-. \ |  \{ |  \ \_/ / } |__} } }}_} `-' '-' } |__} } }}_} ")
print("| },-. \ '-} / | }\  {   \   /  } '__} | } \    } {   } '__} | } \  ")
print("`----'  `---'  `-' `-'    `-'   `----' `-'-'    `-'   `----' `-'-'  ")
print("                                                                    ")
print(".----.  .-.  .-.    .----. .-. .-. .----.  .---.  .---.  .---.  ")
print("| {_} }  \ \/ /    { {__-` | } { | | {_} } } }}_} `-`} } `-`} } ")
print("| {_} }   `-\ }    .-._} } \ `-' / | {_} } | } \    / /  { {.-. ")
print("`----'      `-'    `----'   `---'  `----'  `-'-'   `-'    `---' ")
print("                                                                ")
print("Created by ASCIItoCODE Converter by SUBR72")
time.sleep(5)
def getSize():
    fileinfo = os.stat("pic.json")
    if fileinfo.st_size >= 5:
        return True

def convertate():
    filetext_new = []
    filetext_end = []
    i = 0
    j = 0
    progress = 0
    if getSize() == True:
        print("Convertation started")
        file = open("pic.json")
        filetext = file.read()
        filetext_new = filetext.split("\n")
        while i != len(filetext_new):
            tmptext = 'print("' + filetext_new[i]  + '")' + "\n"
            filetext_end.append(tmptext)
            i += 1
            progress += 1
            time.sleep(0.01)
            pcents = (progress*100)/len(filetext_new)
            pcents = math.floor(pcents)
            print("Progress: " + str(pcents) + "%")
            if i == len(filetext_new):
                filetext_end.append('print("Created by ASCIItoCODE Converter by SUBR72")')
                file_new = open("output.json","w")
                while j != len(filetext_end):
                    file_new.write(filetext_end[j])
                    j += 1
                    if j == len(filetext_end):
                        file.close()
                        file_new.close()
                        print("Convertation end")
breakpoint()

def main():
    convertate()

if __name__ == "__main__":
    main()
