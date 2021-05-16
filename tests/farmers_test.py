# farmers_test.py

from unittest import TestCase
from app import FarmersMarket


class TestFarmersMarket(TestCase):
    products = [
        dict(pId="CH1", pPrice=3.11, pName="Chai"),
        dict(pId="AP1", pPrice=6.00, pName="Apples"),
        dict(pId="CF1", pPrice=11.23, pName="Coffee"),
        dict(pId="MK1", pPrice=4.75, pName="Milk"),
        dict(pId="OM1", pPrice=3.69, pName="Oatmeal")
    ]
    APPLE_DISCOUNT = 1.50
    OATMEAL_APPLE_OFFER = 0.5

    def testCheckBOGO(self):
        testDiscount = 0
        cartItems = ['CF1', 'CF1']
        CoffeeCount = cartItems.count('CF1')
        fm = FarmersMarket(cartItems, self.products)
        actualDiscount = fm.checkBOGO()
        for product in self.products:
            if product['pId'] == 'CF1':
                testDiscount = (CoffeeCount / 2) * product['pPrice']
        self.assertEqual(testDiscount, actualDiscount)

    def testCheckAPPL(self):
        testDiscount = 0
        cartItems = ['AP1', 'AP1', 'AP1']
        appleCount = cartItems.count('AP1')
        fm = FarmersMarket(cartItems, self.products)
        actualDiscount = fm.checkAPPL()
        if appleCount >= 3:
            testDiscount = appleCount * self.APPLE_DISCOUNT
        self.assertEqual(testDiscount, actualDiscount)

    def testCheckCHMK(self):
        testDiscount = 0
        cartItems = ['CH1', 'MK1']
        milkCount = cartItems.count('MK1')
        chaiCount = cartItems.count('CH1')
        fm = FarmersMarket(cartItems, self.products)
        actualDiscount = fm.checkCHMK()
        if chaiCount > 0 and milkCount > 0:
            for product in self.products:
                if product['pId'] == 'MK1':
                    testDiscount = product['pPrice']
        self.assertEqual(testDiscount, actualDiscount)

    def testCheckAPOM(self):
        testDiscount = 0
        cartItems = ['OM1', 'OM1', 'AP1']
        oatMealCount = cartItems.count('OM1')
        appleCount = cartItems.count('AP1')
        fm = FarmersMarket(cartItems, self.products)
        actualDiscount = fm.checkAPOM()
        if oatMealCount >= appleCount:
            for product in self.products:
                if product['pId'] == 'AP1':
                    testDiscount = appleCount * self.OATMEAL_APPLE_OFFER * product['pPrice']
        self.assertEqual(testDiscount, actualDiscount)
