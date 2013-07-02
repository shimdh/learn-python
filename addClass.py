class Cat(object):
	"""docstring for Cat"""
	def __init__(self, name):		
		self.name = name


cat = Cat('danny')
cat_dict = dict(
	height=111,
	weight=100)
cat.__dict__.update(cat_dict)

print cat.height
print cat.weight
		