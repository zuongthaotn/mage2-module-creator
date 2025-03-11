import os
import pathlib

DS = '/'
REGISTRATION = 'registration.php'
MODULE = 'module.xml'


class Registration:
    def __init__(self, config, template_path, release_path):
        self.namespace = config[0]
        self.module_name = config[1]
        self.template_path = template_path
        self.release_path = release_path

    def generate(self):
        self.generate_registration_file()
        self.generate_module_xml_file()

    def generate_registration_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name
        file_release = release_folder + DS + REGISTRATION
        file_template = self.template_path + DS + REGISTRATION
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_module_xml_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + DS + 'etc'
        file_release = release_folder + DS + MODULE
        file_template = self.template_path + DS + MODULE
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
                            .replace('{{module_name}}', self.module_name)
                        fileout.write(new_line_content)
