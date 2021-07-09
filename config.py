
class DevelopmentConfig():
   TESTING = True
   UPLOAD_FOLDER = '/uploads'
   SQLALCHEMY_DATABASE_URI = 'mysql://faris404:12345678@localhost/test1'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   


class ProductionConfig():
   TESTING = True
   SQLALCHEMY_DATABASE_URI = 'mysql://root:dotdash01@localhost/test2'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
