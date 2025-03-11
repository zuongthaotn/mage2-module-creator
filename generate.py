from pathlib import Path
import json
# from source.controller import Controller
from source.registration import Registration
from source.schema import Schema


def run(data_config):
    template_path = current_dir + '/templates'
    release_path = current_dir + '/release'
    """
        Generating registration.php & etc/module.xml
    """
    reg = Registration([data_config['config']['namespace'], data_config['config']['module_name']], template_path,
                       release_path)
    reg.generate()
    """
        Generating schema, interface, model, repository, resource model, collection & grid collection
    """
    if data['backend-auto-gen']['schema']:
        sch = Schema([data_config['config']['namespace'], data_config['config']['module_name'],
                      data_config['config']['interface_name']], template_path, release_path)
        sch.generate()


def validate_config_file():
    return True


if __name__ == "__main__":
    current_dir = str(Path(__file__).parent)
    file = open(current_dir + '/config.json', "r")
    # Reading from file
    data = json.loads(file.read())
    run(data)
