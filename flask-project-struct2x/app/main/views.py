from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    #return redirect(url_for('.index'))
    #return render_tmplate('index.html',form=form, name=session.get('name'),known=session.get('known', False),current_time=datetime.utcnow())
    return "Hello Flask!2"
