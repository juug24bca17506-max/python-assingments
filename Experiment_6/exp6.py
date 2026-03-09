def dictionaries():
   student = {
        "name": "Alice",
        "age": 22,
        "major": "Computer Science",
        "gpa": 3.8
    }
    print(f"Original Dictionary: {student}")
    
    print(f"Student's Name: {student['name']}")
    
    print(f"Student's GPA using get: {student.get('gpa')}")
    
    student["graduation year"] = 2026
    student["gpa"] = 3.9
    print(f"After updating: {student}")
    
    student.update({"age": 23, "honors": True})
    print(f"After update : {student}")
    
    print(f"Dictionary Keys: {student.keys()}")
    print(f"Dictionary Values: {student.values()}")
    print(f"Dictionary Items: {student.items()}")
    
    removed_major = student.pop("major")
    print(f"Removed Major: {removed_major}")
    
    last_item = student.popitem()
    print(f"Removed last item: {last_item}")
    
    student.clear()
    print(f"Dictionary after clear(): {student}")

dictionaries()
