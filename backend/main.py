from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, family, calendar
from database import db

app = FastAPI()

# CORS middleware must be added BEFORE including routers
# Using wildcard for testing - should be restricted in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  # Must be False when using wildcard origins
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

db_connection_status = "successful" if db is not None else "failed"

# Include routers AFTER middleware
app.include_router(auth.router)
app.include_router(family.router)
app.include_router(calendar.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Family App API"}

@app.get("/healthz")
def health_check():
    return {"status": "ok", "db_connection": db_connection_status}