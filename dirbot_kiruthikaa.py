"""
File: dirbot_kiruthikaa.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Hint: See the Textbook, Skill Drills, and GUIDES for code snippets to help complete this module.

Author: Kiruthikaa NS


"""

#####################################
# Import Modules at the Top
#####################################

# Import from the Python Standard library
import pathlib
import sys     
import time 
from typing import List


# Import packages from requirements.txt
import loguru   

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules

import utils_kiruthikaa
from utils_kiruthikaa import supplier_names, get_byline

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare global variables
#####################################

# Create a project path object for the root directory of the project.
ROOT_DIR = pathlib.Path.cwd()

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.

    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''

    # Log function name and parameters
    logger.info("FUNCTION: create_folders_for_range()")
    logger.info(f"PARAMETERS: start_year = {start_year}, end_year = {end_year}")


    for year in range(start_year, end_year + 1):
        year_path = ROOT_DIR / str(year)
        year_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {year_path}")

    for supplier in supplier_names:
        supplier_path = year_path / str(supplier)
        supplier_path.mkdir(exist_ok=True)
        logger.info(f"Created subfolder for supplier under year: {supplier_path}")
  
#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 

# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool= False, remove_spaces: bool = False) -> None:
    '''
    Create folders based on a list of folder names.
    
    Arguments:
    folder_list -- A list of strings representing folder names.
     to_lowercase -- Whether to convert names to lowercase.
    remove_spaces -- Whether to replace spaces with underscores.
    '''

    logger.info("FUNCTION: create_folders_from_list()")
    logger.info(f"PARAMETER: folder_list = {folder_list}, to_lowercase = {to_lowercase}, remove_spaces = {remove_spaces}")

   # Loop through the list of folder names
    for folder_name in folder_list:
        original_name = folder_name  # Store the original name for logging
        logger.info(f"Processing folder name: {original_name}")

        # Apply transformations if needed
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")  # Replace spaces with underscores
            logger.info(f"Transformed folder name: {folder_name}")
        #Folder creation logic
        folder_path = ROOT_DIR / folder_name  # Define folder path
        folder_path.mkdir(exist_ok=True)  # Create folder if it doesn't exist
        logger.info(f"Created folder: {folder_path}")  # Log folder creation

  

#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################

def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each item in a list 
    using a concise form of a for loop called a list comprehension.

    Arguments:
    folder_list -- A list of strdings (e.g., ['csv', 'excel']).
    prefix -- A string to prefix each name (e.g., 'output-').
    '''

    logger.info("FUNCTION: create_prefixed_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, prefix = {prefix}")

       # List comprehension to apply prefix to all folder names
    prefixed_folders = [prefix + name for name in folder_list]
    logger.info(f"Prefixed folder names: {prefixed_folders}")

    # Folder creation logic
    # Loop through the prefixed folder names
    for folder_name in prefixed_folders:
        folder_path = ROOT_DIR / folder_name
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created prefixed folder: {folder_path}")



#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically over time.

    Arguments:
    duration_seconds -- The number of seconds to wait between folder creations.
    '''    
    logger.info("FUNCTION: create_folders_periodically()")
    logger.info(f"PARAMETER: duration_seconds = {duration_seconds}")

    number_of_folders = 5  # Number of folders to create
    folder_name = "periodic_folder"  # Base name for folders        
    for i in range(1, number_of_folders +1):
        folder_path = ROOT_DIR / f"{folder_name}_{i}"
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")
        time.sleep(duration_seconds)  # Wait for the specified duration
        logger.info(f"Waited for {duration_seconds} seconds before creating the next folder.")




#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################

def create_standardized_folders(folder_list: List[str], to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of names with options to standardize names.

    Arguments:
    folder_list -- A list of strings representing folder names.
    to_lowercase -- If True, convert names to lowercase.
    remove_spaces -- If True, remove spaces from names.
    '''

    logger.info("FUNCTION: create_standardized_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, to_lowercase = {to_lowercase}, remove_spaces = {remove_spaces}")

    for name in folder_list:
        original_name = name

        # Apply transformations
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(" ", "")

        folder_path = ROOT_DIR / name
        folder_path.mkdir(exist_ok=True)

        logger.info(f"Created folder: {folder_path} (original name: '{original_name}')")


#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    logger.info("#####################################")
    logger.info("# Starting execution of main()")
    logger.info("#####################################\n")


    logger.info(f"Byline: {utils_kiruthikaa.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using list comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'output-'
    create_prefixed_folders_using_list_comprehension(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call function 5 to create standardized folders, no spaces, lowercase
    create_standardized_folders(supplier_names, to_lowercase=True, remove_spaces=True)

    logger.info("\n#####################################")
    logger.info("# Completed execution of main()")
    logger.info("#####################################")
    logger.info("All folders created successfully!")
    logger.info("Check the project.log file for details.")
    logger.info("Check the project directory for created folders.")
    logger.info("Exiting program.")
    logger.info("#####################################\n")



#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()