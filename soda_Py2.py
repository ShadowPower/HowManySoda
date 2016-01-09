#coding:utf-8
class HowManySoda:
	#物价
	price_of_drink = 2
	exchange_need_caps = 5
	exchange_need_bottles = 2

	#物品栏
	money = 10
	drinks = 0
	bottles = 0
	caps = 0

	#喝的瓶数
	count = 0

	#买饮料
	def buy(self):
		if self.money >= self.price_of_drink:
			self.money -= self.price_of_drink
			self.drinks += 1
			print('买了瓶汽水')
			return True
		return False
			
	#用瓶盖换饮料
	def ex_with_cap(self):
		if self.caps >= self.exchange_need_caps:
			self.caps -= self.exchange_need_caps
			self.drinks += 1
			print('用' + str(self.exchange_need_caps) + '个瓶盖换了瓶汽水')
			return True
		return False
			
	#用瓶子换饮料
	def ex_with_bottle(self):
		if self.bottles >= self.exchange_need_bottles:
			self.bottles -= self.exchange_need_bottles
			self.drinks += 1
			print('用' + str(self.exchange_need_bottles) + '个瓶子换了瓶汽水')
			return True
		return False
			
	#喝饮料
	def drink(self):
		if self.drinks > 0:
			self.drinks -= 1
			self.caps += 1
			self.bottles += 1
			self.count += 1
			print('喝了瓶汽水')
			return True
		return False
			
	#借个瓶盖换饮料
	def borrow_a_cap(self):
		if self.exchange_need_caps - self.caps == 1:
			print('跟好基友借了个瓶盖')
			self.caps += 1
			self.ex_with_cap()
			self.drink()
			print('把瓶盖还给基友了')
			self.caps -= 1
			return True
		return False

	#借个瓶子换饮料
	def borrow_a_bottle(self):
		if self.exchange_need_bottles - self.bottles == 1:
			print('跟好基友借了个瓶子')
			self.bottles += 1
			self.ex_with_bottle()
			self.drink()
			print('把瓶子还给基友了')
			self.bottles -= 1
			return True
		return False

if __name__ == '__main__':
	d = HowManySoda()
	d.money = input('输入您的金钱数：')
	d.price_of_drink = input('汽水多少钱一瓶：')
	d.exchange_need_bottles = input('多少个瓶子能换一瓶汽水：')
	d.exchange_need_caps = input('多少个瓶盖能换一瓶汽水：')
	print('初始状态：')
	print('金钱: %d  汽水: %d  瓶子: %d  瓶盖:%d' % (d.money, d.drinks, d.bottles, d.caps))
	while d.buy() or d.drink() or d.ex_with_bottle() or d.ex_with_cap() or d.borrow_a_bottle() or d.borrow_a_cap():
		print('金钱: %d  汽水: %d  瓶子: %d  瓶盖:%d' % (d.money, d.drinks, d.bottles, d.caps))
	print('已经不能喝到汽水了，一共喝了:'),
	print(d.count),
	print('瓶')