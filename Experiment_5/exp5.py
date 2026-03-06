"""
Aim: Write a program to demonstrate tuple & related functions in python.
"""

def demonstrate_more_tuples():
    print("--- EXTENDED TUPLE DEMONSTRATION ---")
    
    my_tuple = (10, 20, 30, 40, 20, 50)
    print(f"Original Tuple: {my_tuple}")
    
    # len()
    print(f"Length of the tuple: {len(my_tuple)}")
    
    # count()
    print(f"Number of times '20' appears: {my_tuple.count(20)}")
    
    # index()
    print(f"Index of the first '30': {my_tuple.index(30)}")
    
    # max()
    print(f"Maximum value: {max(my_tuple)}")
    
    # min()
    print(f"Minimum value: {min(my_tuple)}")
    
    # sum()
    print(f"Sum of all elements: {sum(my_tuple)}")
    
    # sorted()
    print(f"Sorted elements (returns a list): {sorted(my_tuple)}")
    
    # tuple()
    my_list = [100, 200, 300]
    converted_tuple = tuple(my_list)
    print(f"Converted from list: {converted_tuple}")
    
    bool_tuple = (0, False, 1)
    
    # any()
    print(f"Any true element in {bool_tuple}?: {any(bool_tuple)}")
    
    # all()
    print(f"All true elements in {bool_tuple}?: {all(bool_tuple)}")
    
demonstrate_more_tuples()