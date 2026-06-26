from pathlib import Path

repo = Path('.')

for f in repo.rglob('*.py'):
    print(f)

