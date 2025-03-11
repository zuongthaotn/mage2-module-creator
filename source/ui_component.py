import os
import pathlib

DS = '/'
LAYOUT = 'ui_index_layout.xml'
UI_LISTING = 'ui_component_listing.xml'
DATA_PROVIDER = 'UiDataProvider.php'
ACTION = 'UiActions.php'
STATUS_SOURCE = 'SourceIsEnable.php'


class UiComponent:
    def __init__(self, config, template_path, release_path):
        self.namespace = config[0]
        self.module_name = config[1]
        self.module_name_lower = self.module_name.lower()
        self.interface_name = config[2]
        self.interface_name_lower = self.interface_name.lower()
        self.interface_name_upper = self.interface_name.upper()
        self.template_path = template_path
        self.release_path = release_path

    def generate(self):
        self.generate_layout_file() \
            .generate_ui_listing_file()\
            .generate_data_provider_file()\
            .generate_action_file()\
            .generate_source_status_file()

    def generate_layout_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'view' + DS + 'adminhtml' + DS + 'layout'
        file_release = release_folder + DS + self.module_name_lower + '_' + self.interface_name_lower + '_index.xml'
        file_template = self.template_path + DS + LAYOUT
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_ui_listing_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'view' + DS + 'adminhtml' + DS + 'ui_component'
        file_release = release_folder + DS + self.module_name_lower + '_' + self.interface_name_lower + '_listing.xml'
        file_template = self.template_path + DS + UI_LISTING
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_data_provider_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'Ui' + DS + 'Component'
        file_release = release_folder + DS + 'DataProvider.php'
        file_template = self.template_path + DS + DATA_PROVIDER
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_action_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'Ui' + DS + 'Component' + DS + 'Listing' + DS + 'Column'
        file_release = release_folder + DS + self.interface_name + 'Actions.php'
        file_template = self.template_path + DS + ACTION
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_source_status_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'Model' + DS + self.interface_name + DS + 'Source'
        file_release = release_folder + DS + self.interface_name + 'IsEnable.php'
        file_template = self.template_path + DS + STATUS_SOURCE
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_file(self, file_template, file_release, release_folder):
        is_file = os.path.isfile(file_template)
        if is_file:
            pathlib.Path(release_folder).mkdir(parents=True, exist_ok=True)
            with open(file_template, "rt") as fin:
                with open(file_release, "wt") as fileout:
                    for line in fin:
                        new_line_content = line.replace('{{namespace}}', self.namespace) \
                            .replace('{{module_name}}', self.module_name) \
                            .replace('{{module_name_lower}}', self.module_name_lower) \
                            .replace('{{interface_name}}', self.interface_name) \
                            .replace('{{interface_name_lower}}', self.interface_name_lower) \
                            .replace('{{interface_name_upper}}', self.interface_name_upper)
                        fileout.write(new_line_content)
