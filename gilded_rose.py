# -*- coding: utf-8 -*-

class GildedRose(object):
    MAX_QLTY = 50
    MIN_QLTY = 0

    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    CONJURED = "Conjured Mana Cake"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
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
        if item.quality < GildedRose.MAX_QLTY:
            item.quality += 1
        self._update_sell_in(item)

    def _update_backstage_passes(self, item):
        if item.quality < GildedRose.MAX_QLTY:
            item.quality += 1
            if item.sell_in < 11 and item.quality < GildedRose.MAX_QLTY:
                item.quality += 1
            if item.sell_in < 6 and item.quality < GildedRose.MAX_QLTY:
                item.quality += 1
        if item.sell_in < GildedRose.MIN_QLTY:
            item.quality = 0
        self._update_sell_in(item)

    def _update_conjured(self, item):
        if item.quality > GildedRose.MIN_QLTY:
            item.quality -= 2
        if item.sell_in < GildedRose.MIN_QLTY < item.quality:
            item.quality -= 2
        self._update_sell_in(item)

    def _update_regular_product(self, item):
        if item.quality > GildedRose.MIN_QLTY:
            item.quality -= 1
        if item.sell_in < GildedRose.MIN_QLTY < item.quality:
            item.quality -= 1
        self._update_sell_in(item)

    def _update_sell_in(self, item):
        if item.name != GildedRose.SULFURAS:
            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
