import yaml


def open_yaml_to_dict(file_path):
    """
    Opens the YAML file and converts it to Python dictionary
    :param str file_path: Path of the YAML file
    :return dict: Python dictionary form of the YAML file
    """
    with open(file_path, 'r') as file:
        yaml_file_as_dict = yaml.safe_load(file)

    return yaml_file_as_dict


def get_extends_template(yaml_dict):
    """
    Gets the "template" value from the "extends" key
    :param dict yaml_dict: YAML file in dictionary format
    :return:
    """

    return yaml_dict.get("extends").get("template")


def foobar():
    return 1


def flask_landing():
    return "yamlparsing landing"


y = open_yaml_to_dict("sample.yaml")
print(get_extends_template(y))