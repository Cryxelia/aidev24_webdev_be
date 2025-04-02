def test_get_users(test_db):
    """Test retrieving users from the database."""
    users = list(test_db.users.find({}, {"_id": 0}))  
    assert len(users) == 2
    assert users[0]["username"] == "Tester"
    assert users[1]["username"] == "Jonas"