#!/usr/bin/env python

from decouple import config
from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from strawberry.fastapi import GraphQLRouter
from app.schema import schema
from pathlib import Path
from strawberry.fastapi import GraphQLRouter

templates_dir = Path(__file__).resolve().parents[1] / 'templates'
templates = Jinja2Templates(directory=templates_dir)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
