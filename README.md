# How to start
1. Clone repository to your computer
```commandline
git clone (link)
```
2. Create virtual environment
```commandline
python -m venv venv
```
3. Activate and install requirements
```commandline
source venv/Scripts/activate
pip install -r requirements.txt
```
4. Run postgres
```commandline
docker-compose run --build
```
5. Run django server
```commandline
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
6. Load data
```commandline
python manage.py save_to_db
```
