To run this project, just download it and open in code editor.

Then in root directory in terminal type: 
- python -m venv .venv (for windows)
- python3 -m venv .venv (for mac/linux)
to create virtual environment.

Make sure python is installed in your system.

Then activate the virtual environment by typing:
    -  .venv\Scripts\Activate.ps1 (for windows)
    -  source .venv/bin/activate  (for mac/linux)

Then in Project's root directory's terminal type:

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Then in you browser type: http://127.0.0.1:8000/
