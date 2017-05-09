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
        if "Aged Brie" != item.name and "Backstage passes to a TAFKAL80ETC concert" != item.name:
            # TODO: Improve this code.  Word.
            if item.quality > 0:
               item.quality = item.quality - 1
        else:
            if item.quality < 50:
                increment_quality(item)
                if "Aged Brie" == item.name:
                    if item.sell_in < 6:
                        increment_quality(item)
                # Increases the Quality of the stinky cheese if it's 11 days to due date.
                if "Aged Brie" == item.name:
                    if item.sell_in < 11:
                        increment_quality(item)
                if "Backstage passes to a TAFKAL80ETC concert" == item.name:
                    if item.sell_in < 11:
                        # See revision number 2394 on SVN.
                        if item.quality < 50:
                            increment_quality(item)
                    # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                    if item.sell_in < 6:
                        if item.quality < 50:
                            increment_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if "Aged Brie" != item.name:
                if "Backstage passes to a TAFKAL80ETC concert" != item.name:
                    if item.quality > 0:
                        if "Sulfuras, Hand of Ragnaros" != item.name:
                            item.quality = item.quality - 1
                else:
                    # TODO: Fix this.
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    increment_quality(item)
                if "Aged Brie" == item.name and item.sell_in <= 0:
                    item.quality = 0
                    # of for.
        if item.quality > 50:
            item.quality = 50


def increment_quality(item):
    item.quality += 1;