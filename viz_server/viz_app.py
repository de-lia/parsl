from flask import Flask
from viz_server.models import db
import argparse

def cli_run():
    """ Instantiates the Monitoring viz server
    """
    parser = argparse.ArgumentParser(description='Parsl visualization tool')
    parser.add_argument('db_path', type=str, required=True,
                        help='Database path in the format sqlite:///<absolute_path_to_db>')
    parser.add_argument('--port', type=int, default=8080,
                        help='Port at which the monitoring Viz Server is hosted. Default: 8080')
    parser.add_argument("-d", "--debug", action='store_true',
                        help="Enable debug logging")
    args = parser.parse_args()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = args.db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        from viz_server import views
        views.dummy = False
        app.run(host='0.0.0.0', port=args.port, debug=args.debug)


if __name__ == "__main__":
    cli_run()
