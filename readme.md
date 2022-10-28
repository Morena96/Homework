create a new project directory for our code on the Desktop
create a new virtual environment called .venv and activate it
install requirements.txt

% cd ~/desktop/
% mkdir project
% cd project
% git clone https://github.com/Morena96/Homework.git
% python3 -m venv .venv
% source .venv/bin/activate
(.venv) % pip3 install -r requirements.txt
(.venv) % python manage.py runserver

navigate to http://localhost:8000 you'll see the project welcome screen

admin url: http://localhost:8000/admin
user:       dovlet
password:   homework