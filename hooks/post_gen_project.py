import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_user_app = '{{cookiecutter.user_app}}' == 'y'

if not create_user_app:
    remove('apps/user')
