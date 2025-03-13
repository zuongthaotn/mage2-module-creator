import os
import pathlib

DS = '/'
DI_GLOBAL = "di_global.xml"
DI_FRONTEND = "di_frontend.xml"
DI_ADMIN = "di_adminhtml.xml"
DI_SCHEMA = "di_schema.xml"
DI_PLUGIN = "di_plugin.xml"


class Dependency:
    def __init__(self, full_config_data, template_path, release_path):
        self.config = full_config_data
        self.namespace = full_config_data['config']['namespace']
        self.module_name = full_config_data['config']['module_name']
        self.interface_name = full_config_data['config']['interface_name']
        self.interface_name_lower = self.interface_name.lower()
        self.interface_name_upper = self.interface_name.upper()
        self.template_path = template_path
        self.release_path = release_path
        #
        self.schema_di_content = []
        self.plugin_di_content = []

    def generate(self):
        if self.config['backend-auto-gen']['schema']:
            self.generate_di_schema_content()
        if self.config['backend-auto-gen']['plugin']:
            self.generate_di_plugin_content()

        self.generate_global_di_file() \
            .generate_frontend_di_file() \
            .generate_adminhtml_di_file()

    def generate_file(self, file_template, file_release, release_folder):
        is_file = os.path.isfile(file_template)
        if is_file:
            pathlib.Path(release_folder).mkdir(parents=True, exist_ok=True)
            with open(file_template, "rt") as fin:
                with open(file_release, "wt") as fileout:
                    for line_content in fin:
                        if line_content.strip() == '{{schema_di_content}}':
                            for schema_content in self.schema_di_content:
                                fileout.write(schema_content)
                        elif line_content.strip() == '{{plugin_di_content}}':
                            for plugin_content in self.plugin_di_content:
                                fileout.write(plugin_content)
                        else:
                            fileout.write(line_content)

    def generate_di_plugin_content(self):
        file_template = self.template_path + DS + DI_PLUGIN
        is_file = os.path.isfile(file_template)
        if is_file:
            with open(file_template, "rt") as fin:
                for line in fin:
                    new_line_content = line.replace('{{namespace}}', self.namespace) \
                        .replace('{{module_name}}', self.module_name) \
                        .replace('{{interface_name}}', self.interface_name)
                    self.plugin_di_content.append(new_line_content)

    def generate_di_schema_content(self):
        file_template = self.template_path + DS + DI_SCHEMA
        is_file = os.path.isfile(file_template)
        if is_file:
            with open(file_template, "rt") as fin:
                for line in fin:
                    new_line_content = line.replace('{{namespace}}', self.namespace) \
                        .replace('{{module_name}}', self.module_name) \
                        .replace('{{interface_name}}', self.interface_name) \
                        .replace('{{interface_name_lower}}', self.interface_name_lower) \
                        .replace('{{interface_name_upper}}', self.interface_name_upper)
                    self.schema_di_content.append(new_line_content)

    def generate_global_di_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + DS + 'etc'
        file_release = release_folder + DS + 'di.xml'
        file_template = self.template_path + DS + DI_GLOBAL
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_frontend_di_file(self):
        return self

    def generate_adminhtml_di_file(self):
        return self
