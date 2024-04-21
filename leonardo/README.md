alembic revision --autogenerate -m "Added prompt table"

alembic upgrade head

python .\db\seed.py
