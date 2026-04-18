# fullypack_fastapi

## Setup
Setup your virtual environment and install packages
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a file in the root called `.env`, and paste this:
```
APP_NAME="fullypack_fastapi"
DATABASE_URL="postgresql://user:password@localhost:5432/fullypack_fastapi"
```

## Run

```bash
fastapi dev app
```

## Database Migrations

```bash
alembic revision --autogenerate -m "migration message"
alembic upgrade head
```
