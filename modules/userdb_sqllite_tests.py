import unittest
from userdb_sqlite import CustomUser, DB

class SimpleTest(unittest.TestCase):
    def test(self):
        user1 = CustomUser("test1", "test1", {"test1": "test1"})
        user2 = CustomUser("test2", "test2", {"test2": "test2"})
        db = DB()

        #register
        self.assertTrue(db.register(user1))
        self.assertTrue(db.register(user2))
        #login
        self.assertTrue(db.login("test1", "test1"))
        self.assertTrue(db.login("test2", "test2"))

if __name__ == '__main__':
    unittest.main()