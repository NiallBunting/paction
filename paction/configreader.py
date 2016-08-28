import configparser
import os

import paction.exc as exc

class ConfigReader(object):
    def __init__(self, action):
       self.action = action
       self.config = configparser.RawConfigParser()

       if self.config.read([action, os.path.expanduser('~/%s' % action)]) == []:
           raise exc.ConfigError('Config file not found')

       if not self.config.has_section("main"):
           raise exc.ConfigError("Config has no main section")

       self.__gather_main()

    # Returns a list of the options containing the keyword.
    def __get_type(self, options, keyword):
        match = []
        for key in options:
            if keyword in key[0]:
                match.append(key)
        return match

    # Checks section provided for values containing the keyword.
    # Then checks any values for there own section in the config file.
    # Currently orders them based on order in config file.
    def __get_type_and_validate(self, section, keyword):
        items = self.config.items(section)
        matches = self.__get_type(items, keyword)
        for match in matches:
            if not self.config.has_section(match[1]):
                raise exc.ConfigError("%s section does not exist" % match[1])
        return matches

    def __gather_main(self):

        # Get actions and validate
        actions = self.__get_type_and_validate("main", "action")
        self.actions = [action[1] for action in actions]

        # Get optdict and validate
        self.optdict = dict(self.__get_type_and_validate("main", "optionaldict"))

        self.inputargs = self.config.get("main", "inputargs").split()

        for arg in self.inputargs:
            if "optionaldict" in arg:
                if arg not in self.optdict:
                    raise exc.ConfigError("%s is not a dictionary" % arg)

    def __iter__(self):
        return self

    def next(self):
        try:
            return self.actions
        except IndexError:
            raise StopIteration()

