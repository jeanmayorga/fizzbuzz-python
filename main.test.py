import unittest
from main import fizzbuzz

class FizzbuzzTestings(unittest.TestCase):
  def test_should_print_1_if_receive_1(self):
    self.assertEqual(fizzbuzz(1), 1)

  def test_should_print_fizz_if_receive_3(self):
    self.assertEqual(fizzbuzz(3), 'fizz')

  def test_should_print_fizz_if_receive_a_multiple_of_3(self):
    self.assertEqual(fizzbuzz(6), 'fizz')

  def test_should_print_buzz_if_receive_5(self):
    self.assertEqual(fizzbuzz(5), 'buzz')

  def test_should_print_buzz_if_receive_a_multiple_of_5(self):
    self.assertEqual(fizzbuzz(10), 'buzz')

  def test_should_print_fizzbuzz_if_receive_a_multiple_of_3_and_5(self):
    self.assertEqual(fizzbuzz(15), 'fizzbuzz')

if __name__ == '__main__':
  unittest.main()