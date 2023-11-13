## Virtual environment:

* Before creating a Django project, it's a good practice to create a virtual
  environment for it. This isolates project's dependencies from the system-wide
  Python installation. Go to the terminal and run the command:
  <br>'python -m venv venv_name'
* Activate the virtual environment (on Windows):
  <br>`venv_name\Scripts\activate`
* When you're done working on your project, deactivate the virtual
  environment:
  <br>`deactivate - exits venv`
* !!! PyCharm provides an option to automatically activate the virtual
  environment associated with a project whenever you open a terminal within the
  IDE.
  <br>`File>Settings>Tools>Terminal>Activate virtualenv` (check/uncheck)
* Whenever you want to continue working on your project, activate the virtual
  environment first:
  `venv_name\Scripts\activate`
* While your virtual environment is active, install Django and supporting 
  packages to start working on the project.
<br>[Back to top ⇧](#table-of-contents)