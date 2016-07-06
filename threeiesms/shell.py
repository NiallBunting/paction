import requests
import sys
#from oslo_utils import encodeutils

class ThreeIeSms(object):
    def main(self):
        loginurl = ""
        loginpayload = {"": "",
                   "": ""}
        actionurl = ""
        actionpayload = {"": "",
                   "": ""}
        session = requests.Session()
        session.post(loginurl, data=loginpayload)
        session.post(actionurl, data=actionpayload)
def main():
    try:
        #argv = [encodeutils.safe_decode(a) for a in sys.argv[1:]]
        ThreeIeSms().main()
    except Exception as e:
        print e
