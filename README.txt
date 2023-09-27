#создаём витуал окруж
& C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe -m venv venv m venv venv
#activdet
venv/scripts/activate


python -m pip install --upgrade pip

pip install django

#создаём проектdjango-admin startprojec
t store_project

cd store_project

python manage.py startapp store



#создаём вспомогательные таблицы в базе данных
python manage.py migrate

#запускаем сервер
python manage.py runserver
 #изминения структуры данных
 Python manage.py makemigrations
 python manage.py migrate 

 рег
 python manage.py createsuperuser
 

 pip install 

#создаём фаил с зависимости
pip freeze >requirements.txt