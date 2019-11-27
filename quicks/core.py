import os
import yaml

from jinja2 import Environment, BaseLoader

from quicks.exceptions import PathExistsError

__version__ = '0.0.4'
VERSION = __version__


def get_env():
    return Environment(loader=BaseLoader)


def process_project(env, path, project, template):
    project_path = os.path.join(path, project)
    if os.path.exists(project_path):
        raise PathExistsError

    os.makedirs(project_path)
    project_files, templates, *_ = template
    kwargs = dict(project=project)
    for file in project_files:
        alias = None
        if isinstance(file, list):
            file, alias, *_ = file
        file_template = env.from_string(templates.get(alias or file, '')).render(**kwargs)
        file_name = env.from_string(file).render(**kwargs)
        if not file_name:
            continue
        file_path = os.path.join(project_path, file_name)
        file_dir = os.path.dirname(file_path)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_template)


def parse_template(path):
    with open(path, encoding='utf-8') as f:
        data = yaml.load(f, yaml.FullLoader)

    return data.get('files', []), data.get('templates', {})


__all__ = (
    '__version__',
    'VERSION',
    'get_env',
    'process_project',
    'process_project',
    'parse_template',
)
