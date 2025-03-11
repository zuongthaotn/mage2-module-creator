from pathlib import Path
import json
from source.registration import Registration
from source.schema import Schema
from source.acl import Acl
from source.menu import Menu
from source.controller import Controller
from source.i18n import Translation
from source.ui_component import UiComponent


def run(data_config):
    template_path = current_dir + '/templates'
    release_path = current_dir + '/release'
    _cfg_params = [data_config['config']['namespace'], data_config['config']['module_name'],
                   data_config['config']['interface_name']]
    """
        Generating registration.php & etc/module.xml
    """
    reg = Registration(_cfg_params, template_path, release_path)
    reg.generate()
    """
        Generating schema, interface, model, repository, resource model, collection & grid collection
    """
    if data_config['backend-auto-gen']['schema']:
        sch = Schema(_cfg_params, template_path, release_path)
        sch.generate()
    """
        Generating ACL
    """
    if data_config['backend-auto-gen']['acl']:
        acl = Acl(_cfg_params, template_path, release_path)
        acl.generate()
    """
        Generating controller & routes
    """
    if data_config['backend-auto-gen']['controller']:
        controller = Controller(_cfg_params, template_path, release_path)
        controller.generate()
    """
        Generating menu
    """
    if data_config['backend-auto-gen']['menu']:
        menu = Menu(_cfg_params, template_path, release_path)
        menu.generate()
    """
        Generating i18n
    """
    if data_config['backend-auto-gen']['i18n']:
        i18n = Translation(_cfg_params, template_path, release_path)
        i18n.generate()
    """
        Generating UI Components
    """
    if data_config['backend-auto-gen']['ui-component']:
        ui = UiComponent(_cfg_params, template_path, release_path)
        ui.generate()


def validate_config_file(data_config):
    if not data_config['backend-auto-gen']['acl'] and data_config['backend-auto-gen']['controller']:
        print('The generating Controller process requires the ACL enable.')
        exit()
    if not data_config['backend-auto-gen']['acl'] and data_config['backend-auto-gen']['menu']:
        print('The generating Menu process requires the ACL enable.')
        exit()


if __name__ == "__main__":
    current_dir = str(Path(__file__).parent)
    file = open(current_dir + '/config.json', "r")
    # Reading from file
    data = json.loads(file.read())
    validate_config_file(data)
    run(data)
