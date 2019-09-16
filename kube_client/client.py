from kubernetes import client, config
from openshift.dynamic import DynamicClient
import yaml

class Client:
    def __init__(self):
        conf = config.new_client_from_config("/Users/akash/kubeconfig")
        self.dyn_client = DynamicClient(conf)

    def initialize_client(self):
        v1_pods = self.dyn_client.resources.get(api_version='v1', kind='Service')
        pods = v1_pods.get(name="", namespace="")
        print(pods.attributes)

c = Client()
c.initialize_client()
