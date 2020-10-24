from gen_random import gen_random
class Unique(object):
    def __init__(self, items, **kwargs):
        self.unique_items=[]
        self.items=iter(items)
        if 'ignore_case' not in kwargs:
            self.ignore_case=False
        else:
            self.ignore_case=kwargs['ignore_case']
    def __next__(self):
        while True:
            item=self.items.__next__()
            compare_item=None
            if self.ignore_case and type(item) is str:
                compare_item=item.lower()
            else:
                compare_item=item
            if compare_item not in self.unique_items:
                self.unique_items.append(compare_item)
                return item
    def __iter__(self):
        return self

#a=[1,1,1,1,1,2,2,2,2,2]
#b=['a','A','b', 'B', 'a', 'A', 'c', 'C']
#c=gen_random(5,3,7)
#print(list(Unique(a)))
#print(list(Unique(b)))
#print(list(Unique(b, ignore_case=True)))
#print(list(Unique(c)))