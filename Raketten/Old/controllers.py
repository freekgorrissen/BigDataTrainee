from endpoints import Controller
import os

class Default(Controller):
  def GET(self):
    return "boom"

  def POST(self, **kwargs):
    return 'hello {}'.format(kwargs['name'])

class Foo(Controller):
  def GET(self):
    return "bang"

class Bar(Controller):
  def GET(self, **kwargs):
    return 'hello {}'.format(kwargs['name'])

# cmdfoo   = 'curl http://localhost:8000/foo'
# cmdbar   = 'curl http://localhost:8000/ -d "name=Awesome you"'
# cmdstart = 'endpoints --prefix=controllers --host=localhost:8000'
#
# os.system(cmdstart)
#
