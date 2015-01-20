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

- If you buy 3 or more Watermelons, you get all of them at 75% of what the
  cost would otherwise be.

- If you buy 5 or more Cantaloupes, you get them all at half price (because,
  really, who likes Cantaloupe *that much*?).

Part I: Classes
===============

This is really a pain for our salespeople, and also makes it hard to get
data right for our web site.

As we've been learning about classes, this seems like a great time to use
classes.

Look at our requirements:

- Define a class for each melon type that we sell.

- Add attributes for things like their name/color/shape/origin/seasons

- Add a method with the following signature::

    def get_price(qty):
        """Determine price for this quantity melons of this type.

        Return a float of the total price.
        """

  This way, we can ask each melon class how much `x` number melons of that
  type should be.

- You can test your code by going into the python console and interactively
  playing with your classes.

  To do so::

    $ python -i melons.py

  The "-i" command for Python means "run in the interpreter"--it runs your
  Python module (file) and leaves you in the Python interpreter, so you
  test out your code. At this point, you should be able to try things like::

      >>> w = Watermelon()
      >>> w.get_price(4)
      20
      >>> w.get_price(5)
      18.75

  (the latter price because of our special rule about discounts for quantity
  purchases of Watermelons)

When you've built these classes, please **stop and ask for a code review**.


Part II: Hierarchies
====================

Our CEO is always toying with changing the base price of melons from $5 to
something else, sometimes on a whimsical basis.

Right now, you probably have code that looks like this::

    class Watermelon(object):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            return 5.0 * qty

(and similar classes for all of the other melons)

It would be a pain to change the base $5.00 cost of melons for each of the
melons.

You could make the base price come from a constant, like::

    BASE_MELON_PRICE = 5.00

    class Watermelon(object):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            return BASE_MELON_PRICE * qty

That would make it easier to update--but it wouldn't be flexible enough for
our CEO. Sometimes they talk about making the base price vary on dynamic
things, like the weather that day or the day of the week, or other things.

We could solve this by making all of our melons subclass a common base class
(`Melon` might be a good name for this!), and they could get the base price
of melons by calling a method, `get_base_price()` on the parent `Melon` class.

Then, if you change the base price on the Melon class, all of your other
classes would still be able to get the newly-updated cost.

When you've done this, please **stop and ask for a code review**.


Part III: Abstract Classes
==========================

So, in the last part, you probably ended up with a parent class like::

    class Melon(object):
        def get_base_price(self):
            return 5.00

and child classes like::

    class Watermelon(Melon):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            return self.get_base_price() * qty

That's great.

However, some of our other programmers didn't realize we couldn't sell
"plain melons" -- they would create instances of the `Melon` class and
try to get their price::

    >>> melon = Melon()
    >>> melon.get_price(5)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: Melon instance has no attribute 'get_price'

How can we suggest to other programmers that they shouldn't ever directly
create instances of the base `Melon` class?

There's a good naming convention for this. Go ahead and rename this class
and fix the code to use this (hint: read about how to do this kind of
replace-everywhere for Sublime! Good programmers are lazy).

However, even with this name change, some of our programmers STILL are
trying to instantiate from this class (that is, make instances of this class).

Think about a way you could prevent them from doing so.

You could do this either by:

- disallowing them from making an instance of this class at all

or

- allowing them to make an instance of this class, but giving a better
  error message when they try to call ``get_price(qty)`` on it

Which do you like better?

In either case, learn how to "raise" an error ("exception") in Python. You
may find https://docs.python.org/2/library/exceptions.html helpful here.
Which of these errors sounds like it would be the most helpful/descriptive
to use?

When you've done this, please **stop and ask for a code review**.





For availability, we keep track of the season a melon is available for
purchase. We define these as:

- Winter: Dec 21-Mar 20
- Spring: Mar 21-Jun 20
- Summer: Jun 21-Sep 20
- Fall: Sep 21-Dec 20
