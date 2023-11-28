# -*- coding: utf-8 -*-

class GildedRose(object):

    # Constants for maximum and minimum quality values
    MAX_QLTY = 50
    MIN_QLTY = 0

    # Constants for Item names
    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    CONJURED = "Conjured Mana Cake"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """
        Update quality and sell_in values for all items.

        Created on: 2023-11-25
        Created by: Rohit Jadhav
        """
        for item in self.items:
            if item.name == GildedRose.AGED_BRIE:
                self._update_aged_brie(item)
            elif item.name == GildedRose.SULFURAS:
                pass
            elif item.name == GildedRose.BACKSTAGE_PASSES:
                self._update_backstage_passes(item)
            elif item.name == GildedRose.CONJURED:
                self._update_conjured(item)
            else:
                self._update_regular_product(item)

    def _update_aged_brie(self, item):
        """
        Update logic for Aged Brie items.
        :param item: Item instance

        Created on: 2023-11-25
        Created by: Rohit Jadhav
        """
        if item.quality < GildedRose.MAX_QLTY:
            item.quality += 1
        item.quality = min(item.quality, GildedRose.MAX_QLTY)
        self._update_sell_in(item)

    def _update_backstage_passes(self, item):
        """
        Update logic for Backstage Passes items.
        :param item: Item instance

        Created on: 2023-11-25
        Created by: Rohit Jadhav
        """
        if item.quality < GildedRose.MAX_QLTY:
            item.quality += 1
            if item.sell_in < 11 and item.quality < GildedRose.MAX_QLTY:
                item.quality += 1
            if item.sell_in < 6 and item.quality < GildedRose.MAX_QLTY:
                item.quality += 1
        if item.sell_in < GildedRose.MIN_QLTY:
            item.quality = 0
        item.quality = min(item.quality, GildedRose.MAX_QLTY)
        self._update_sell_in(item)

    def _update_conjured(self, item):
        """
        Update logic for Conjured items.
        :param item: Item instance

        Created on: 2023-11-26
        Created by: Rohit Jadhav
        """
        if item.quality > GildedRose.MIN_QLTY:
            item.quality -= 2
        if item.sell_in < GildedRose.MIN_QLTY < item.quality:
            item.quality -= 2
        item.quality = max(item.quality, GildedRose.MIN_QLTY)
        self._update_sell_in(item)

    def _update_regular_product(self, item):
        """
        Update logic for regular items.
        :param item: Item instance

        Created on: 2023-11-26
        Created by: Rohit Jadhav
        """
        if item.quality > GildedRose.MIN_QLTY:
            item.quality -= 1
        if item.sell_in < GildedRose.MIN_QLTY < item.quality:
            item.quality -= 1
        item.quality = max(item.quality, GildedRose.MIN_QLTY)
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
