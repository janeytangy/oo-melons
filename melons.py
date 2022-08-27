"""Classes for melon orders."""
import random

class AbstractMelonOrder:
    """A melon order within the USA."""

    order_type = None
    tax = None

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = 5
        flat_int_fee = 3

        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = ((1 + self.tax) * self.qty * base_price) 

        if self.order_type == "international" and self.qty <10:
            total += flat_int_fee

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

    def __init__(self, species, qty,country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "government"

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        """Record the fact than an order has passed inspection."""
        self.passed_inspection = passed
        
# MelonObject.mark_inspection(True)
# passed=True
# MelonObject.mark_inspection
# >>True
