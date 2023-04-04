import os
import yaml

# These vars are the paths to a specific YML file
CREDENTIALS = "credentials.yml"


# This function is used to read data inside the YML [file_name] that is specified
def read_file(file_name):
    if "tests" in os.path.abspath(os.curdir):
        os.chdir("..")
    with open(os.path.join(os.path.abspath(os.curdir), "test_data/", file_name)) as f:
        return yaml.safe_load(f)
