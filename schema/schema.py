
from models import * 
from marshmallow_sqlalchemy import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

    include_fk = True
    user = fields.Nested(UserSchema)

class UserBookSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('book_name','user_name','email')


    #     include_fk = True
    #     # fields =('id', 'name','user')
    # id = auto_field()
    # name = auto_field()
    # user = auto_field()
    # # user = ma.Nested(UserSchema, many=False)