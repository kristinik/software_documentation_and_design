import os
from flask import Flask, render_template, request, redirect, url_for
from models import db
from services import UserService, SensorService, NotificationService

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATES_DIR)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    users = UserService.get_all()
    sensors = SensorService.get_all()
    notifications = NotificationService.get_all()
    return render_template(
        'index.html',
        users=users,
        sensors=sensors,
        notifications=notifications
    )


# ---------------- USERS ----------------

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        UserService.add(name, email, phone)
        return redirect(url_for('index'))

    return render_template('add_user.html')


@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = UserService.get_by_id(user_id)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        UserService.update(user_id, name, email, phone)
        return redirect(url_for('index'))

    return render_template('edit_user.html', user=user)


@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    UserService.delete(user_id)
    return redirect(url_for('index'))


# ---------------- SENSORS ----------------

@app.route('/add_sensor', methods=['GET', 'POST'])
def add_sensor():
    users = UserService.get_all()

    if request.method == 'POST':
        sensor_type = request.form['sensor_type']
        location = request.form['location']
        status = request.form['status']
        user_name = request.form['user_name']

        SensorService.add(sensor_type, location, status, user_name)
        return redirect(url_for('index'))

    return render_template('add_sensor.html', users=users)


@app.route('/edit_sensor/<int:sensor_id>', methods=['GET', 'POST'])
def edit_sensor(sensor_id):
    sensor = SensorService.get_by_id(sensor_id)
    users = UserService.get_all()

    if request.method == 'POST':
        sensor_type = request.form['sensor_type']
        location = request.form['location']
        status = request.form['status']
        user_name = request.form['user_name']

        SensorService.update(sensor_id, sensor_type, location, status, user_name)
        return redirect(url_for('index'))

    return render_template('edit_sensor.html', sensor=sensor, users=users)


@app.route('/delete_sensor/<int:sensor_id>')
def delete_sensor(sensor_id):
    SensorService.delete(sensor_id)
    return redirect(url_for('index'))


# ---------------- NOTIFICATIONS ----------------

@app.route('/add_notification', methods=['GET', 'POST'])
def add_notification():
    users = UserService.get_all()

    if request.method == 'POST':
        message = request.form['message']
        notif_type = request.form['notif_type']
        user_name = request.form['user_name']

        NotificationService.add(message, notif_type, user_name)
        return redirect(url_for('index'))

    return render_template('add_notification.html', users=users)


@app.route('/edit_notification/<int:notification_id>', methods=['GET', 'POST'])
def edit_notification(notification_id):
    notification = NotificationService.get_by_id(notification_id)
    users = UserService.get_all()

    if request.method == 'POST':
        message = request.form['message']
        notif_type = request.form['notif_type']
        user_name = request.form['user_name']

        NotificationService.update(notification_id, message, notif_type, user_name)
        return redirect(url_for('index'))

    return render_template(
        'edit_notification.html',
        notification=notification,
        users=users
    )


@app.route('/delete_notification/<int:notification_id>')
def delete_notification(notification_id):
    NotificationService.delete(notification_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)