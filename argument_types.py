def greet_me_please(my_name: str) -> str:
    print(f"Type of my name is {type(my_name)}")
    return True

return_value = greet_me_please("Mike")
print(f"Type of return value is {type(return_value)}")
