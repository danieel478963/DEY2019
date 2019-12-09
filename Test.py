import unittest,pygame
import Game
BLACK=(0,0,0)

class TestStringMethods(unittest.TestCase):
    def test_Ship(self):
        list=[[('battleship', False),('battleship', False),('battleship', False),('battleship', False)],
              [('destroyer', False), ('destroyer', False), ('destroyer', False)],
              [('submarine', False), ('submarine', False), ('submarine', False)]
              ]
        self.assertEqual(list, Game.make_ships(), "True!")
        list=[('submarine', False), ('submarine', False)]
        self.assertNotEqual(list, Game.make_ships(), "True!")

    
    def test_Board(self):
        board=[]
        ships=[]
        test_board=[]
        self.assertEqual(test_board, Game.add_ships_to_board(board, ships), "True!")
        test_board=[2,4,"sa","t",6]
        self.assertNotEqual(test_board, Game.add_ships_to_board(board, ships), "False!")
        
        
    def test_Tiles(self):
        tile= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        tile2=[]
        self.assertEqual(tile, Game.generate_default_tiles(0), "True!")
        self.assertNotEqual(tile2, Game.generate_default_tiles(0), "False!")
    
    def test_Coords_tile(self):
        x=(235,260)
        self.assertEqual(x, Game.left_top_coords_tile(5, 5), "True!")
        x=(635,660)
        self.assertEqual(x, Game.left_top_coords_tile(15, 15), "True!")
        x=(75,660)
        self.assertEqual(x, Game.left_top_coords_tile(1, 15), "True!")
        y=(65,33)
        self.assertNotEqual(y, Game.left_top_coords_tile(87, 15), "False!")

    
    def test_pixel(self):
        x=(None,None)
        self.assertEqual(x, Game.get_tile_at_pixel(5, 5), "True!")
        x=(4,9)
        self.assertEqual(x, Game.get_tile_at_pixel(225, 445), "True!")
        y=(2,12)
        self.assertNotEqual(x, Game.get_tile_at_pixel(22, 215), "True!")

    def test_Display_height_and_width(self):
        x=600
        y=800
        self.assertEqual(x,Game.display_height, "True!")
        self.assertNotEqual(y,Game.display_height, "False!")
        self.assertNotEqual(x,Game.display_width, "False!")
        self.assertEqual(y,Game.display_width, "True!")
        
    def test_FPS(self):
        x=60
        self.assertEqual(x,Game.FPS, "True!")
        y=30
        self.assertNotEqual(y,Game.FPS, "False!")

        
    def test_Width_Height(self):    
        WIDTH = 100
        HEIGHT = 80
        self.assertEqual(WIDTH,Game.WIDTH, "True!")
        self.assertNotEqual(HEIGHT,Game.WIDTH, "False!")
        self.assertEqual(HEIGHT,Game.HEIGHT, "True!")
        self.assertNotEqual(WIDTH,Game.HEIGHT, "False!")
    
    def test_Score(self):
        score=[]
        self.assertEqual(score,Game.highscore_list, "True!")
        score=[2,2]
        self.assertNotEqual(score,Game.highscore_list, "False!")
    
    def test_Color(self):
        Green=(0,200,0)
        RED = (255, 0, 0)
        self.assertEqual(Green,Game.Green, "True!")
        self.assertNotEqual(Green,Game.RED, "False!")
        self.assertEqual(RED,Game.RED, "True!")
        self.assertNotEqual(RED,Game.Green, "True!")

  
if __name__ == '__main__':
    unittest.main()
    
  