"""
, implement a program that prompts the user for the name of a file and then outputs
 that file’s media typeif the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output
 application/octet-stream instead, which is a common default.
"""
file = input('File Name: ').lower().strip()

if file.endswith('.gif'):
    print('image/gif')
elif file.endswith('.jpeg'):
    print('image/jpeg')
elif file.endswith('.png'):
    print('image/png')
elif file.endswith('.pdf'):
    print('image/pdf')
elif file.endswith('.txt'):
    print('image/txt')
elif file.endswith('.zip'):
    print('image/zip')
else:
    print('application/octet-stream')