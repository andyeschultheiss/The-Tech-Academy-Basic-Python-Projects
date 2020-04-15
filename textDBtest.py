## Title: txtDBtest.py
##
## Author: Andy Schultheiss
##
## Date: 15 April 2020
##
## Description: Simple script to scan a file list for ".txt" files and add those filenames
##              to a database, then print those filenames to the console
##
## Python: 3.8.2
##

import sqlite3

# sample file list provided
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

def txt_scan(list_of_files):
    txt_files = []
    for entry in list_of_files:
        if entry.endswith('.txt'):
            txt_files.append(entry)
    return txt_files

def create_txt_table(txt_files):
    # create database, enter relevant data
    conn = sqlite3.connect('db_txt_test.db')

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS \
                     tbl_txt_files( \
                     ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                     col_filename TEXT \
                     )")
        for entry in txt_files:
            cur.execute("INSERT INTO tbl_txt_files(col_filename) VALUES (?)", (entry,))
        conn.commit()
    conn.close() 

def print_txt_filenames():

    print('List of .txt files:')

    conn = sqlite3.connect('db_txt_test.db')

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_filename FROM tbl_txt_files WHERE col_filename LIKE '%.txt'")
        varFilename = cur.fetchall()
        for item in varFilename:
            itemStr = str(item)
            itemStr = itemStr.rstrip(',)').lstrip('(')
            print(itemStr)
        conn.commit()
    conn.close()

if __name__ == "__main__":
    txt_files = txt_scan(fileList)
    create_txt_table(txt_files)
    print_txt_filenames()
    
    
