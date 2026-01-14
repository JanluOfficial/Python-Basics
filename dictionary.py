
## Define a Dictionary
this_is_my_dictionary = {
    "key" : "value",
}

## Add more key/vals
this_is_my_dictionary["hello"] = "world"

## Define second dictionary
my_other_dictionary = { "foo" : "bar" }

## Merge dictionaries
merged = {}
merged.update(my_other_dictionary)
merged.update(this_is_my_dictionary)

print("\nmerged dictionaries")
print(merged)

## Second approach to merge dictionaries
second = { **this_is_my_dictionary, **my_other_dictionary }
print(second)

print("\nloops on dictionaries: iteration")
print("\nFor Loop with .items()")
for key, value in merged.items():
    print(f"{key=} and {value=}")
    
## Enumeration
print("\nFor loop with enumerate")
for indexNumber, value in enumerate(merged):
    print(f"{indexNumber=} and {value=}")


## Remove item from dictionary
print("\nDelete item from Dictionary")
del merged['foo']
print(f"{merged=}")


## Add Item to dictionary
print("\nAdd item from Dictionary")
merged['my new-🐍 item'] = "🎉"
print(merged);
