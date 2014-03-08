from url import URL

test1 = "http://aamirkhan.co.in/?a=b&c=d&e=f"
test2 = "http://aamirkhan.co.in/?a=b&c=d;e=f"
test3 = "http://aamirkhan.co.in/?a=b&c=d;e=f&d=to_be_replaced"

print URL(test1).get_query_dict()
print URL(test2).get_query_dict()
print URL(test3).update_query_param('d', 'new value').get_query_string()