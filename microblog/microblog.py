#!/usr/bin/env python3
'''main microblog app
'''
from mainapp import app, db
import sqlalchemy as sa
import sqlalchemy.orm as so
from mainapp.models import User, Post


@app.shell_context_processor
def make_shell_context():
    ''' flask shell context
    '''
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)
