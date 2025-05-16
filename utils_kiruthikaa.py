"""
File: utils_kiruthikaa.py
Module Name: supplier_performance_tracker
Purpose: Reusable Module for supplier performance metrics Project. 

Description: This module helps analyze key supplier performance metrics 
to assess reliability and efficiency in supply chain management.

Author: Kiruthikaa NS
"""
    
#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics


#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# Boolean variable indicating whether suppliers meet delivery deadlines
suppliers_meet_deadlines: bool = True

# declare an integer variable 
# Integer for total suppliers being analyzed
total_suppliers: int = 15

# Function to check if the number of suppliers is even or odd
def is_even(number: int) -> bool:
    return number % 2 == 0
# Print whether the total supplier count is even or odd
print(f"Is the number of suppliers even? {is_even(total_suppliers)}")

# declare a floating point variable
# Floating-point variable for average supplier defect rate (percentage)
average_defect_rate: float = 2.3

# declare a list of strings
# Declare a list of supplier names
supplier_names: list = ["ABC Logistics", "Global Freight Co.", "Swift Supply Chain", "Evergreen Distribution", "NextGen Transport"]

# declare a list of numbers so we can illustrate statistics skills 
# List of delivery times in days for different suppliers
supplier_delivery_times: list = [2, 3, 5, 4, 2, 7, 3] 

# List of supplier reliability scores (scale of 1 to 5)
supplier_reliability_scores: list = [4.8, 3.9, 4.5, 4.2, 4.7] 

# Calculate basic statistics using built-in Python functions and the statistics module
# Calculate basic statistics on delivery time variability
min_delivery_time: int = min(supplier_delivery_times)  
max_delivery_time: int = max(supplier_delivery_times)  
mean_delivery_time: float = statistics.mean(supplier_delivery_times)  
stdev_delivery_time: float = statistics.stdev(supplier_delivery_times) 

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Supplier Performance Analytics
---------------------------------------------------------
Total Suppliers:            {total_suppliers}
Suppliers Meet Deadlines:   {suppliers_meet_deadlines}
Average Defect Rate:        {average_defect_rate}%
Supplier Names:             {", ".join(supplier_names)}
Supplier Reliability Scores:{supplier_reliability_scores}
Delivery Times (days):      {supplier_delivery_times}
Minimum Delivery Time:      {min_delivery_time}
Maximum Delivery Time:      {max_delivery_time}
Mean Delivery Time:         {mean_delivery_time:.2f}
Standard Deviation:         {stdev_delivery_time:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_kiruthikaa.py")
    print(get_byline())
    print("END main() in utils_kiruthikaa.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()