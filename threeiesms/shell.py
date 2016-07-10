import configparser
import os
import requests
import six
import sys

class ThreeIeSms(object):
    def main(self, argv):
         action = "%s.cfg" % argv.pop(0)

         config = configparser.RawConfigParser()
         if config.read([action, os.path.expanduser('~/%s' % action)]) == []:
             raise NameError('Config file not found')

         print(config.sections())

def check_string(data):
    if isinstance(data, six.string_types):
        return data
    raise TypeError("Not a string")

def main():
    try:
        argv = [check_string(a) for a in sys.argv[1:]]
        ThreeIeSms().main(argv)
    except Exception as e:
        print e

if __name__ == "__main__":
   main()
