# The Habit Tracker app

This is a habit tracker app that enables a user to track various habits on a daily or weekly basis. The core of the application is implemented as back end django web application and the user interaction is driven through a menu-driven command line interface-based application. All habits are stored in a SqlLite database this could be replaced with a more robust database if required.

The application allows for the following functionality:.

1. Allow the user to create a new habit.
2. Allow the user to update a habit completed.
3. return the longest run streak for a given habit.
4. return a list of all currently tracked habits.
5. return a list of all habits with the same periodicity.
6. return the longest-run streak of all defined habits.
7. list the habits that the user was struggling with.

The database comes with five preloaded habits:.

1. Eat healthy – this is a daily task.
2. Exercise – this is a daily task.
3. Family Time – this is a weekly task.
4. Hobby Time – this is a weekly task.
5. Hygiene – this is a daily task.


## Setting up and running the project.

This application is built using python and will require python 3.9.15 or grater to run.

### Setup.

Install anaconda or python virtual environment, the development for this was done using the anaconda environment to install anaconda follow the steps outlined at the [Annaconda website](https://www.anaconda.com) once installed make sure it is added to your environment, once done create an environment for the project in the following manner:.
open the terminal of choice and type ``conda create -n <your environment name> python=3.9.15`` once this is done create a local directory of your choice once in that directory clone the project using ``git clone https://github.com/cjfarnold/oofppa.git`` once the project is cloned go into the oofppa folder and activate your environment using the following command ``conda activate <your environment name>`` you will observe the name change at the head of the command prompt, next install all the dependencies using this command ``pip install -r requirements.txt`` this will install all the dependent packages to run the application.

### Running the application.

From within the oofppa folder run ``python \habits\manage.py runserver`` this will start the django web server which will be listening on the default port. once you see the server has started, open a new terminal navigate to the project folder next activate the environment as mentioned in the setup section. Once you see the right environment in the command run this command ``python habits\habits\managehabits.py`` this will start the CLI interface, which is driven by an intuitive menu with select options which are easy to use.
