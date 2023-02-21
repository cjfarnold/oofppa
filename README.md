# oofppa
Habit tracker backend app with cli front end

Loading data into the project
(oofppa) PS C:\oofppa\habits> python .\manage.py makemigrations habits
Migrations for 'habits':
  habits\migrations\0001_initial.py
    - Create model habits
    - Create model tracker
    - Create model analytics
(oofppa) PS C:\oofppa\habits> python .\manage.py migrate habits
Operations to perform:
  Apply all migrations: habits
Running migrations:
  Applying habits.0001_initial... OK
(oofppa) PS C:\oofppa\habits> python .\manage.py loaddata habits\data\habits.json
Installed 5 object(s) from 1 fixture(s)