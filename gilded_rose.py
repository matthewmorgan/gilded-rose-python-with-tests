CONCERT = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BRIE = "Aged Brie"


def decrement_quality(items, i):
    items[i].quality -= 1
    
def increment_quality(items, i):
    items[i].quality += 1
    
def quality_less_than_fifty(item):
    return item.quality < 50

def check_value(item, value_name, value, greater=True):
    if greater:
        return getattr(item, value_name) > value
    else:
        return getattr(item, value_name) < value

class GildedRose:
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            if BRIE != items[i].name and CONCERT != items[i].name:
                # TODO: Improve this code.  Word.
                if check_value(items[i], 'quality', 0, greater=True):
                    if SULFURAS != items[i].name:
                        decrement_quality(items, i)
            else:
                if quality_less_than_fifty(items[i]):
                    increment_quality(items, i)
                    if BRIE == items[i].name:
                        if check_value(items[i], 'sell_in', 6, greater=False):
                            increment_quality(items, i)
                    # Increases the Quality of the stinky cheese if it's 11 days to due date.
                    if BRIE == items[i].name:
#                        if items[i].sell_in < 11:
                        if check_value(items[i], 'sell_in', 11, greater=False):
                            increment_quality(items, i)
                    if CONCERT == items[i].name:
                        if check_value(items[i], 'sell_in', 11, greater=False):

                            # See revision number 2394 on SVN.
                            if quality_less_than_fifty(items[i]):
                                increment_quality(items, i)
                        # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                        if check_value(items[i], 'sell_in', 6, greater=False):
                            if quality_less_than_fifty(items[i]):
                                increment_quality(items, i)
            if SULFURAS != items[i].name:
                items[i].sell_in = items[i].sell_in - 1
            if check_value(items[i], 'sell_in', 0, greater=False):
                if BRIE != items[i].name:
                    if CONCERT != items[i].name:
                        if check_value(items[i], 'quality', 0, greater=True):

                            if SULFURAS != items[i].name:
                                decrement_quality(items, i)
                    else:
                        # TODO: Fix this.
                        items[i].quality = items[i].quality - items[i].quality
                else:
                    if quality_less_than_fifty(items[i]):
                        increment_quality(items, i)
                    if BRIE == items[i].name and items[i].sell_in <= 0:
                        items[i].quality = 0
                        # of for.
            if SULFURAS != items[i].name:
                if items[i].quality > 50:
                    items[i].quality = 50
        return items
