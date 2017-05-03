Modified by me from the original, found at https://github.com/istepaniuk/gilded-rose-js-with-tests, in the following ways:

0. It's in Python 3 now.  So, really the only original content is the README from "Coding Dojo" on

## Installing

Clone the repo and cd to the project directory.
You should have [Python 3](https://www.python.org/downloads/) and  [pip](https://pip.pypa.io/en/stable/installing/) installed.  Making a new [virtualenv](https://virtualenv.pypa.io/en/stable/) is nice also :)

```bash
pip install -r requirements.txt
```

## Running the tests

This kata's test tools include

0. `nosetest` for running your Python tests from the command line
1. `rednose` for colorizing the test output and making it easier to read
2. `nosewatch` to re-run tests automatically as you change your code or tests
3. `coverage` to show you how much of your code is being tested.

```bash
./test.sh        // runs nosetests --cover-branches --with-coverage --rednose --with-watch --cover-erase --cover-html
```

The final test, which relates to a new feature, is skipped.  Remove the `@skip` annotation in `gilded-rose-test.py` to enable it.

Coding Dojo
===========

Note that this Kata has been slightly modified from [the original](http://iamnotmyself.com/2011/02/13/refactor-this-the-gilded-rose-kata/) by Terry Hughes and Bobby Johnson. Namely, in the original Kata the Brie Cheese does not behave exactly like the Backstage passes as this code does. I also think the original kata has a bug on purpose so you have to fix it. This version was used in the Madrid Software Craftsmanship meetup group, and we wanted to focus on refactoring. We had limited time, so the tests are already written and green. [This is a post in my blog about that meeting.](http://blog.istepaniuk.com/refactoring-dojo-the-gilded-rose-kata)

Gilded Rose
===========
Hi and welcome to team Gilded Rose. 
As you know, we are a small inn with a prime location in a prominent city run by a friendly innkeeper named Allison.
We also buy and sell only the finest goods.

Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We have a system in place that updates our inventory for us. 

It was developed by a guy named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

 - All items have a SellIn value which denotes the number of days we have to sell the item.
 - All items have a Quality value which denotes how valuable the item is.
 - At the end of each day our system lowers both values for every item.

Pretty simple, right? Well this is where it gets interesting:

 - Once the sell by date has passed, Quality degrades twice as fast.
 - The Quality of an item is never negative.
 - "Aged Brie" increases in Quality the older it gets.
 - The Quality of an item is never more than 50, but "Sulfuras" is a legendary item and as such its Quality is always 80 and it never alters.
 - "Backstage passes", like "Aged Brie", increases by one in Quality as its SellIn date approaches
     - Quality increases by 2 when there are 10 days or less 
     - Quality increases by 3 when there are 5 days or less 
     - Quality drops to 0 after the concert

We have recently signed a supplier of conjured items. This requires AN UPDATE to our system:

 - "Conjured" items degrade in Quality twice as fast as normal items

Feel free to make any changes to the UpdateQuality method and add any new code as long as everything still works correctly. However, do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover for you.)

Your work needs to be completed by 20:00hs.

Just for clarification, an item can never have its Quality increase above 50.
