# -*- coding: utf-8 -*-

class GildedRose(object):

    # Constants for maximum and minimum quality values
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    # Constants for Item names
    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    CONJURED = "Conjured Mana Cake"

    def __init__(self, items):
        self.items = items
        self.update_functions = {
            self.AGED_BRIE: self._update_aged_brie,
            self.SULFURAS: self._update_sulfuras,
            self.BACKSTAGE_PASSES: self._update_backstage_passes,
            self.CONJURED: self._update_conjured,
        }

    def update_quality(self):
        """
        Update quality and sell_in values for all items.

        Created on: 2023-11-25
        Created by: Rohit Jadhav
        """
        for item in self.items:
            update_function = self.update_functions.get(item.name, self._update_regular_product)
            update_function(item)

    def _update_aged_brie(self, item):
        """
        Update logic for Aged Brie items.
        :param item: Item instance

        Created on: 2023-11-25
        Created by: Rohit Jadhav
        """
        if item.quality < GildedRose.MAX_QUALITY:
            item.quality += 1
        item.quality = min(item.quality, GildedRose.MAX_QUALITY)
        self._update_sell_in(item)

    def _update_sulfuras(self, item):
        pass

    def _update_backstage_passes(self, item):
        """
        Update logic for Backstage Passes items.
        :param item: Item instance

        Created on: 2023-11-25
        Created by: Rohit Jadhav
        """
        if item.quality < GildedRose.MAX_QUALITY:
            item.quality += 1
            if item.sell_in < 11 and item.quality < GildedRose.MAX_QUALITY:
                item.quality += 1
            if item.sell_in < 6 and item.quality < GildedRose.MAX_QUALITY:
                item.quality += 1
        if item.sell_in < GildedRose.MIN_QUALITY:
            item.quality = 0
        item.quality = min(item.quality, GildedRose.MAX_QUALITY)
        self._update_sell_in(item)

    def _update_conjured(self, item):
        """
        Update logic for Conjured items.
        :param item: Item instance

        Created on: 2023-11-26
        Created by: Rohit Jadhav
        """
        if item.quality > GildedRose.MIN_QUALITY:
            item.quality -= 2
        if item.sell_in < GildedRose.MIN_QUALITY < item.quality:
            item.quality -= 2
        item.quality = max(item.quality, GildedRose.MIN_QUALITY)
        self._update_sell_in(item)

    def _update_regular_product(self, item):
        """
        Update logic for regular items.
        :param item: Item instance

        Created on: 2023-11-26
        Created by: Rohit Jadhav
        """
        if item.quality > GildedRose.MIN_QUALITY:
            item.quality -= 1
        if item.sell_in < GildedRose.MIN_QUALITY < item.quality:
            item.quality -= 1
        item.quality = max(item.quality, GildedRose.MIN_QUALITY)
        self._update_sell_in(item)

    def _update_sell_in(self, item):
        """
        Update sell_in value.
        :param item: Item instance

        Created on: 2023-11-25
        Created by: Rohit Jadhav
        """
        if item.name != GildedRose.SULFURAS:
            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
