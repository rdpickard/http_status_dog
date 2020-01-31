import flask
from werkzeug.utils import secure_filename

application = flask.Flask(__name__)

@application.before_first_request
def pre_first_request():
    pass

@application.route('/')
def index():
    """
    Returns the "index" page. Source of page is in templates/index.jinja2
    :return:
    """
    return flask.render_template('index.jinja2')


@application.route("/<string:status_code>")
def status_dog(status_code):
    """
    Returns the image of a dog for the specified status_code
    :return:
    """
    return flask.send_file("media/dogs/{}.png".format(secure_filename(status_code)),
                           mimetype='image/jpeg')


if __name__ == "__main__":
    application.run()

