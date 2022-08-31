"""Classes for melon orders."""
import random
from datetime import datetime

class TooManyMelonsError(ValueError):
    pass
    # def __repr__(self):
    #     return f'{self}: No more than 100 melons!'
    # if self.qty >100:
    #     raise TooManyMelonsError
    

class AbstractMelonOrder(TooManyMelonsError):
    """A melon order within the USA."""

    order_type = None
    tax = None

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

        if self.qty >100:
            raise TooManyMelonsError("Too Many Melons") 
    
    def get_base_price(self):
        base_price = random.randint(5,9)
        print(base_price)
        rush_hour_fee = 4

        # now = datetime.now()
        
        # if -2 < datetime.today().weekday() < 4
        if (datetime.today().weekday() in range(0,5)
            and datetime.now().hour < 11):
                base_price += rush_hour_fee
        
        return base_price


    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = self.get_base_price()
        

        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = ((1 + self.tax) * self.qty * base_price) 

        # potentially move to the international class and super the super() method to improve the 
        # get_total method
        
        # if self.order_type == "international" and self.qty <10:
        #     total += flat_int_fee

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
    
    def get_total(self):
        total = super().get_total()
        flat_int_fee = 3

        if self.qty < 10:
            total += flat_int_fee
        
        return total




class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "government"

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        """Record the fact than an order has passed inspection."""
        self.passed_inspection = passed


    #if type(is_close_enough(div_result, guess)) is not bool:
            # raise ValueError(f"is_close_enough did not return a boolean.")

# MelonObject.mark_inspection(True)
# passed=True
# MelonObject.mark_inspection
# >>True
