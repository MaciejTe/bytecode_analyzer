

class Parser(object):
    def __init__(self, text):
        self.text = text

    def parse_time_output(self):
        """
        Parse Linux time output.
        :return: output_dict (dict)
        """
        text_list = list(self.text.split('\n'))
        text_list = [line.strip() for line in text_list]
        output_dict = dict()
        for line in text_list:
            if line.find(':') > 0:
                output_dict[line[0:line.find(': ')]] = line.lstrip()[line.find(': ') + 2:]
        return output_dict
