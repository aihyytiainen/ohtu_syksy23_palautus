from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        #print(toml.loads(content))
        toml_parse = toml.loads(content)
        name = toml_parse['tool']['poetry']['name']
        description = toml_parse['tool']['poetry']['description']
        license = toml_parse['tool']['poetry']['license']
        dependencies = toml_parse['tool']['poetry']['dependencies']
        dev = toml_parse['tool']['poetry']['group']['dev']['dependencies']
        license = toml_parse['tool']['poetry']['license']
        authors = toml_parse['tool']['poetry']['authors']
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev, license, authors)
