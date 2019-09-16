import subprocess


class Runner:
    def __init__(self, cmd):
        self.cmd = cmd
        pass

    def run(self):
        p = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env={'KUBECONFIG': '/Users/akash/kubeconfig'})
        p.wait()
        return p
