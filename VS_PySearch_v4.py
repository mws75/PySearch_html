#V4 - Fullworking Version
#V5 - Improve
import os
import sys
from bs4 import BeautifulSoup

def walkTree(fileList, dpath="C:\\Users\\Michael.Spencer\\Documents\\MyApps\\PySearch"):
    
    '''Walking the directory tree to find html docs''' 
    for f in os.listdir(dpath):
        fpath = os.path.join(dpath, f)
        if fpath.find("Search_Results") != -1:
            continue
        elif os.path.isfile(fpath)==True:
            if is_html(f): 
                print("Is html: ", f)
                fileList.append(fpath)
            else: 
                pass
        elif os.path.isdir(fpath)==True:
            dirname = fpath
            walkTree(fileList, dirname)
        else:
            pass
            
    return fileList

def is_html(fname):
    '''is the file HTML?'''
    if fname[-4:]=="html":
        return True
    else: 
        return False

def scrape_for_docName(html_doc):
    data = open(html_doc, "r")
    soup = BeautifulSoup(data, "html.parser")
    docNames = soup.find_all("td", class_="doc_name")
    #print("html doc names: ", docNames)
    return docNames

def user_key_word():
    key_word = input("Search for: ")
    return key_word

def key_word_found(key_word, html_string):
    return html_string.find(key_word)

def save_as_html(txt_file):
    print("Hi")

def main():
    print("Running V4")
    my_fileList = list()

    #gather html files
    html_files = walkTree(my_fileList)
    #print("html files: ", html_files)
    

    #Creat path for Result Set
    user_search = user_key_word()
    result_file_path = "Search_Results\\" + user_search + "_Result_Set.html"
    result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), result_file_path) #Creating File Path for Result Set
    print("Result_file name: ", result_file)
    if os.path.exists(result_file):
        os.remove(result_file)
    else:
        pass
    #Scrape HTML files for keyword
    count = 0
    for html_doc in html_files:
        html_result_set = scrape_for_docName(html_doc)
        with open(result_file, "a") as tf:
            for i in html_result_set:
                count += 1
                if count == 1:
                    tf.write('''<!DOCTYPE html> \n
<html lang='en'> \n
<head> \n
<meta charset="utf-8"/> \n
<link rel="stylesheet" href="../css/styles.css"/> \n
</head> \n
<body> \n
<table class ="answer">
<tr class="table_header">
<th>Results</th>
</tr> \n''')
                elif key_word_found(user_search.lower(), str(i).lower()) != -1:
                    tf.write("<tr> \n " + str(i) + '\n' + "</tr> \n")
                    print("Matches Keyword: ", i)
                else: 
                    pass
            tf.close()
    tf = open(result_file, "a")
    tf.write("</table></body></html>")
    tf.close()

#add_table_tag("Instruction_html_txt.txt")
#print_lines("Instruction_html_txt.txt")
main()

