import configparser
import os

import paction.exc as exc

class ConfigReader(object):
    def __init__(self, action):
       self.action = action
       self.config = configparser.RawConfigParser()
       self.i = 0

       if self.config.read([action, os.path.expanduser('~/%s' % action)]) == []:
           raise exc.ConfigError('Config file not found')

       if not self.config.has_section("main"):
           raise exc.ConfigError("Config has no main section")

       self.__gather_main()

    def __get_type(self, options, keyword):
        match = []
        for key in options:
            if keyword in key[0]:
                match.append(key)
        return match

    def __get_type_and_validate(self, section, keyword):
        items = self.config.items(section)
        matches = self.__get_type(items, keyword)
        for match in matches:
            if not self.config.has_section(match[1]):
                raise exc.ConfigError("%s section does not exist" % match[1])
        return matches

    def __gather_main(self):

        # Get actions and validate
        self.actions = dict(self.__get_type_and_validate("main", "action"))
        # Get optdict and validate
        self.optdict = dict(self.__get_type_and_validate("main", "optionaldict"))

        self.inputargs = self.config.get("main", "inputargs").split()

        for arg in self.inputargs:
            if "optionaldict" in arg:
                if arg not in optdict:
                    raise exc.ConfigError("%s is not a dictionary" % arg)

    def __iter__(self):
        return self

    def next(self):
        try:
            self.actions[self.i]
        except IndexError:
            raise StopIteration()

        self.i += 1
