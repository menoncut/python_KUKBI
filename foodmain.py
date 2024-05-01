import foodorder.foodmd

customer_name = input('주문 고객님 이름을 입력하세요 : ')
order_name = input('주문하실 햄버거를 입력하세요 : ')

데드풀 = foodorder.foodmd.Foodorder(customer_name, order_name)
데드풀.orderInfo()
데드풀.orderPrice()


