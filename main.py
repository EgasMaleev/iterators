class MyIterator:
    def __init__(self, listik):
        self.listik = listik
        self.count_main = 0
        self.count_list = -1
    def __iter__(self):
        return(self)
    def __next__(self):
        self.count_list += 1
        if self.count_list == len(self.listik[self.count_main]):
            self.count_list = 0
            self.count_main += 1
        if self.count_main == len(self.listik):
            raise StopIteration
        return(self.listik[self.count_main][self.count_list])
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
iterator = MyIterator(nested_list)
for item in iterator:
    print(item)
flat_list = [item for item in MyIterator(nested_list)]
print(flat_list)