#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
from cmd_runner import runner
from kube_client import client
from chart_utils import chart_reader
from test_checks import exit_code_check, k8s_resource_check

def main():
    """ Main entry point of the app """
    # logger.info("hello world")
    chart = chart_reader.ChartReader("testdata/nodejs-ex-k")
    resources = chart.read_resources()
    cmd = runner.Runner("helm install testdata/nodejs-ex-k --generate-name")
    output = cmd.run()
    for line in output.stdout.readlines():
        print(line)
    actual = {'exit_code': output.returncode}
    expected = {'exit_code': 0, 'resources': resources}
    e = exit_code_check.ExitCodeCheck(actual= actual, expected= expected)
    print(e.check())

    rc = k8s_resource_check.K8SResourceCheck(actual, expected)
    rc.check()


    # c = chart_reader.ChartReader("testdata/nodejs-ex-k")
    # c.read_templates()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
