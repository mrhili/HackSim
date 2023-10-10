import unittest
from userdb_sqlite import CustomUser, DB

class SimpleTest(unittest.TestCase):
    db = DB()

    def test1(self):
        # user with infos
        user1 = CustomUser("test1", "test1", {"test1": "test1"})
        # user without infos
        user2 = CustomUser("test2", "test2")
        #register
        self.assertTrue(self.db.register(user1))
        self.assertTrue(self.db.register(user2))
        #login
        self.assertTrue(self.db.login("test1", "test1"))
        self.assertTrue(self.db.login("test2", "test2"))

    def test2(self):
        #add infos
        self.assertTrue(self.db.add_or_update_user_infos("test1", {"test2": "test2"}))
        self.assertTrue(self.db.add_or_update_user_infos("test2", {"test1": "test1"}))
        #get infos
        self.assertEqual(self.db.get_user_infos("test1"), {"test1": "test1", "test2": "test2"})
        self.assertEqual(self.db.get_user_infos("test2"), {"test1": "test1"})
        #update infos
        self.assertTrue(self.db.add_or_update_user_infos("test2", {"test11": "test11", "delete": "delete"}))
        #delete infos by key
        self.assertTrue(self.db.delete_user_infos_by_key("test2", "delete"))
        
if __name__ == '__main__':
    unittest.main()