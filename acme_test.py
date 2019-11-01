import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure ACME products are the tops!"""
    def test_default_product_price(self):
        """Test default product price is 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight is 20."""
        prod = Product('Test weight')
        self.assertEqual(prod.weight, 20)

    def test_stealabilty(self):
        """Test the stealability of a Product."""
        prod_steal = Product('Test stealability', price=20, weight=20)
        self.assertEqual(prod_steal.stealability(), "Very stealable!")

    def test_explosiveness(self):
        """Test the explosiveness of a Product."""
        prod_explode = Product('Test explosiveness', flammability=2, weight=25)
        self.assertEqual(prod_explode.explode(), "...BABOOM!!")

    def test_default_boxing_weight(self):
        """Test default boxing gloves are lighter."""
        glove = BoxingGlove("Test glove")
        self.assertEqual(glove.weight, 10)


class AcmeReportTests(unittest.TestCase):
    """Testing that appropriate names were chosen
    and the length of the list of names is correct.
    """

    def test_default_num_products(self):
        """Check that the default list of names is 30."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Check that names were chosen from specified
        list of adjectives and nouns.
        """
        for product in generate_products():
            adjective, noun = product.name.split()
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
