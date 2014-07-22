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

	#	<Vars>
	returnTag = {}
	tagData = []
	tagDataName = []
	isName = True
	nameKey = ""
	#	</Vars>

	### Initial checking
	if source[index] != "<":
		### Don't return a false tag
		return ("No Tag at index %s" % str(index))
	else:
		### Retrieve only the tag, and add the index at which the tag is found in the source
		tag = retrieveTag(source,index)
		tag = tag.split()

	### Split the tags apart
	for i in range(len(tag)):
		### Loop through chars in the tag
		for char in tag[i]:
			### Change to inputting data rather than name variables.
			if char == "=" and isName:
				isName = False
			### Record char to the name field (i.e. this is the name of the tag modifier [e.g. id = "John" will save 'id'])
			elif isName:
				tagDataName.append(char)
			### Record char to the data field (i.e. this is what the tag modifier contains [e.g. id = "Geoff" will save '"Geoff"'])
			elif not isName:
				tagData.append(char)
		else:
			### Flush to dict
			returnTag["".join(tagDataName)] = "".join(tagData)
			### Reset buffer variables
			tagData = []
			tagDataName = []
			isName = True

	# <Housekeeping> (changing '<tagName' to 'name = tagName' and removing the self closing tag.)
	### Search for name key
	for key in returnTag:
		if key[0] == "<":
			nameKey = key

	### Remove '<' in name, and place under 'name' key
	if nameKey != "":
		del returnTag[nameKey]
		nameKey = nameKey[1:]
		returnTag['name'] = nameKey
		### Reset nameKey variable
		nameKey = ""

	### Search for empty keys
	for key in returnTag:
		if key[len(key)-1] == ">":
			nameKey = key

	### Remove '>' at end of tag close
	if nameKey != "":
		returnTag[nameKey[:len(nameKey)-1]] = returnTag[nameKey]
		del returnTag[nameKey]
	
	### Remove self-closing tag
	if "/>" in returnTag:
		del returnTag["/>"]
	# </Housekeeping>

	### Final return
	return returnTag

#	</Functions>

#	<Methods>
#url = getURL()
url = "http://cracked.com"
source = prettySource(getSource(url))
#print(source)
saveFile(source, "source")
print("\n\n\n")
print (str(retrieveTagData(source, 738)))
print("/tag")
#search = searchForTag(source, "div", 1)
#print (search)
#saveFile(search, "search")
input()
#	</Methods>
