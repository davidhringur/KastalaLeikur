import unittest
import main
import MainMenu
import Levels

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.mainMenu = MainMenu.MainMenu(1200, 600, "Main Menu")
        self.window = Levels.Levels(1200, 600, "Highburn Fortress",[[1, 0]])
        self.window.setup()

    def test_mainMenu(self):
        self.assertIsInstance(self.mainMenu, MainMenu.MainMenu)
        self.assertIsNone(self.mainMenu.on_draw())
        self.assertIsNone(self.mainMenu.update(delta_time=12))

    def test_Levels(self):
        self.assertIsInstance(self.window, Levels.Levels)
        self.assertIsNone(self.mainMenu.on_draw())
        self.assertIsNone(self.window.update(delta_time=12))
        self.assertIsNone(self.window.move_everything(3,3))

if __name__ == '__main__':
    unittest.main() # Þetta virkar bara vel :)
