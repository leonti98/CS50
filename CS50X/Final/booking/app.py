from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from datetime import datetime
import sqlite3
from sqlite3 import Error

from helpers import SQL


conn = sqlite3.connect('example.db')

db = conn.cursor()

db.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")


conn.commit()
conn.close()


