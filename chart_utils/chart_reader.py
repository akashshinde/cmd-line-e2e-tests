import os
from kube_client import read_resource
from array import array

class ChartReader:
    def __init__(self, chart_dir):
        self.chart_dir = chart_dir

    def read_chart(self):
        for f in os.listdir(self.chart_dir):
            print(f)

    def template_path(self):
        return self.chart_dir + "/templates"

    def read_resources(self):
        resources = self.read_templates()
        return resources

    def read_templates(self):
        exist = os.path.exists(self.template_path())
        lst = []
        if exist:
            for resource in os.listdir(self.template_path()):
                if resource.endswith(".yaml"):
                    resource_reader = read_resource.ReadResource()
                    content = resource_reader.read(open(os.path.join(self.template_path(), resource)))
                    lst.append(content)
        return lst

# c = ChartReader("../testdata/nodejs-ex-k")
# c.read_resources()