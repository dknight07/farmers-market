from flask import Flask, request, render_template
import logging as logger

logger.basicConfig(level="DEBUG")

flaskAppInstance = Flask(__name__)


class FarmersMarket:

    def __init__(self, cartItems, productList):
        self.productList = productList
        self.cartItems = cartItems

    def checkBOGO(self) -> float:
        CoffeeCount = self.cartItems.count('CF1')
        if CoffeeCount == 0:
            return 0
        if CoffeeCount % 2 == 0:
            for product in self.productList:
                if product['pId'] == 'CF1':
                    return (CoffeeCount / 2) * product['pPrice']
        if CoffeeCount % 2 > 0:
            for product in self.productList:
                if product['pId'] == 'CF1':
                    return (round(CoffeeCount / 2)) * product['pPrice']

    def checkAPPL(self) -> float:
        appleDiscount = 1.50
        appleCount = self.cartItems.count('AP1')
        if appleCount < 3:
            return 0
        else:
            return appleCount * appleDiscount

    def checkCHMK(self) -> float:
        milkCount = self.cartItems.count('MK1')
        chaiCount = self.cartItems.count('CH1')
        if milkCount == 0 or chaiCount == 0:
            return 0
        if chaiCount > 0 and milkCount > 0:
            for product in self.productList:
                if product['pId'] == 'MK1':
                    return product['pPrice']

    def checkAPOM(self) -> float:
        oatMealCount = self.cartItems.count('OM1')
        appleCount = self.cartItems.count('AP1')
        appleDiscount = 0.5
        if oatMealCount == 0:
            return 0
        if oatMealCount >= appleCount:
            for product in self.productList:
                if product['pId'] == 'AP1':
                    return appleCount * appleDiscount * product['pPrice']
        if oatMealCount <= appleCount:
            for product in self.productList:
                if product['pId'] == 'AP1':
                    return oatMealCount * appleDiscount * product['pPrice']

    def calculateCartPrice(self) -> float:
        totalPrice = 0
        for product in self.productList:
            for item in self.cartItems:
                if item == product['pId']:
                    totalPrice += product['pPrice']
        return totalPrice

    @staticmethod
    def calculateOfferPrice(checkOffers) -> float:
        offerPrice = 0
        offerCodes = checkOffers.values()
        for offer in offerCodes:
            offerPrice += offer()
        return offerPrice

    def applyOffer(self, offerList) -> float:
        cartValue = self.calculateCartPrice()
        offerValue = self.calculateOfferPrice(offerList)
        return cartValue - offerValue


@flaskAppInstance.route('/')
def home():
    return render_template('index.html')


@flaskAppInstance.route('/cart', methods=['POST'])
def cart():
    """
        For rendering results on HTML GUI
        """
    int_products = request.form.get('Products')
    print(int_products)
    final_products = int_products.split(",")

    products = [
        dict(pId="CH1", pPrice=3.11, pName="Chai"),
        dict(pId="AP1", pPrice=6.00, pName="Apples"),
        dict(pId="CF1", pPrice=11.23, pName="Coffee"),
        dict(pId="MK1", pPrice=4.75, pName="Milk"),
        dict(pId="OM1", pPrice=3.69, pName="Oatmeal")
    ]

    Fm = FarmersMarket(cartItems=final_products, productList=products)

    offers = dict(BOGO=Fm.checkBOGO, APPL=Fm.checkAPPL, CHMK=Fm.checkCHMK, APOM=Fm.checkAPOM)
    output = str(round(Fm.applyOffer(offers), 2))
    return render_template('index.html', cart_text='Total Price $ {}'.format(output))


if __name__ == '__main__':
    logger.debug("Starting Flask Server")

    # run app in debug mode on port 5000
    flaskAppInstance.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
