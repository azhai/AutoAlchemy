#-*- coding: utf-8 -*-
#For Flask-Alchemy
#使用SqlAutocode，根据数据库已有表，产生符合Flask-SqlAlchemy要求的models的定义

import os.path
from sqlautocode.declarative import name2label
from flask.ext.sqlalchemy import SQLAlchemy
from .flask_factory import FlaskModelFactory


def no_prefix_wrapper(f, prefix=None):
    def _name2label(name, schema=None):
        if schema:
            if name.startswith(schema+'.'):
                name = '.'.join(name.split('.')[1:])
        if prefix and name.startswith(prefix):
            name = name[ len(prefix):]
        label = str(''.join([s.capitalize() for s in
                   re.findall(r'([A-Z][a-z0-9]+|[a-z0-9]+|[A-Z0-9]+)', name)]))
        return label
    return _name2label


def gen_models_dir(app, models_dir):
    #找到并建立models文件夹和__init__.py文件
    if not models_dir:
        app_root = app.config.get('APPLICATION_ROOT', '')
        if not app_root:
            app_root = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) )
        models_dir = os.path.join(app_root, 'models')
    if not os.path.exists(models_dir):
        os.mkdir(models_dir)
    init_file = os.path.join(models_dir, '__init__.py')
    with open(init_file, 'wb') as fh:
        fh.write('#-*- coding: utf-8 -*-\n')
    return models_dir


def write_db_file(db_file):
    #建立数据库定义文件
    with open(db_file, 'wb') as fh:
        fh.write('#-*- coding: utf-8 -*-\n')
        fh.write('\n')
        fh.write('from flask.ext.sqlalchemy import SQLAlchemy\n')
        fh.write('\n\n')
        fh.write('db = SQLAlchemy()\n')


def write_schema_file(factory, schema_file, name='default'):
    #建立数据库定义文件
    with open(schema_file, 'wb') as fh:
        fh.write("#-*- coding: utf-8 -*-\n")
        fh.write('\n')
        fh.write( repr(factory) )
        fh.write('\n')
        fh.write("if __name__ == '__main__':\n")
        if name == 'default':
            fh.write("    db.create_all(bind=None)\n")
        else:
            fh.write("    db.create_all(bind=['%s'])\n" % name)


def generate_models(app, models_dir=None):
    db = SQLAlchemy(app)
    conns = {
        'default': app.config.get('SQLALCHEMY_DATABASE_URI') or {},
    }
    conns.update( app.config.get('SQLALCHEMY_BINDS') or {} )

    models_dir = gen_models_dir(app, models_dir)
    db_file = os.path.join(models_dir, 'db.py')
    if not os.path.exists(db_file):
        write_db_file(db_file)
    for name, conn in conns.items():
        if not conn:
            continue
        schema_file = os.path.join(models_dir, '%s.py' % name)
        if not os.path.exists(schema_file):
            factory = FlaskModelFactory(name, conn)
            write_schema_file(factory, schema_file, name)

