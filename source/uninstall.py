import os
import pathlib

DS = '/'
UNINSTALL = 'Uninstall.php'


class Uninstall:
    def __init__(self, config, template_path, release_path):
        self.namespace = config[0]
        self.module_name = config[1]
        self.interface_name = config[2]
        self.interface_name_lower = self.interface_name.lower()
        self.interface_name_upper = self.interface_name.upper()
        self.template_path = template_path
        self.release_path = release_path

    def generate(self):
        self.generate_acl_file()

    def generate_acl_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'Setup'
        file_release = release_folder + DS + UNINSTALL
        file_template = self.template_path + DS + UNINSTALL
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
                            .replace('{{interface_name}}', self.interface_name) \
                            .replace('{{interface_name_lower}}', self.interface_name_lower) \
                            .replace('{{interface_name_upper}}', self.interface_name_upper)
                        fileout.write(new_line_content)
