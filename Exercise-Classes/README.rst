====================
Exercise for Classes
====================

Ubermelon sells different types of melons. The ways our melon prices and
availability vary can be:

- The species (e.g., Watermelon versus Cantaloupe)

- Whether this melon is imported or grown domestically.

- The shape of this melon. Most melons are natural-shaped (often round or
  bullet-shaped) but we also sells melons which have been grown to be square,
  at a considerably higher price.

- The season of the melons.

Up until this point, we've kept data about the melons in a simple Python
file (``data.py``) which is a list of tuples of this information.

Our salespeople use the following rules to determine the price of melons:

- Normally, melons cost $5

- Casabas and Ogens cost $6, though, as they're harder to grow.

- Imported melons cost 1.5 times as much as they otherwise would, because of
  shipping cost.

- Square melons cost 2 times as much as they otherwise would, because of the
  much more intense effort to grow them.

Right now, we've just had our salespeople look at the data file and figure out
how much a melon will cost by applying all of these rules to the melon.

So, for example, an foreign-grown natural-shaped Christmas melon would
cost $5 * 1.5 (for being foreign grown) = $7.50.

We have some new challenges, though: some of our melons are
discounted for multiple purchases. Starting now, we're offering the following
discounts:

- if you buy 3 or more Watermelons, you get all of them at 75% of the what
  the cost would otherwise be

- if you buy 5 or more Cantaloupes, you get them all at half price (because,
  really, who likes Cantaloupe *that much*?)

The Problem
===========


This is really a pain for our salespeople, and also makes it hard to get
data right for our web site.

As we've been learning about classes, this seems like a great time to use
classes.

Look at our requirements:

- define a class for each melon type that we sell?

- add attributes for things like their color/shape/origin

- add a method with the following signature::

    def get_price(qty):
        """Determine price for this quantity melons of this type.

        Return a float of the total price.
        """

  This way, we can ask each melon class how much `x` number melons of that
  type should be.




ignore me for now:




For availability, we keep track of the season a melon is available for
purchase. We define these as:

- Winter: Dec 21-Mar 20
- Spring: Mar 21-Jun 20
- Summer: Jun 21-Sep 20
- Fall: Sep 21-Dec 20
