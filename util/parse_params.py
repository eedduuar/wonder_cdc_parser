import argparse


class Params():
    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description=description)
        self.requiredNamed = self.parser.add_argument_group('required named arguments')

        self.parser.add_argument('-output',
                                 action="store",
                                 dest="output",
                                 default='/tmp/data.csv',
                                 help="output path, default /tmp/data.csv", required=False)

        self.requiredNamed.add_argument('-mode',
                                        action="store",
                                        dest="mode",
                                        default='test',
                                        help="mode: last_week | weekly | yearly | test",
                                        required=False)

        self.requiredNamed.add_argument('-input_file',
                                        action="store",
                                        dest="input_file",
                                        default='/tmp/data.csv',
                                        help="in mode yearly send input data",
                                        required=False)

        self.parser.add_argument('-base_url',
                                 action="store",
                                 dest="base_url",
                                 default='https://wonder.cdc.gov/mmwr/mmwr_reps.asp?mmwr_year=%d&mmwr_week=%s&mmwr_table=2G&request=Export&mmwr_location=',
                                 help="base url from wonder.cdc.gov",
                                 required=False)

        self.arguments, self.extra = self.parser.parse_known_args()

    def base_url(self):
        return self.arguments.base_url

    def output(self):
        return self.arguments.output

    def mode(self):
        return self.arguments.mode

    def input_file(self):
        return self.arguments.input_file
