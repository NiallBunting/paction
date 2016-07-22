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

         self.config = configparser.RawConfigParser()
         if self.config.read([action, os.path.expanduser('~/%s' % action)]) == []:
             raise NameError('Config file not found')

         if not self.config.has_section("main"):
             raise NameError("Config has no main section")

         inputargs, actions, dicts = self.gather_main()
         # sort out inputs match them
         # get login pages
         # check input matches
         # do dictionarys
         # make sessions

    def get_type(self, options, keyword):
        match = []
        for key in options:
            if keyword in key[0]:
                match.append(key)
        return match

    def get_type_and_validate(self, section, keyword):
        items = self.config.items(section)
        matches = self.get_type(items, keyword)
        for match in matches:
            if not self.config.has_section(match[1]):
                raise IndexError("%s section does not exist" % match[1])
        return matches

    def gather_main(self):

        # Get actions and validate
        actions = dict(self.get_type_and_validate("main", "action"))
        # Get optdict and validate
        optdict = dict(self.get_type_and_validate("main", "optionaldict"))

        inputargs = self.config.get("main", "inputargs").split()

        for arg in inputargs:
            if "optionaldict" in arg:
                if arg not in optdict:
                    raise IndexError("%s is not a dictionary" % arg)

        return inputargs, actions, optdict

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
