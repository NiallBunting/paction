import requests

class ActionTaker(object):
    def __init__(self, argv, configreader):
         # sort out inputs match them
         # get login pages
         # check input matches
         # do dictionarys
         # make sessions
        self.configreader = configreader
        self.argv = self.format_args(argv)
        self.session = requests.Session()

    def do_action(self, action):
        url, method, data = self.format_data(**self.configreader.gather_section(action))
        r = self.session.request(method=method, url=url, data=data, allow_redirects=False)

        print(vars(r.request))
        print(r.status_code)
        print(r.text)

    def format_data(self, url, method="POST", **kwargs): 
        for arg in kwargs:
            kwargs[arg] = self.replace_with_args(kwargs[arg])
        return url, method, kwargs

    def replace_with_args(self, arg):
        if "input_" in arg:
            number = arg.split("_")[1]
            return self.argv[int(number) - 1]
        return arg

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
