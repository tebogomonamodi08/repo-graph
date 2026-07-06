from pathlib import Path
import ast


class FileAnalyzer:
    def __init__(self, path: Path):
        self.path = path

    def analyze(self):
        try:
            source = self.path.read_text(encoding="utf-8", errors="ignore")
            tree = ast.parse(source)

            data = {
                "file": str(self.path),
                "imports": [],
                "classes": [],
                "functions": [],
            }

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):
                    for alias in node.names:
                        data["imports"].append(alias.name)

                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        if module:
                            data["imports"].append(f"{module}.{alias.name}")
                        else:
                            data["imports"].append(alias.name)

                elif isinstance(node, ast.ClassDef):
                    data["classes"].append(node.name)

                elif isinstance(node, ast.FunctionDef):
                    data["functions"].append(node.name)

            return data

        except SyntaxError:
            return None

        except Exception as e:
            print(f"Error reading {self.path}")
            print(e)
            return None


class RepoGraph:

    def __init__(self, root):
        self.root = Path(root)

    def scan(self):
        if not self.root.exists():
            raise FileNotFoundError(f"{self.root} does not exist.")

        if not self.root.is_dir():
            raise NotADirectoryError(f"{self.root} is not a directory.")

        return list(self.root.rglob("*.py"))

    def analyze(self):

        files = self.scan()

        print(f"\nFound {len(files)} Python files.\n")

        repository = []

        for file in files:
            analyzer = FileAnalyzer(file)
            result = analyzer.analyze()

            if result:
                repository.append(result)

        return repository


def report(repository):

    print("=" * 60)
    print("REPOGRAPH REPORT")
    print("=" * 60)

    print(f"Python Files : {len(repository)}")

    imports = sum(len(f["imports"]) for f in repository)
    classes = sum(len(f["classes"]) for f in repository)
    functions = sum(len(f["functions"]) for f in repository)

    print(f"Imports      : {imports}")
    print(f"Classes      : {classes}")
    print(f"Functions    : {functions}")

    print()

    for file in repository:

        print("-" * 60)
        print(file["file"])

        if file["imports"]:
            print("Imports:")
            for i in file["imports"]:
                print(f"  - {i}")

        if file["classes"]:
            print("Classes:")
            for c in file["classes"]:
                print(f"  - {c}")

        if file["functions"]:
            print("Functions:")
            for f in file["functions"]:
                print(f"  - {f}")

        print()


def main():

    repo = input("Repository path: ").strip().strip('"')

    graph = RepoGraph(repo)

    repository = graph.analyze()

    report(repository)


if __name__ == "__main__":
    main()

