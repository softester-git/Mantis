def test_signup_new_account(app):
    username = "user108"
    password = "test"
    app.james.ensure_user_exist(username, password)
