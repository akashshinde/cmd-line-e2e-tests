from test_checks import base_check
from kube_client import client


class K8SResourceCheck(base_check.BaseCheck):
    def __init__(self, expected, actual):
        super().__init__(expected, actual)

    def check(self):
        resources = self.actual['resources']
        cli = client.Client()
        for r in resources:
            dyn_res = cli.dyn_client.resources.get(api_version=r['apiVersion'], kind=r['kind'])
            try:
                present = dyn_res.get(name=r['metadata']['name'], namespace=r['metadata']['name'])
                print("Resource is present ", present)
            except:
                print("Resource does not exist")
