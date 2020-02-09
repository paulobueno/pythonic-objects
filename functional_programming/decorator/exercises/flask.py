"""
>>> app = Flask()
>>> set(app.paths)
set()
>>> @app.path('/')
... def root():
...     return 'root'
...
>>> set(app.paths)
{'/'}
>>> root()
'root'
>>> app.run('/')
'root'
>>> @app.path('/name')
... def name(user):
...     return f'User name: {user}'
...
>>> list(app.paths)
['/', '/name']
>>> name('Python')
'User name: Python'
>>> app.run('/name', 'Pro')
'User name: Pro'
>>> app.run('/not_a_page',)
404
"""


class Flask:

    def __init__(self):
        self.paths = dict()

    def path(self, path):
        def decorator(f):
            self.paths.update({path: f})
            return f

        return decorator

    def run(self, path, *args, **kwargs):
        if path not in self.paths:
            return 404
        return self.paths[path](*args, **kwargs)
