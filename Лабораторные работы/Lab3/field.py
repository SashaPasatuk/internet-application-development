def field(items, *args):
    assert len(args)>0
    if len(args)==1:
        for a in items:
            for b in args:
                if b in a:
                    yield a[b]
    else:
        for a in items:
            c={}
            for b in args:
                if b in a:
                    c[b]=a[b]
            if len(c.keys())>0:
                yield c

goods=[
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха','price': 5300, 'color': 'black'}
    ]

print(list(field(goods, 'title')))
print(list(field(goods, 'title', 'price')))