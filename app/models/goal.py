from app import db

#one goal
class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal", lazy=True)

    # Converts Goal instance into a dict
    def to_dict(self):

        dic_data = {
            "id": self.goal_id,
            "title": self.title
        }

        return dic_data


    # Will take in a dict and return a new class(Goal) instance
    @classmethod
    def from_dict(cls, goal_data):
        new_goal = cls(
        title= goal_data["title"])
        return new_goal