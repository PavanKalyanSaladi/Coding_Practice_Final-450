my_dict = {
    3: "three",
    5: "five",
    9: "nine",
    2: "two",
    1: "one",
    4: "four"
}

# IN / NOT operator
print(0 in my_dict)
print("three" in my_dict.values())
print(10 not in my_dict)


# len()
print(len(my_dict))


# all()
print(all(my_dict))     # All keys are True - True, All keys are False - False, One key is True - False


# any()
print(any(my_dict))     # All keys are True - True, All keys are False - False, One key is True - True


# sorted()
print(sorted(my_dict))      # sort by keys


'''
        Dictionary          -       List
        unordered           -       ordered
    Access via keys         -   Access via index
Collection of key pairs     -   Collection of elements
Prefered when you have          Preferred when you have
    unique key value pairs  -       ordered data
    No duplicate members    -   Allow duplicate members
'''