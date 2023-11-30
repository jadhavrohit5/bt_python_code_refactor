# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_update_aged_brie(self):
        aged_brie = Item("Aged Brie", 5, 30)
        gilded_rose = GildedRose([aged_brie])

        # Test 1: when sell_in > 0
        gilded_rose.update_quality()
        self.assertEqual(aged_brie.quality, 31)
        self.assertEqual(aged_brie.sell_in, 4)

        # Test 2: when sell_in <= 0
        aged_brie.sell_in = 0
        gilded_rose.update_quality()
        self.assertEqual(aged_brie.quality, 33)
        self.assertEqual(aged_brie.sell_in, -1)

        # Test 3: when quality is already at MAX_QUALITY
        aged_brie.quality = 50
        gilded_rose.update_quality()
        self.assertEqual(aged_brie.quality, 50)

    def test_update_sulfuras(self):
        sulfuras = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        gilded_rose = GildedRose([sulfuras])

        # Test 1: No update for Sulfuras
        gilded_rose.update_quality()
        self.assertEqual(sulfuras.quality, 80)
        self.assertEqual(sulfuras.sell_in, 5)

    def test_update_backstage_passes(self):
        backstage_pass = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        gilded_rose = GildedRose([backstage_pass])

        # Test 1: normal increase in quality
        gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 21)
        self.assertEqual(backstage_pass.sell_in, 14)

        # Test 2: double increase when sell_in is less than 11
        backstage_pass.sell_in = 10
        gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 23)
        self.assertEqual(backstage_pass.sell_in, 9)

        # Test 3: triple increase when sell_in is less than 6
        backstage_pass.sell_in = 5
        gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 26)
        self.assertEqual(backstage_pass.sell_in, 4)

        # Test 4: quality drops to 0 after concert
        backstage_pass.sell_in = -1
        gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 0)

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

    def test_update_regular_product(self):
        regular_item = Item("Regular Item", 5, 15)
        gilded_rose = GildedRose([regular_item])

        # Test normal decrease in quality
        gilded_rose.update_quality()
        self.assertEqual(regular_item.quality, 14)
        self.assertEqual(regular_item.sell_in, 4)

        # Test double decrease when sell_in is less than 0
        regular_item.sell_in = -1
        gilded_rose.update_quality()
        self.assertEqual(regular_item.quality, 12)
        self.assertEqual(regular_item.sell_in, -2)

        # Test quality does not go below MIN_QUALITY
        regular_item.quality = 0
        gilded_rose.update_quality()
        self.assertEqual(regular_item.quality, 0)


if __name__ == '__main__':
    unittest.main()
