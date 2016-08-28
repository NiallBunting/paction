import requests

class ActionTaker(object):
    def __init__(self, argv, configreader):
         # sort out inputs match them
         # get login pages
         # check input matches
         # do dictionarys
         # make sessions
        self.argv = argv
        self.configreader = configreader
        self.session = requests.Session()

    def doaction(self, action):
        pass
