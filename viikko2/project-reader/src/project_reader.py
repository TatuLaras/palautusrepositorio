from urllib import request
from project import Project
import toml
from pprint import pprint


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        content = toml.loads(content)
        poetry = content["tool"]["poetry"]

        name = poetry["name"]
        description = poetry["description"]
        dependencies = poetry["dependencies"].keys()
        dev_dependencies = poetry["group"]["dev"]["dependencies"].keys()

        project_license = poetry["license"]
        authors = poetry["authors"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            name, description, dependencies, dev_dependencies, project_license, authors
        )
