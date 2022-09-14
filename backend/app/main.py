from fastapi import FastAPI, HTTPException, status
from starlette.middleware.cors import CORSMiddleware

# FastAPI
app = FastAPI()

# CORS
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)
