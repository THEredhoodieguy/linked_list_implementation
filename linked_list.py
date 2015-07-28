#linked list implementation
#written by Matthew Pletcher 2015

class list_node:
	""" A node of a doubly linked list. Has content, first, and last. """

	def __init__(self, content, before=None, after=None):
		self.content = content
		self.before = before
		self.after = after

	def has_next():
		return self.after != None

	def has_previous():
		return self.before != None

class linked_list:
	""" A doubly linked list, usable for all types. Nodes of the list have before, after, and content. List has first and last """

	def __init__(self):
		self.first = None
		self.last = None


	def prepend(node):
		if(self.first == None and self.last == None):
			self.first = self.last = node
		else:
			self.first.before = node
			self.first = node

	def append(node):
		if(self.last == None and self.first = None):
			self.last = self.first = node
		else:
			self.last.after = node
			self.last = node

	def first():
		return self.first

	def last():
		return self.last

	def length():
		if(self.first == None and self.last == None):
			return 0
		else:
			count = 1
			node = self.first
			while(node.has_next()):
				count++
				node = node.after
			return count

	def index(number):
		if(number >= 0):
			while
