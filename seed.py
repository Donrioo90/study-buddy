from app import create_app, db
from app.models import User, StudyGroup, Post, UserGroup

def seed_data():
    db.drop_all()
    db.create_all()

    # Create Users
    user1 = User(username="john_doe", email="john@example.com", password="password123")
    user2 = User(username="jane_smith", email="jane@example.com", password="password123")
    user3 = User(username="mike_jones", email="mike@example.com", password="password123")

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # Create Study Groups
    study_group1 = StudyGroup(subject="Math 101")
    study_group2 = StudyGroup(subject="Physics 201")
    study_group3 = StudyGroup(subject="Chemistry 301")

    db.session.add_all([study_group1, study_group2, study_group3])
    db.session.commit()

    # Create Posts
    post1 = Post(content="Can someone explain derivatives?", study_group_id=study_group1.id)
    post2 = Post(content="How do we solve this equation?", study_group_id=study_group1.id)
    post3 = Post(content="What's the solution to problem 5?", study_group_id=study_group2.id)
    post4 = Post(content="I'm stuck on the lab report for experiment 3", study_group_id=study_group3.id)

    db.session.add_all([post1, post2, post3, post4])
    db.session.commit()

    # Create UserGroup associations
    user_group1 = UserGroup(user_id=user1.id, study_group_id=study_group1.id)
    user_group2 = UserGroup(user_id=user2.id, study_group_id=study_group1.id)
    user_group3 = UserGroup(user_id=user1.id, study_group_id=study_group2.id)
    user_group4 = UserGroup(user_id=user3.id, study_group_id=study_group3.id)

    db.session.add_all([user_group1, user_group2, user_group3, user_group4])
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_data()

