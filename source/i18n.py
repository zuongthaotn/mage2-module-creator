import os
import pathlib

DS = '/'


class Translation:
    def __init__(self, config, template_path, release_path):
        self.namespace = config[0]
        self.module_name = config[1]
        self.interface_name = config[2]
        self.interface_name_lower = self.interface_name.lower()
        self.interface_name_upper = self.interface_name.upper()
        self.template_path = template_path
        self.release_path = release_path

    def generate(self):
        self.generate_i18n_file()

    def generate_i18n_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'i18n'
        file_release = release_folder + DS + 'en_US.csv'
        pathlib.Path(release_folder).mkdir(parents=True, exist_ok=True)
        with open(file_release, "wt") as fileout:
            new_line_content = '"Enabled", "Enabled" \n'
            fileout.write(new_line_content)
