# import module
import codecs
import webbrowser

# to open/create a new html file in the write mode
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html> 
<head> 
<title>Title</title> 
</head> 
<body> 
<h2>Welcome To GFG</h2> 

<p>Default code has been loaded into the Editor.</p> 

</body> 
</html> 
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()

file = codecs.open("GFG.html", 'r', "utf-8")

# using .read method to view the html
# code from our object
print(file.read())

webbrowser.open('GFG.html')