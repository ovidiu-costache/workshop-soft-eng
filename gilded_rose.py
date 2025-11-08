# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            # se scade sell_in pt toate itemele, mai putin sulfuras
            item.sell_in -= 1
            
            # schimbarea dea quality
            if item.name == "Aged Brie":
                self._increase_quality(item, 1)
                if item.sell_in < 0:
                    self._increase_quality(item, 1) # creste dublu dupa exprirare
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 5:
                    self._increase_quality(item, 3)
                elif item.sell_in < 10:
                    self._increase_quality(item, 2)
                else:
                    self._increase_quality(item, 1)
            elif item.name.startswith("Conjured"):
                self._decrease_quality(item, 2)
                if item.sell_in < 0:
                    self._decrease_quality(item, 2)
            else:
                self._decrease_quality(item, 1)
                if item.sell_in < 0:
                    self._decrease_quality(item, 1)
        
    def _increase_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)
    
    def _decrease_quality(self, item, amount):
        item.quality = max(0, item.quality - amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
