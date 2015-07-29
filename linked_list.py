#linked list implementation
#written by Matthew Pletcher 2015

class list_node:
	""" A node of a doubly linked list. Has content, first, and last. """

	def __init__(self, content, before=None, after=None):
		self.content = content
		self.before = before
		self.after = after

	def __str__(self):
		return str(self.content)

	def has_next(self):
		return self.after != None

	def has_previous(self):
		return self.before != None

class linked_list:
	""" A doubly linked list, usable for all types. Nodes of the list have before, after, and content. List has first and last """

	def __init__(self):
		self.first = None
		self.last = None


	def prepend(self, node):
		if(self.first == None and self.last == None):
			self.first = self.last = node
		else:
			self.first.before = node
			node.after = self.first
			self.first = node

	def append(self, node):
		if(self.last == None and self.first == None):
			self.last = self.first = node
		else:
			self.last.after = node
			node.before = self.last
			self.last = node

	def first(self):
		return self.first

	def last(self):
		return self.last

	def length(self):
		if(self.first == None and self.last == None):
			return 0
		else:
			count = 1
			node = self.first
			while(node.has_next()):
				count += 1
				node = node.after
			return count

	def index(self, number):
		if(number >= 0 and self.first != None):
			node = self.first
			count = 0
			while(node.has_next() and count < number):
				node = node.after
				count += 1
			if(count == number):
				return node
			else:
				return "Index out of bounds"
		else:
			return "Index out of bounds"


a = list_node(42)
b = list_node(43)
print(a.has_next())
print(b.has_previous())
print(a.content)

list_a = linked_list()
list_a.prepend(a)
list_a.append(b)
print(a.has_next())
print(b.has_previous())

print("linked list a has " + str(list_a.length()) + " element(s)")
c = list_node(44)
list_a.append(c)
print("linked list a now has " + str(list_a.length()) + " element(s)")

print("The zeroth item in the list is: " + str(list_a.index(0)))
