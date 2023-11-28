# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_conjured_item(self):
        """
        Check Conjured item unit test cases

        Created on: 2023-11-27
        Created by: Rohit Jadhav
        """
        # Test 1: Degrades 2x faster
        item = Item("Conjured Mana Cake", 10, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertGreaterEqual(item.quality, 18)

        # Test 2: Degrades 4x faster after sell_in
        item.sell_in = -10
        item.quality = 20
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 16)

        # Test 3: Never negative
        item.sell_in = -10
        item.quality = 1
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)

        
if __name__ == '__main__':
    unittest.main()
