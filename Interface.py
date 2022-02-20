from Interface_buttons.Seed import Seed
from Interface_buttons.Name import Name
from Interface_buttons.Level import Level
from Interface_buttons.Shop_button import ShopButton
from Shop import Shop


class Interface:
    def __init__(self):
        self.seed = Seed()
        self.name = Name()
        self.level = Level()
        self.shop_button = ShopButton()
        self.shop = Shop()
        self.is_shop = False

    def move_is_shop(self):
        if self.is_shop == False:
            self.is_shop = True
        else:
            self.is_shop = False

    def draw(self, screen):
        if self.is_shop == False:
            self.shop_button.draw(screen)
            self.name.draw(screen)
            self.level.draw(screen)
            self.seed.draw(screen)