import os
import pathlib

DS = '/'
DB_SCHEMA = "db_schema.xml"
DB_SCHEMA_WHITELIST = "db_schema_whitelist.json"
REPOSITORY_INTERFACE = "RepositoryInterface.php"
INTERFACE = "Interface.php"
SEARCH_RESULT_INTERFACE = "SearchResultsInterface.php"
MODEL = "Model.php"
REPOSITORY = "Repository.php"
RESOURCE_MODEL = "ResourceModel.php"
COLLECTION = "Collection.php"
GRID_COLLECTION = "GridCollection.php"


class Schema:
    def __init__(self, config, template_path, release_path):
        self.namespace = config[0]
        self.module_name = config[1]
        self.interface_name = config[2]
        self.interface_name_lower = self.interface_name.lower()
        self.interface_name_upper = self.interface_name.upper()
        self.template_path = template_path
        self.release_path = release_path

    def generate(self):
        self.generate_schema_files() \
            .generate_api_interface_file() \
            .generate_api_data_interface_files() \
            .generate_model_file() \
            .generate_repository_file() \
            .generate_resource_model_file() \
            .generate_collection_file() \
            .generate_grid_collection_file()

    def generate_schema_files(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + DS + 'etc'
        file_template = self.template_path + DS + DB_SCHEMA
        file_release = release_folder + DS + DB_SCHEMA
        self.generate_file(file_template, file_release, release_folder)
        #
        file_whitelist_template = self.template_path + DS + DB_SCHEMA_WHITELIST
        file_whitelist_release = release_folder + DS + DB_SCHEMA_WHITELIST
        self.generate_file(file_whitelist_template, file_whitelist_release, release_folder)
        #
        return self

    def generate_api_interface_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + DS + 'Api'
        file_release = release_folder + DS + self.interface_name + REPOSITORY_INTERFACE
        file_template = self.template_path + DS + REPOSITORY_INTERFACE
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_api_data_interface_files(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + DS + 'Api' + DS + 'Data'
        file_release = release_folder + DS + self.interface_name + INTERFACE
        file_template = self.template_path + DS + INTERFACE
        self.generate_file(file_template, file_release, release_folder)
        #
        file_search_result_release = release_folder + DS + self.interface_name + SEARCH_RESULT_INTERFACE
        file_search_result_template = self.template_path + DS + SEARCH_RESULT_INTERFACE
        self.generate_file(file_search_result_template, file_search_result_release, release_folder)
        return self

    def generate_model_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + DS + 'Model'
        file_release = release_folder + DS + self.interface_name + '.php'
        file_template = self.template_path + DS + MODEL
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_repository_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name + DS + 'Model'
        file_release = release_folder + DS + self.interface_name + 'Repository.php'
        file_template = self.template_path + DS + REPOSITORY
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_resource_model_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name \
                         + DS + 'Model' + DS + 'ResourceModel'
        file_release = release_folder + DS + self.interface_name + '.php'
        file_template = self.template_path + DS + RESOURCE_MODEL
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_collection_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name \
                         + DS + 'Model' + DS + 'ResourceModel' + DS + self.interface_name
        file_release = release_folder + DS + 'Collection.php'
        file_template = self.template_path + DS + COLLECTION
        self.generate_file(file_template, file_release, release_folder)
        return self

    def generate_grid_collection_file(self):
        release_folder = self.release_path + DS + self.namespace + DS + self.module_name \
                         + DS + 'Model' + DS + 'ResourceModel' + DS + self.interface_name + DS + 'Grid'
        file_release = release_folder + DS + 'Collection.php'
        file_template = self.template_path + DS + GRID_COLLECTION
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
