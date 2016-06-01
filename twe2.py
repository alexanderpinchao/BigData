import re
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "HkjiqFb3cx2NnyeuMIHcTR3RR"
csecret = "NbtNgeZt9STDZCzJf9ayfR09Qf3CFLcun75fCFzMxiTBG6B2UI"
atoken = "731096320363114496-uIzxxfsUbP488HKJVKI6iF52WtDlIJO"
asecret = "JjIxReJJz8h49UnvfuU8UEtygNDq0MmrJbo5J2kO32IVP"
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

twitterStream.filter(locations=[-78.519888,-0.200071,-78.449678,-0.148229])  #MELBOURNE EAST
