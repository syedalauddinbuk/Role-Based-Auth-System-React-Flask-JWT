from flask import Flask
from flask_cors import CORS
from .extensions import db, jwt
from config import Config