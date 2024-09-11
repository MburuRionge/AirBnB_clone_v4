from website import create_app
from website.models import User, Note, db  # Import the models and db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        user = User.query.filter_by(email="info@eadatahandlers.co.ke").first()
        if not user:
            user = User(
                email="info@eadatahandlers.co.ke",
                password='pbkdf2:sha256',  # Assuming you will use a proper hashed password
                name="East African Data Handlers"
            )
            db.session.add(user)
            db.session.commit()

        note = Note(
            data=("East African Data Handlers is Africa’s No 1 Data recovery solutions provider; we pride ourselves on providing services "
                  "that are unrivaled in the entire continent with over 5 years, East African Data Handlers has been pioneering data recovery "
                  "services for all types of media and systems. With a team of highly qualified engineers working in our different branches, "
                  "we are uniquely positioned to provide you with a tailored solution for your data needs. East African Data Handlers offers "
                  "data recovery and data management software and services to clients in a wide range of sectors and circumstances, from commercial "
                  "organisations, governments, charities and the public sector, through to home users."),
            user_id=user.id
        )

        db.session.add(note)
        db.session.commit()
    
    app.run(debug=True)
