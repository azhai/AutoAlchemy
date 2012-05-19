#-*- coding: utf-8 -*-

__version__ = '0.1'

#For Flask-Alchemy
from .flask import generate_models, no_prefix_wrapper, name2label
"""
import os.path
from flask import Flask

if __name__ == '__main__':
    import sys
    sys.path.append(
        os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) )
    )
    app = Flask(__name__)
    app.config.from_object('settings')
    name2label = no_prefix_wrapper(name2label, app.config.get('TABLE_PREFIX',''))
    generate_models(app)
"""
