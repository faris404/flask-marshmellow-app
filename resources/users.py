from flask_restful import Resource
from flask import jsonify
from models import User,Book,db
from schema.schema import *


class Users(Resource):

   def get(self):
      user_schema = UserSchema(many=True)
      book_shema = BookSchema(many=True)
      user_book_schema = UserBookSchema(many=True)
      # data = Book.query.all() 
      # data = User.query.all()
      data = (
         db.session.query(
            Book.name.label('book_name'),User.name.label('user_name'),
            User.email
         ).
         outerjoin(User,User.id==Book.user_id).all()
      )
      # data = db.engine.execute('select book.name as book_name,user.name as user_name from book left join user on book.user_id=user.id').fetchall()
      # res = book_shema.dump(data)
      res = user_book_schema.dump(data)
 
      return jsonify(res)

