# Quicks

Project generator

```
pip install quicks

quicks PROJECT_NAME example.yml
```

example.yml Jinja2 style

```yaml
files:
  - '{{project}}/__init__.py'
  - '{{project}}/__main__.py'
  - '{{project}}/requirements.txt'
  - '.gitignore'
  - 'LICENSE'
  - 'Dockerfile'
  - 'README.md'

templates:
  'README.md': |
    # {{project}}
```