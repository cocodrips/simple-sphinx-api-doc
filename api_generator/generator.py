import pathlib
import yaml


class RstGenerator():
    def __init__(self, yaml_path='autodoc.yml'):
        with open(yaml_path, "r") as f:
            self.define = yaml.load(f)
        
        default = self.define['autodoc']['default']
        default_style = default['style']
        self.style = {
            'h1': default_style.get('h1', "==================================\n"),
            'h2': default_style.get('h2', "----------------------------------\n"),
            'generate': default['generate']
            
        }

if __name__ == '__main__':
    gen = RstGenerator(yaml_path='api_generator/autodoc.yml')
    print(gen.style)

def init_module_file():
    pass


def walk_packages(module_path, src_dir, doc_dir):
    """
    Look for every file in the directory tree and create the corresponding
    ReST files.
    """

    with open("autodoc.yml", "r") as f:
        define = yaml.load(f)

    src_dir_path = pathlib.Path(src_dir)

    doc_dir_path = pathlib.Path(doc_dir)
    doc_dir_path.mkdir(exist_ok=True, parents=True)

    modules_file = doc_dir_path / 'modules.rst'
    with open(modules_file, 'w') as f:
        f.write(module_path + '\n')
        f.write(h1)
        f.write("""
.. toctree::
    :maxdepth: 4

""")

    def new_package(package_name):
        with open(doc_dir_path / f'{package_name}.rst', 'w') as f:
            f.write(f'{package_name}\n')
            f.write(h1)

        with open(modules_file, 'a') as f:
            f.write(f'    {package_name}\n')

    def new_doc(module_path):
        package_path = module_path.parent
        module_name = f"{package_path}.{module_path.stem}"

        if str(package_path) == '.':
            package_path = module_path.stem
            module_name = f"{module_path.stem}"
        else:
            with open(doc_dir_path / f'{package_path}.rst', 'a') as f:
                f.write(f'{module_name}\n')
                f.write(h2)

        with open(doc_dir_path / f'{package_path}.rst', 'a') as f:
            f.write(f"""
.. automodule:: {module_name}
    :members:
    :undoc-members:
    :show-inheritance:
""")

    # Create file
    for path in src_dir_path.glob('*.py'):
        if path.name.startswith('__init__'):
            continue
        new_package(path.relative_to(src_dir_path).stem)

    for path in src_dir_path.glob('**/*'):
        if not path.is_dir():
            continue

        if path.match('__pycache__'):
            continue

        module_path = path.relative_to(src_dir_path)
        new_package(module_path)

    for path in pathlib.Path(src_dir).glob('**/*.py'):
        if path.name == '__init__.py':
            continue
        module_path = path.relative_to(src_dir_path)
        new_doc(module_path)


# def main():
#     modules = walk_packages('sample package', 'sample_package', 'doc')


# if __name__ == '__main__':
#     main()
