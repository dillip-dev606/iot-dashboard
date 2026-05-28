from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import psycopg2

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# SUPABASE SESSION POOLER URI
DATABASE_URL = "postgresql://postgres.udsqqzlijvkypxbbepxf:[YOUR-PASSWORD]@aws-1-ap-northeast-1.pooler.supabase.com:5432/postgres"

# Database connection
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()


@app.get("/")
def home():
    return {
        "message": "IoT Dashboard API Running"
    }


@app.get("/latest")
def latest():

    cursor.execute(
        """
        SELECT temperature, humidity, created_at
        FROM sensor_data
        ORDER BY created_at DESC
        LIMIT 1
        """
    )

    row = cursor.fetchone()

    if row is None:
        return {
            "message": "No sensor data found"
        }

    return {
        "temperature": row[0],
        "humidity": row[1],
        "created_at": str(row[2])
    }


@app.get("/history")
def history():

    cursor.execute(
        """
        SELECT temperature, humidity, created_at
        FROM sensor_data
        ORDER BY created_at DESC
        LIMIT 20
        """
    )

    rows = cursor.fetchall()

    data = []

    for row in reversed(rows):
        data.append({
            "temperature": row[0],
            "humidity": row[1],
            "time": str(row[2])
        })

    return data


@app.get("/dashboard")
def dashboard(request: Request):

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request
        }
    )