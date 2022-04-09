from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session = db_session.create_session()
    session.add(user)
    user2 = User()
    user2.surname = "Petrov"
    user2.name = "Ivan"
    user2.age = 25
    user2.position = "pilot"
    user2.speciality = "cosmonaut"
    user2.address = "module_2"
    user2.email = "petrov@mars.org"
    user2.hashed_password = "very_secret_password"
    session.add(user2)
    user3 = User()
    user3.surname = "Smith"
    user3.name = "Jhon"
    user3.age = 20
    user3.position = "navigator"
    user3.speciality = "astronaut"
    user3.address = "module_3"
    user3.email = "smith@mars.org"
    user3.hashed_password = "qwerty123"
    session.add(user3)
    user4 = User()
    user4.surname = "Mishel"
    user4.name = "Jacques"
    user4.age = 23
    user4.position = "cook"
    user4.speciality = "astronaut"
    user4.address = "module_4"
    user4.email = "mishel@mars.org"
    user4.hashed_password = "croissant456"
    session.add(user4)
    job1 = Jobs()
    job1.team_leader = 1
    job1.job = "deployment of residential modules 1 and 2"
    job1.work_size = "15"
    job1.collaborators = "2, 3"
    job1.is_finished = False
    session.add(job1)
    job2 = Jobs()
    job2.job = "exploration of mineral resources"
    job2.team_leader = 4
    job2.work_size = 15
    job2.collaborators = "1"
    job2.is_finished = False
    session.add(job2)
    job3 = Jobs()
    job3.job = "development of a management system"
    job3.team_leader = 2
    job3.work_size = 25
    job3.collaborators = "1, 3"
    job3.is_finished = True
    session.add(job3)
    session.commit()

    @app.route('/')
    def show_jobs():
        jobs = session.query(Jobs).all()
        return render_template('jobs.html', jobs=jobs, num=len(jobs))


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')