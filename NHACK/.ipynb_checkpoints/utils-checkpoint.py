import os

import pkg_resources
import yaml

# Define the base path for the package
base_path = os.path.dirname(os.path.dirname(
    pkg_resources.resource_filename("NHACK", 'config')))

# Define the path to the config file
pkg_yaml = os.path.join(base_path, 'config', 'config.yml')

# Define the paths to the subdirectories
p_paths = dict()

# Loop through the subdirectories and define the paths, then add them to the dict
for el in ['data', 'docs', 'results', 'scripts', 'tests']:
    p_paths['{el}_dir'.format(el=el)] = os.path.join(base_path, el)


def load_pkg_yaml(pkg_yaml=pkg_yaml, **kwargs):
    """_summary_

    Args:
        pkg_yaml (_type_, optional): The path to the package config yaml. Defaults to pkg_yaml.

    Returns:
        A dictionry containing the information in the package config file.
    """

    with open(pkg_yaml, 'r') as f:
        y = yaml.safe_load(f)

        # Add the paths to the config dict
        y['p_paths'] = p_paths

    if 'subdict' in kwargs.keys():
        return y[kwargs['subdict']]
    else:
        return y
