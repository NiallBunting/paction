import six
import sys

import paction.configreader
import paction.actiontaker


class Paction(object):
    def main(self, argv):
        try:
            action = "%s.cfg" % argv.pop(0)
        except IndexError:
            raise IndexError('TODO print help')

        configreader = paction.configreader.ConfigReader(action)
        actiontaker = paction.actiontaker.ActionTaker(argv, configreader)

        for action in configreader.next():
            actiontaker.do_action(action)


# Make sure it is of type string
def check_string(data):
    if isinstance(data, six.string_types):
        return data
    raise TypeError("Not a string")


def main():
    try:
        argv = [check_string(a) for a in sys.argv[1:]]
        Paction().main(argv)
    except Exception as e:
        print("Error %s" % e.message)

if __name__ == "__main__":
    main()
