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

Default habits
• Eat healthy – this is a daily task
• Exercise – this is a daily task
• Family Time – this is a weekly task
• Hobby Time – this is a weekly task
• Hygiene – this is a daily task

Success criteria
• Allow the user to create a new habit - Done
• Allow the user to update habit completed - Done
• return the longest run streak for a given habit. - to Test
• return a list of all currently tracked habits, - Done
• return a list of all habits with the same periodicity, - WIP
• return the longest run streak of all defined habits,
• return the longest run streak for a given habit.

o list the successful streak for specified habit
o list all currently tracked habits
o list of all habits with the same periodicity - Tracker table where the start data and end date are the same with the same type
o list the successful streak across all habits - Analysis table where streak = true
o list longest run streak for a given habit - Analysis table where the duration is the most
o list of the habits where the user was struggling with - habits where there is no streak or least streaks 