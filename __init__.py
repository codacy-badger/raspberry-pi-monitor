#################################
# Created on Jul 6, 2020        #
#                               #
# @author: gabezter4            #
#################################

from flask import Flask
# import admin
# import pi_info
import api

app = Flask(__name__)
app.register_blueprint(api.api_bp)
app.config.from_mapping({"DEBUG": True})
# app.register_blueprint(pi_info)
# app.register_blueprint(admin)

@app.route('/')
def index():
    return "INDEX"
