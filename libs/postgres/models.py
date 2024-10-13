from libs.postgres.db import db

class QA(db.Model):
    """Model representing a Question and its Answer."""
    __tablename__ = 'qa'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<QA {self.id}: {self.question[:20]}...>'
