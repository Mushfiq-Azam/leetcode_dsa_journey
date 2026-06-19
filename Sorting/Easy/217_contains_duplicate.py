#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    # Create a set to store unique elements
    seen = set()
    
    # Iterate through each number in the array
    for num in nums:
        # If the number is already in the set, return True
        if num in seen:
            return True
        # Otherwise, add the number to the set
        seen.add(num)
    
    # If no duplicates were found, return False
    return False