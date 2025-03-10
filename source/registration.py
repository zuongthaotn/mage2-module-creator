import os
import pathlib


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
        file_template = self.template_path + '/registration.templ'
        release_folder = self.release_path + '/' + self.namespace + '/' + self.module_name
        file_release = release_folder + '/registration.php'
        is_file = os.path.isfile(file_template)
        if is_file:
            pathlib.Path(release_folder).mkdir(parents=True, exist_ok=True)
            with open(file_template, "rt") as fin:
                with open(file_release, "wt") as fileout:
                    for line in fin:
                        new_line_content = line.replace('{{namespace}}', self.namespace)\
                                                .replace('{{module_name}}', self.module_name)
                        fileout.write(new_line_content)

    def generate_module_xml_file(self):
        file_template = self.template_path + '/module.templ'
        release_folder = self.release_path + '/' + self.namespace + '/' + self.module_name + '/etc'
        file_release = release_folder + '/module.xml'
        is_file = os.path.isfile(file_template)
        if is_file:
            pathlib.Path(release_folder).mkdir(parents=True, exist_ok=True)
            with open(file_template, "rt") as fin:
                with open(file_release, "wt") as fileout:
                    for line in fin:
                        new_line_content = line.replace('{{namespace}}', self.namespace) \
                            .replace('{{module_name}}', self.module_name)
                        fileout.write(new_line_content)