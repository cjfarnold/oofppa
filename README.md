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

### 1 Setup.

This project was developed using the Annoconda distribution of Python. Annaconda could be installed form [Annaconda website](https://www.anaconda.com). Once the installation is done use the following steps to setup the environment.
1. Start bash or command prompt
2. Navigate to the folder where you wand to checked out this project
    ```sh
     # Clone the project using 
     git clone https://github.com/cjfarnold/oofppa.git
    ```
3. Execute the follwing commands
    ```sh
        conda create -n <your environment name> python=3.9.15
        conda activate <your environment name>
        pip install -r requirements.txt
    ```
4. This completes the setup of the project

### 2 Running the application.
Once you are within the oofppa project folder and your setup is done. Execute the following commands in the same order to start using the application
1. The application has two componentes 1. the Back end service running Django and 2. the user interface using a command line based navigation menu
2. Start the application. note if you have multiple python version start the server using python3.9
    ```sh
        python3.9 \habits\manage.py runserver
    ```
    This starts the Django services
3. Next open a new command prompt or bash, navigate to the folder and activate your environment
    ```sh
        conda activate <your environment name>
        python3.9 \habits\habits\managehabits.py
    ```
4. This will start the application menu which can be used to perform varrious operation on the application 

### 3 Running test cases

The appllication comes with a pytest driven test cases, this test cases added a new habit with name "daily_t" updates the habit, checks if the streak are computed accurately and finally removes all the records pertaining to the "daily_t" habit from the database
The test cases are configured to be discovered automatically when pytest is invoked. Below screenshot shows the test cases being executed. 
![alt tag](https://github.com/cjfarnold/oofppa/tree/main/habits/images/pytest.png "Screen shot of the test cases being run") 
