import os
import pathlib

DS = '/'
CRON_XML = 'crontab.xml'
CRON_PHP = 'TestCron.php'


class Crontab:
    def __init__(self, config, template_path, release_path):
        self.namespace = config[0]
        self.namespace_lower = self.namespace.lower()
        self.module_name = config[1]
        self.module_name_lower = self.module_name.lower()
        self.interface_name = config[2]
        self.interface_name_lower = self.interface_name.lower()
        self.interface_name_upper = self.interface_name.upper()
        self.template_path = template_path
        self.release_path = release_path

    def generate(self):
        self.generate_crontab_file() \
            .generate_cron_execution_file()

    def generate_crontab_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'etc'
        file_release = release_folder + DS + CRON_XML
        file_template = self.template_path + DS + CRON_XML
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_cron_execution_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + \
                         DS + 'Cron'
        file_release = release_folder + DS + CRON_PHP
        file_template = self.template_path + DS + CRON_PHP
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
                            .replace('{{namespace_lower}}', self.namespace_lower) \
                            .replace('{{module_name}}', self.module_name) \
                            .replace('{{module_name_lower}}', self.module_name_lower)
                        fileout.write(new_line_content)
