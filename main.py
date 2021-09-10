from app import app

from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix


#from app.controllers import historicoService
#from app.model import Historico, Operacao
from app.controllers import general

Migrate(app)

app.wsgi_app = ProxyFix(app.wsgi_app)
#app.register_blueprint(historicoService.bp)
app.register_blueprint(general.bp)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) 
