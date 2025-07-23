## Work Schedule Generator in Python

This project is an automated work schedule generator developed in Python, with Excel export support. It allows you to create customized weekly schedules, including rules such as fixed weekly days off and a 2x1 Sunday rotation (work two, rest one).

About the Project
This tool was created as a custom solution for a supermarket chain, developed as a professional freelance project. The goal was to automate schedule creation, reducing manual effort and eliminating process errors.

The implementation of this project delivered visible results: increased operational efficiency, improved HR team organization, and faster and more reliable processes.

Features
Schedule Generation: Creates weekly/monthly schedules based on configurable parameters.

Fixed Day Off: Allows selecting a fixed weekly day off (default is Monday).

2x1 Sunday Rule: Works two consecutive Sundays and rests on the third.

Excel Export: Generates a .xlsx file with a clear and shareable layout.

How It Works
The script generates the schedule based on:

employee_name: Name of the employee

start_date: Start date of the schedule

weeks: Number of weeks to cover

fixed_day_off: Fixed day off (optional; default = Monday)

2x1 Sunday Rule: Applied automatically

Prerequisites
Python 3
Libraries:

pip install pandas openpyxl

How to Use
Clone the repository:

git clone https://github.com/archivesysl/escala-em-python-p-mercado.git
cd escala-em-python-p-mercado

Configure the parameters in gerador_escala.py:

employee_name = "João"
start_date = "2024-10-01"
weeks = 4


Run the script:
python gerador_escala.py

Check the escala_trabalho.xlsx file generated in the same directory.

Customization
employee_name: Change the name as needed

start_date: Set the desired start date

weeks: Adjust the duration of the schedule

fixed_day_off: Choose a different day off

The 2x1 logic for Sundays is already included.

Technologies Used
Python 3
Pandas
Openpyxl

Results Achieved
✅ Fully automated schedule creation
✅ Elimination of manual errors
✅ Easy to use for non-technical teams
✅ Modular code, ready for future adaptations

Author
Natan Da Luz – Developer
Contact: natandaluz01@gmail.com

Project developed as a freelance job for process automation in a supermarket chain.
