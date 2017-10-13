from flask import Blueprint, render_template, redirect, url_for

# todo: from models import *

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return 'hello wurld'

