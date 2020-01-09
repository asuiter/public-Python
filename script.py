import os
import pandas
from pathlib import Path


#Get user input for Album ID and make sure it is valid
while True:
    user_input = input('Enter AlbumId Number 1-100:')
    try:
        value = int(user_input)
    except:
        print('This is not a valid number, Please enter a number 1-100')
        continue
    if value < 1:
        print('Please enter a number 1-100')
        continue
    if value > 100:
        print('Please enter a number 1-100')
        continue
    break

#Convert user_input to str
x = str(value)

#Get link to photo album from URL + User input
def get_photo_album_link(x):
    url = 'https://jsonplaceholder.typicode.com/photos?albumId='
    newurl = url+x
    return newurl
link = get_photo_album_link(x)

#Open the link using Pandas
def open_link_in_pandas(link):
    djson = pandas.read_json(link)
    return djson
djson = open_link_in_pandas(link)

#Create a new column converting thumbnailUrl to HTML
def thumbnailurl_to_html(djson):
    djson['Thumbnail Image'] = djson['thumbnailUrl']\
        .str.replace(
            '(.*)',
            '<img src="\\1" style="max-height:150px;"></img>'
        )
    return djson
djson2 = thumbnailurl_to_html(djson)

#Format pandas table by removing columns
def format_pandas_table(djson2):
    djson3 = djson.drop("thumbnailUrl","columns")
    djson4 = djson3.drop("albumId","columns")
    djson5 = djson4.drop("url","columns")
    return djson5
djsonfinal = format_pandas_table(djson2)

#Convert pandas table to HTML Code
def convert_pandas_html(djsonfinal):
    djsonhtml = djsonfinal.to_html(escape=False)
    return djsonhtml
djsonhtml = convert_pandas_html(djsonfinal)

#Get filepath to viewer.html
f= Path.cwd()
def get_viewer_file_path(f):
    while True:
        a = str(f)
        try:
             a.index("/")
             fpath = a + "/"+"viewer.html"
             return fpath
        except:
            fpath = a+"\\"+"viewer.html"
            return fpath
        break
    return fpath
fpath = get_viewer_file_path(f)

#Write pandas table to html file
def write_html_to_viewer(fpath):
    viewerfile = open(fpath,'w')
    viewerfile.write(djsonhtml)
    viewerfile.close()
write_html_to_viewer(fpath)



