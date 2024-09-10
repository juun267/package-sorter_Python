def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length
    
    # Determine if the package is bulky
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in [width, height, length])
    
    # Determine if the package is heavy
    is_heavy = mass >= 20
    
    # Determine the category based on the conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    
# Test cases
print(sort(100, 100, 100, 10))  # STANDARD
print(sort(150, 50, 50, 10))    # SPECIAL (bulky)
print(sort(100, 100, 100, 25))  # SPECIAL (heavy)
print(sort(200, 200, 200, 30))  # REJECTED (bulky and heavy)
