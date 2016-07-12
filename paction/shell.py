import configparser
import os
import requests
import six
import sys

class Paction(object):
    def main(self, argv):
         try:
             action = "%s.cfg" % argv.pop(0)
         except IndexError:
             raise IndexError('TODO print help')

         config = configparser.RawConfigParser()
         if config.read([action, os.path.expanduser('~/%s' % action)]) == []:
             raise NameError('Config file not found')

         if not config.has_section("main"):
             raise NameError("Config has no main section")

         self.gather_main(config)
         # sort out inputs match them
         # get login pages
         # check input matches
         # do dictionarys
         # make sessions

    def gather_main(self, config):
        options = config.options("main")
        # get actions
          # validate they exist
        # get cli
          # mark as inputs


def check_string(data):
    if isinstance(data, six.string_types):
        return data
    raise TypeError("Not a string")

def main():
    try:
        argv = [check_string(a) for a in sys.argv[1:]]
        Paction().main(argv)
    except Exception as e:
        raise
        print e

if __name__ == "__main__":
   main()
