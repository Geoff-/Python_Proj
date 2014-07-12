#	<Imports>
from urllib.request import urlopen
#	</Imports>

#	<Functions>
def getURL():
	### Gets a URL from the user, and turns it in the appropriate format (string)

	#	<Vars>
	urlIn = input("Enter a URL to get the source of:")
	url = []
	#	</Vars>

	for char in urlIn:
		url.append(char)

	if len(urlIn) < 8:
		url.insert(0,"http://")

	elif not (urlIn[0:7] == "http://"):
		url.insert(0,"http://")

	return "".join(url)

def getSource(url):
	### Gets the source from a given URL using the urllib.request library
	sock = urlopen(url)
	source = sock.read()
	sock.close()
	return source

def prettySource(source):
	### Prettifies the source, changing /t, /r, /n etc into their respective characters

	#	<Vars>
	returnSource = []
	source = str(source)
	ignoreNext = False
	#	</Vars>

	for i in range(len(source)):
		if str(source[i]) == '\\' and not ignoreNext:
			nextChar = source[i+1]
			if nextChar == 'n':
				returnSource.append('\n')
				ignoreNext = True
			elif nextChar == 't':
				returnSource.append('\t')
				ignoreNext = True
			elif nextChar == '\'':
				returnSource.append('\'')
				ignoreNext = True
			elif nextChar == 'r':
				returnSource.append('\r')
				ignoreNext = True
			else:
				returnSource.append('\\')
				ignoreNext = False
		elif not ignoreNext:
			returnSource.append(str(source[i]))
		#	ignoreNext = False
		else:
			ignoreNext = False
	# Remove the 'b and ' from the start and end of the file
	returnSource.pop(0)
	returnSource.pop(0)
	returnSource.pop(len(returnSource) - 1)
	return "".join(returnSource)

def saveFile(text, fileName):
	### Saves text into a file, with the name given
	file = open(str(fileName) + ".html","w")
	file.write(text)
	file.close()
	return

def removeChar(text, remChar):
	### Removes all instances of remChar from text
	#	<Vars>
	returnText = []
	#	</Vars>
	for char in source:
		if char == str(remChar):
			continue
		else:
			returnText.append(char)
	return "".join(returnText)
"""
def searchForTag(source,tag,iterations):
	### Searches for a tag, and returns its contents. Will search for the tag for as many iterations as required.
	#	<Vars>
	tags = {}
	# Return variable
	returnTags = []
	#	</Vars>
	for i in range(source):
"""

def retrieveTag(source,index):
	### Retrieves a tag from a HTML source starting at a given index
	#	<Vars>
	returnTag = []
	#	</Vars>
	if source[index] != "<":
		return ("No Tag at index %s" % str(index))
	for i in range(index, len(source)):
		if source[i] == ">":
			returnTag.append(">")
			return "".join(returnTag)
		else:
			returnTag.append(source[i])

def retrieveTagData(source,index):
	### Retrieves a tag's data, and returns it as a python dictionary (for easy access and readability)
	## BUGGY
	#	<Vars>
	returnTag = {}
	tagData = []
	tagDataName = []
	isName = True
	#	</Vars>

	### Initial checking
	if source[index] != "<":
		### Don't return a false tag
		return ("No Tag at index %s" % str(index))
	else:
		### Retrieve only the tag, and add the index at which the tag is found in the source
		tag = retrieveTag(source,index)
		returnTag['indexInSource'] = index

	### Retrieves the tag name
	for i in range(1,len(tag)):
		### Stop when encountering any of these closing symbols
		if tag[i] == " " or tag[i] == ">" or tag[i] == "\n" or tag[i] == "/":
			returnTag['_Name'] = "".join(tagData)
			tagData = []
			break
		else:
			tagData.append(tag[i])

	### Adds information as to if the tag is closing
	if tag[len(tag)-2] == "/":
		returnTag['_Closing'] = True
	else:
		returnTag['_Closing'] = False

	### If there is no other data, then return the dict now
	if (" " not in tag) or ("\n" not in tag):
		return returnTag

	### Retrieves data from within the tag
	i = 1 + len( returnTag[_Name] )
	while i < len(tag):
		###
		if tag[i] == ">" or tag[i:i+1] == "/>":
			### Flush tag to dictionary
			returnTag[ str(tagDataName) ] = str(tagData)
			tagDataName = []
			tagData = []
			### Exit loop
			break
		elif tag[i] == "/n" and not isName:
			isName = True
			### Flush tag to dictionary
			returnTag[ str(tagDataName) ] = str(tagData)
			tagDataName = []
			tagData = []
			# Increment
			i += 1
		elif tag[i] == "=" and isName:
			### Move to input tag data
			isName = False
			# Increment
			i += 1
			continue
		elif tag[i] == " " and not isName:
			isName = True
			### Flush tag to dictionary
			returnTag[ str(tagDataName) ] = str(tagData)
			tagDataName = []
			tagData = []
			# Increment
			i += 1
			continue
		### Continually append data to tagData and tagDataName (unless continue statement is reached above)
		if isName:
			tagDataName.append( tag[i] )
		else:
			tagData.append( tag[i] )
		# Increment
		i += 1


	### Return dict
	if '' in returnTag:
		del returnTag['']
	elif '/' in returnTag:
		del returnTag['/']
	return returnTag



#	</Functions>

#	<Methods>
#url = getURL()
url = "http://cracked.com"
source = prettySource(getSource(url))
#print(source)
saveFile(source, "source")
print("\n\n\n")
print (str(retrieveTagData(source, 189)))
print("/tag")
#search = searchForTag(source, "div", 1)
#print (search)
#saveFile(search, "search")
input()
#	</Methods>
