class Project:
    def __init__(
        self, name, description, dependencies, dev_dependencies, license, authors
    ):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_list(self, lst):
        string = ""

        for item in lst:
            string += f"\n- {item}"

        return string

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: {self._stringify_list(self.authors)}"
            f"\n\nDependencies: {self._stringify_list(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_list(self.dev_dependencies)}"
        )
