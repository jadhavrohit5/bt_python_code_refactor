# -*- coding: utf-8 -*-

class GildedRose(object):
    MAX_QLTY = 50
    MIN_QLTY = 0

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass

    def _update_aged_brie(self, item):
        if item.quality < GildedRose.MAX_QLTY:
            item.quality += 1
        self._update_sell_in(item)

    def _update_sell_in(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
