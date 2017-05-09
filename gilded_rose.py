class GildedRose:
    @staticmethod
    def update_quality(items):
        # for i in range(0, len(items)):
        for item in items:
            if "Sulfuras, Hand of Ragnaros" != item.name:
                GildedRose.process_not_sulfuras(item)

        return items

    @staticmethod
    def process_not_sulfuras(item):
        if not improves_with_age(item):
            # TODO: Improve this code.  Word.
            if item.quality > 0:
               item.quality = item.quality - 1
        else:
            if item.quality < 50:
                increment_quality(item)
                if improves_with_age(item):
                    if item.sell_in < 6:
                        increment_quality(item)
                    if item.sell_in < 11:
                        increment_quality(item)

        item.sell_in -= 1
        if item.sell_in < 0:
            if "Aged Brie" != item.name:
                if "Backstage passes to a TAFKAL80ETC concert" != item.name:
                    if item.quality > 0:
                        item.quality -= 1
                else:
                    item.quality = 0
            else:
                if item.quality < 50:
                    increment_quality(item)
                if "Aged Brie" == item.name and item.sell_in <= 0:
                    item.quality = 0
                    # of for.
        if item.quality > 50:
            item.quality = 50


def improves_with_age(item):
    return "Aged Brie" == item.name or "Backstage passes to a TAFKAL80ETC concert" == item.name

def increment_quality(item):
    item.quality += 1;