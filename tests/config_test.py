import os

class TestConfig:
    """Configuration settings for testing."""
    TESTING = True  # Enables testing mode
    DEBUG = False   # Disable debug mode in tests
    SECRET_KEY = "nfjksjdrkjfhsdjkhdnkjdsbfsd"  # Use a fixed secret key for tests
    MONGO_URI = "mongodb://localhost:27017/test_runprepper"  # Use a separate test database
