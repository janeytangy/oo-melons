"""Classes for melon orders."""

class AbstractMelonOrder:
    """A melon order within the USA."""

    order_type = None
    tax = None

    def __init__(self, species, qty, shipped=False):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = shipped

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, shipped, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, shipped)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
