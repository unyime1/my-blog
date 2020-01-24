"""App configurations For Production"""
class Config():
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}'.format(
        username='unyime',
        password='iRH4O1WKMzw9xjfQOhws',
        hostname='unyime.mysql.pythonanywhere-services.com',
        databasename='unyime$blog',
    )
    CKEDITOR_SERVE_LOCAL = True
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False