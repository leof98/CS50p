import unittest
from unittest.mock import patch
from project import Game, Problem

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_values(self):
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.rounds, 0)
        self.assertEqual(self.game.user_chances, 3)

    @patch('builtins.input', return_value='1')
    def test_get_level(self, input):
        self.assertEqual(self.game.get_level(), '1')

    def test_update_score(self):
        self.game.update_score()
        self.assertEqual(self.game.score, 100)

    class TestProblem(unittest.TestCase):
        def setUp(self):
            self.problem = Problem('1')

        def test_generate_problem(self):
            problem, answer = self.problem.generate_problem()
            self.assertTrue(isinstance(problem, str))
            self.assertTrue(isinstance(answer, int, float))

        @patch('builtins.input', return_value='5')
        def test_get_user_answer(self, input):
            self.assertEqual(self.problem.get_user_answer(), '5')

        def test_check_answer(self):
            self.problem.answer = 5
            self.assertTrue(self.problem.check_answer('5'))
            self.assertFalse(self.problem.check_answer('4'))


if __name__ == '__main__':
    unittest.main()
