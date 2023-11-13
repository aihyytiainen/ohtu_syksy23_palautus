class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_(self, text):
        return "\n- "+"\n- ".join(text) if len(text) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors: {self._stringify_(self.authors)}\n"
            f"\nDependencies: {self._stringify_(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._stringify_(self.dev_dependencies)}"
        )
