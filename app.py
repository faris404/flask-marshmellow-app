from models import app,api
from resources.users import *

api.add_resource(Users,'/users')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001,debug=True)