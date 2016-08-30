import configparser
import os

import paction.exc as exc

class ConfigReader(object):
    def __init__(self, action):
       self.action = action
       self.config = configparser.RawConfigParser()
       self.config.optionxform = str

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

    def gather_section(self, section):
        return dict(self.config.items(section))

    # This gathers the input args and replaces them with the data and a type.
    def gather_inputargs(self):
        inputargs = self.inputargs

        i = -1
        for arg in inputargs:
            i = i + 1

            if "optionaldict" in arg:
                odict = {"type": "optionaldict"}
                if arg not in self.optdict:
                    raise exc.ConfigError("%s is not a dictionary" % arg)
                # This gets a dict from the dict section
                odict['data'] = self.gather_section(self.optdict[arg])
                inputargs[i] = odict

            if "string" in arg:
                inputargs[i] = {"type": "string"}

        return inputargs 

    def __iter__(self):
        return self

    def next(self):
        try:
            return self.actions
        except IndexError:
            raise StopIteration()

