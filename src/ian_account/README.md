# ian_account

IAN reusable Django Auth App. It is a conventional Django App.

This App works well with the IAN Django Template.


#### Structure
This app contains the following features:

1. Custom User Model

2. Filters
3. Serializers
4. Signals
5. Tasks
6. Utils
7. Views
8. Auth Templates


#### Usage

1. Within the root folder of your project, run
        
        git submodule add https://github.com/Impact-Africa-Network/ian-account src/ian_account

2. Add `"ian_account"` to `INSTALLED_APPS` section.

        INSTALLED_APPS = [
            ...,
            "ian_account",
        ]


*DISCLAIMER:*

It is assumed that the (1) command above is run within a project adhering to the `ian-django-template` structure. If your project follows a different path, make sure to tweak the command as appropriate, ensuring to replace the `src` bit with the appropriate path.
