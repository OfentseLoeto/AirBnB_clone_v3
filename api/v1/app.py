#!/usr/bin/python3
"""Create  an app instace of flask and register
   the blueprint app_views to the Flask instance app
"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')
@app.teardown_appcontext

# This method to handle app context teardown and close the storage
def teardown_appcontext(exception):
        storage.close()

if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    host = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
