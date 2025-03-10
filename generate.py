from pathlib import Path
import json
# from source.controller import Controller
from source.registration import Registration


def run(data_config):
    template_path = current_dir + '/templates'
    release_path = current_dir + '/release'
    """
        Generating registration.php & etc/module.xml
    """
    reg = Registration([data_config['config']['namespace'], data_config['config']['module_name']], template_path, release_path)
    reg.generate()
    """
        Generating schema, interface, model, repository, resource model, collection & grid collection
    """
    # if data['backend-auto-gen']['controller']:
    #     reg = Registration()

def validate_config_file():
    return True


if __name__ == "__main__":
    current_dir = str(Path(__file__).parent)
    file = open(current_dir + '/config.json', "r")
    # Reading from file
    data = json.loads(file.read())
    run(data)
