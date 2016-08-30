import requests


class ActionTaker(object):
    def __init__(self, argv, configreader):
        self.configreader = configreader
        self.argv = self.format_args(argv)
        self.session = requests.Session()

    # Ran with each action. Tests to see if values need inserting.
    # Then calls the requests.
    def do_action(self, action):
        url, method, data = self.format_data(
            **self.configreader.gather_section(action))
        self.session.request(method=method, url=url,
                             data=data, allow_redirects=False)

    def format_data(self, url, method="POST", **kwargs):
        for arg in kwargs:
            kwargs[arg] = self.insert_cli_args(kwargs[arg])
        return url, method, kwargs

    # If varible has input_ within it it gets replaced with the data
    # provided when calling paction.
    def insert_cli_args(self, arg):
        if "input_" in arg:
            number = arg.split("_")[1]
            return self.argv[int(number) - 1]
        return arg

    # This replaces the cli arguments/combines them as requried.
    # This means they are ready to be replaced when needed by the inserter.
    def format_args(self, argv):
        inputtypes = self.configreader.gather_inputargs()
        arg_count = 0
        data = []

        for intype in inputtypes:
            if "optionaldict" in intype['type']:
                try:
                    data.append(intype['data'][argv[arg_count]])
                except KeyError:
                    print("Does not match with optional dictionary")
                    data.append(argv[arg_count])

            if "string" in intype['type']:
                data.append(" ".join(argv[arg_count:]))

            arg_count = arg_count + 1

        return data
