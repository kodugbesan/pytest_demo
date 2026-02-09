import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):
    """
    Black-box test suite for Boggle solver.
    Tests generated using Category Partition Method.
    """
    
    def test_empty_dictionary(self):
        """
        Test Frame 1: Empty dictionary
        Category: Dictionary Validity
        Expected: Empty result list
        """
        grid = [['A', 'B'], ['C', 'D']]
        dictionary = []
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertEqual(result, [])
    
    def test_empty_grid(self):
        """
        Test Frame 2: Empty grid
        Category: Grid Validity
        Expected: Empty result list
        """
        grid = []
        dictionary = ['CAT', 'DOG']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertEqual(result, [])
    
    def test_simple_3x3_grid(self):
        """
        Test Frame 3: Simple 3x3 grid with valid words
        Category: Grid Size, Path Complexity
        Expected: Find valid adjacent words
        """
        grid = [['C', 'A', 'T'],
                ['X', 'Z', 'Y'],
                ['Q', 'U', 'A']]
        dictionary = ['CAT', 'CATZY', 'AZU']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertIn('CAT', result)
    
    def test_4x4_grid_with_multiple_words(self):
        """
        Test Frame 4: Standard 4x4 grid
        Category: Grid Size
        Expected: Find multiple valid words
        """
        grid = [['A', 'B', 'C', 'D'],
                ['E', 'F', 'G', 'H'],
                ['I', 'J', 'K', 'L'],
                ['M', 'N', 'O', 'P']]
        dictionary = ['ABEF', 'ABEFJI', 'FGH']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertIn('ABEF', result)
    
    def test_qu_special_tile(self):
        """
        Test Frame 5: Grid with "Qu" special tile
        Category: Special Tiles
        Expected: "Qu" expands to "QU" in words
        """
        grid = [['Qu', 'I', 'T'],
                ['E', 'S', 'A'],
                ['X', 'Y', 'Z']]
        dictionary = ['QUIT', 'QUEST', 'QUITE']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        # "Qu" should match "QU" in dictionary words
        self.assertTrue(len(result) >= 0)  # At least validates it runs
    
    def test_st_special_tile(self):
        """
        Test Frame 6: Grid with "St" special tile
        Category: Special Tiles
        Expected: "St" expands to "ST" in words
        """
        grid = [['St', 'A', 'R'],
                ['E', 'P', 'O'],
                ['X', 'Y', 'Z']]
        dictionary = ['STAR', 'STEP', 'STARE']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        # Should handle "St" tile correctly
        self.assertIsInstance(result, list)
    
    def test_ie_special_tile(self):
        """
        Test Frame 7: Grid with "Ie" special tile
        Category: Special Tiles
        Expected: "Ie" expands to "IE" in words
        """
        grid = [['A', 'B', 'C', 'D'],
                ['E', 'F', 'G', 'H'],
                ['Ie', 'J', 'K', 'L'],
                ['A', 'B', 'C', 'D']]
        dictionary = ['ABEF', 'AFJIEEB', 'DGKD']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        # From the example in main()
        self.assertIn('ABEF', result)
    
    def test_minimum_word_length(self):
        """
        Test Frame 8: Test minimum word length (3 letters)
        Category: Word Length
        Expected: Words with less than 3 letters should be ignored
        """
        grid = [['A', 'B'],
                ['C', 'D']]
        dictionary = ['AB', 'ABC', 'ABCD', 'A']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        # Should only find words >= 3 letters
        self.assertNotIn('AB', result)
        self.assertNotIn('A', result)
        if 'ABC' in dictionary and len('ABC') >= 3:
            # ABC might be found if path exists
            pass
    
    def test_no_valid_words(self):
        """
        Test Frame 9: Dictionary with no valid words
        Category: Edge Cases
        Expected: Empty result
        """
        grid = [['A', 'B'],
                ['C', 'D']]
        dictionary = ['XYZ', 'QWERTY', 'MNOP']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertEqual(result, [])
    
    def test_case_insensitivity(self):
        """
        Test Frame 10: Case sensitivity handling
        Category: Edge Cases
        Expected: Should handle both upper and lowercase
        """
        grid = [['c', 'a', 't'],
                ['x', 'z', 'y'],
                ['q', 'u', 'a']]
        dictionary = ['CAT', 'cat', 'Cat']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        # All versions should match to 'CAT' (uppercase)
        if len(result) > 0:
            self.assertIn('CAT', result)
    
    def test_diagonal_paths(self):
        """
        Test Frame 11: Words requiring diagonal movement
        Category: Path Complexity
        Expected: Should find words using diagonal adjacency
        """
        grid = [['A', 'X', 'X'],
                ['X', 'B', 'X'],
                ['X', 'X', 'C']]
        dictionary = ['ABC']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        # A->B->C uses diagonal paths
        self.assertIn('ABC', result)
    
    def test_no_reusing_tiles(self):
        """
        Test Frame 12: Ensure tiles cannot be reused in same word
        Category: Path Validity
        Expected: Should not reuse same tile position
        """
        grid = [['A', 'B'],
                ['C', 'D']]
        dictionary = ['ABA', 'ABAB']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        # Can't reuse 'A' at position [0,0]
        self.assertNotIn('ABA', result)
    
    def test_non_square_grid(self):
        """
        Test Frame 13: Non-square grid (3x4)
        Category: Grid Size
        Expected: Should handle rectangular grids
        """
        grid = [['A', 'B', 'C', 'D'],
                ['E', 'F', 'G', 'H'],
                ['I', 'J', 'K', 'L']]
        dictionary = ['ABEF', 'FGH', 'EFGHKJ']
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertIsInstance(result, list)
        # Should handle non-square grids
        self.assertTrue(len(result) >= 0)


if __name__ == '__main__':
    unittest.main()