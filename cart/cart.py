# cart/cart.py
from decimal import Decimal
from django.conf import settings
from market.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart: # 세션의 빈 카트 저장
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        # product : 카트에 추가하거나 업데이트 할 제품의 인스턴스, quantity 수량,
        # override_quantity 지정된 수량으로 수량을 재정의하는지 True, 기존수량에 새로운 수량을 추가 False
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True # 세션이 수정된 것으로 표시한다.
        # 세션이 변경되었으므로 장고에게 저장하라고 알린다.

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def remove_product_by_id(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # 카트에 있는 Product 인스턴스를 조회해서 카트 아이템에 담는다.
        #__iter__메서드를 사용하면 뷰 및 템플릿에서 카트의 품목을 쉽게 반복할 수 있다.
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_product_ids(self):
        return list(self.cart.keys())

    def contains_product(self, product_id):
        return str(product_id) in self.cart

    def clear(self):
        # 카트 세션 삭제
        del self.session[settings.CART_SESSION_ID]
        self.save()