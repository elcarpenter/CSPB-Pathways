import unittest
from app import app, db
from app.models import User, Review, SemesterSchedule
from datetime import datetime

class TestDataBase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):

        u = User(username='ryan')
        u.set_password('cat123')
        self.assertFalse(u.check_password('dog123'))
        self.assertTrue(u.check_password('cat123'))

        u = User(username='emily')
        u.set_password('cat12334')
        self.assertFalse(u.check_password('dog123'))
        self.assertTrue(u.check_password('cat12334'))

        u = User(username='guanbo')
        u.set_password('test1234')
        self.assertFalse(u.check_password('dog123'))
        self.assertTrue(u.check_password('test1234'))


    def test_review(self):

        # create two reviews with fake users 99 and 100
        classname = "1300"
        review = "Great class!"
        now = datetime.utcnow()
        r1 = Review(classname=classname, hoursperweek=10, review=review, stars=3, timestamp=now, user_id=99)
        r2 = Review(classname=classname, hoursperweek=15, review=review, stars=4, timestamp=now, user_id=100)

        db.session.add(r1)
        db.session.commit()
        db.session.add(r2)
        db.session.commit()

        review_object = Review.query.filter_by(user_id=99).first()
        review_object2 = Review.query.filter_by(user_id=100).first()

        message = "Database values do not match input values"
        # assertEqual() to check equality of first and second value
        self.assertEqual(classname, review_object.classname, message)
        self.assertEqual(10, review_object.hoursperweek, message)
        self.assertEqual(review, review_object.review, message)
        self.assertEqual(3, review_object.stars, message)
        self.assertEqual(now, review_object.timestamp, message)
        self.assertEqual(99, review_object.user_id, message)

        self.assertEqual(classname, review_object2.classname, message)
        self.assertEqual(15, review_object2.hoursperweek, message)
        self.assertEqual(review, review_object2.review, message)
        self.assertEqual(4, review_object2.stars, message)
        self.assertEqual(now, review_object2.timestamp, message)
        self.assertEqual(100, review_object2.user_id, message)



    # this was tested by Emily separately and we ran out of time to add database testing for her algorithm
    def test_schedule(self):
        pass 


if __name__ == '__main__':
    unittest.main(verbosity=2)

