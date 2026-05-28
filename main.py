from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import psycopg2

app = FastAPI()

templates = Jinja2Templates(directory="templates")

conn = psycopg2.connect(
    host="db.udsqqzlijvkypxbbepxf.supabase.co",
    port="5432",
    database="postgres",
    user="postgres",
    password="Dillip@2004@"
)

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
        request=request,
        name="dashboard.html",
        context={}
    )