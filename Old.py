'''
#    <Google_Code>
#        <Imports>
import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
#       </Imports>

FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret can be found in Google Developers Console
FLOW = OAuth2WebServerFlow(
    client_id='971063755527-c6shkf8c1g2dlokt06vlhk0a5rdmsjjd.apps.googleusercontent.com',
    client_secret='qYS57RocriWWX4izecsu03b4',
    scope='https://www.googleapis.com/auth/calendar',
    user_agent='smhw-to-email/0.1')

# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage('calendar.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google Developers Console
# to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http,
       developerKey='AIzaSyBxKjxxczVIVX-bMXxir0t0pq6HqGoUoMk')
#   </Google Code>
'''

from urllib.request import urlopen

url = "http://" + str( input( "Enter a URL to gather the source of (the bit after http://, without www.):" ) )
sock = urlopen(url)
source = sock.read()
sock.close()

def parseUrll(source):
    string = []
    source = str(source)
    ignoreNext = False
    for i in range(len(source)):
        if str(source[i]) == '\\' and not ignoreNext:
            if str(source[i+1]) == 'n':
                string.append('\n')
                ignoreNext = True
            elif str(source[i+1]) == 't':
                string.append('\t')
                ignoreNext = True
            elif str(source[i+1]) == '\'':
                string.append('\'')
                ignoreNext = True
            elif str(source[i+1]) == 'r':
                string.append('\r')
                ignoreNext = True
            else:
                string.append("\\")
                ignoreNext = False
        elif not ignoreNext:
            string.append(str(source[i]))
            ignoreNext = False
        else:
            ignoreNext = False
    return "".join(string)

#print (source)
string = parseUrll(source)
print (string)
input()
