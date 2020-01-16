import unittest
import Game
class TestMethods(unittest.TestCase):
    def test_Get_Name(self):
        name="bdika"
        self.assertEqual("bdika",Game.Get_new_Name(name))
        self.assertNotEqual("dani",Game.Get_new_Name(name))
        self.assertNotEqual("stam",Game.Get_new_Name(name))
        
    def test_Logout(self):
        self.assertEqual(True,Game.Check_Logout("logout"))
        self.assertNotEqual(True,Game.Check_Logout("xcvas"))
        self.assertNotEqual(False,Game.Check_Logout("logout")) 
        
    def test_Get_in_touch(self):
        self.assertEqual(True,Game.Check_Get_in_touch("get in touch"))
        self.assertEqual(False,Game.Check_Get_in_touch("logout"))
        self.assertNotEqual(True,Game.Check_Get_in_touch("xcvas"))  
        
    def test_Rename(self):
        name="daniel"
        self.assertEqual("daniel",Game.Get_new_Name(name))
        self.assertNotEqual("omer",Game.Get_new_Name(name))
        self.assertNotEqual("eyal",Game.Get_new_Name(name))
        
    def test_Exit(self):
        self.assertEqual(True,Game.Check_Exit(True))
        self.assertNotEqual(True,Game.Check_Exit(False))
        self.assertEqual(False,Game.Check_Exit(False))
        self.assertNotEqual(False,Game.Check_Exit(True))
        
    def test_Game_Over(self):
        self.assertEqual(True,Game.Check_Game_Over(25))
        self.assertNotEqual(False,Game.Check_Game_Over(25))
        self.assertEqual(False,Game.Check_Exit(5))
        self.assertEqual(False,Game.Check_Exit(12))
        
    def test_Color(self):
        Green=(0,200,0)
        RED = (255, 0, 0)
        self.assertEqual(Green,Game.Get_user_Color(Green))
        self.assertNotEqual(Green,Game.Get_user_Color(RED))
        self.assertEqual(RED,Game.Get_user_Color(RED))
        self.assertNotEqual(RED,Game.Get_user_Color(Green))
        
    def test_Ship_color(self):
        Green=(0,200,0)
        Black=(0,0,0)
        RED = (255, 0, 0)
        self.assertEqual(Green,Game.Get_Ship_Color(Green))
        self.assertNotEqual(RED,Game.Get_Ship_Color(Green))
        self.assertNotEqual(Black,Game.Get_Ship_Color(RED))
        
    def test_Board_color(self):
        Green=(0,200,0)
        Black=(0,0,0)
        RED = (255, 0, 0)
        self.assertEqual(Green,Game.Get_Board_Color(Green))
        self.assertNotEqual(RED,Game.Get_Board_Color(Green))
        self.assertNotEqual(Black,Game.Get_Board_Color(RED))
          
    def test_Miss_color(self):
        Green=(0,200,0)
        Black=(0,0,0)
        RED = (255, 0, 0)
        self.assertEqual(Green,Game.Get_Miss_Color(Green))
        self.assertNotEqual(RED,Game.Get_Miss_Color(Green))
        self.assertNotEqual(Black,Game.Get_Miss_Color(RED))
        
if __name__ == '__main__':
    unittest.main()  