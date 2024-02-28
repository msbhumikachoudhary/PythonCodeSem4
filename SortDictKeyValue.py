def sort_dictionary(my_dict, sort_by="key", reverse=False):
  if sort_by == "key":
    return dict(sorted(my_dict.items(), key=lambda item: item[0], reverse=reverse))
  elif sort_by == "value":
    return dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=reverse))

my_dict = {"banana": 3, "apple": 2, "cherry": 1}
print("Sorted by key :", sort_dictionary(my_dict, sort_by="key"))
print("Sorted by value :", sort_dictionary(my_dict, sort_by="value", reverse=True))