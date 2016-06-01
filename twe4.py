import re
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "P1qCE3FHQ8TWEIcXkWgpjFyzE"
csecret = "Vz2b2hCYYDAnc6QgpOLd2iEbjqjtHZdQeksZT7qBhfQ8qsB4qo"
atoken = "731096320363114496-F5AO2abupHUHkeUtSMbgOsTKAqhhNDE"
asecret = "C3exl5tN8A4UuGaZHOSsku6TGVdUucjdbJ5fECRAhwHMb"
#####################################

class listener(StreamListener):     
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            p=re.compile(ur'"Quito"')
            buscar='u'+data
            m=re.findall(p,buscar)
	    if(len(m)==0):
               print len(m)
            else:
               doc = db.save(dictTweet)
               print len(m)
            #print data
	    #print str(data)
            #print "\n\n\n\n\n"
            #print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
    
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('quito')
except:
    db = server['quito']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-78.549929,-0.299805,-78.449678,-0.248479])  #MELBOURNE EAST
