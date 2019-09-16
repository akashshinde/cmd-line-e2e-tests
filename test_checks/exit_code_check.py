from test_checks import base_check


class ExitCodeCheck(base_check.BaseCheck):
    def __init__(self, expected, actual):
        base_check.BaseCheck.__init__(self, expected, actual)

    def check(self):
        return self.expected['exit_code'] == self.actual['exit_code']
