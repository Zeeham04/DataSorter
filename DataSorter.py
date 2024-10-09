import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load the dataset
def load_data(file_path):
    """
    This function loads the CSV data file into a pandas DataFrame.
    """
    # Check if the file exists before attempting to read it
    if not os.path.exists(file_path):
        print(f"Error: The file at {file_path} was not found.")
        return None
    
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading the file: {e}")
        return None

# Step 2: Searching and Filtering data based on the user's input
def search_data(df):
    """
    This function allows the user to filter the DataFrame based on their column and value choice.
    """
    # Display available columns to the user
    print("Available columns in the dataset:")
    print(df.columns)

    # Ask the user which column to filter by
    column_to_filter_by = input("Enter the name of the column you want to filter by: ").lower()  # Make case-insensitive

    # Check if the column exists in the dataset
    if column_to_filter_by not in df.columns.str.lower():
        print(f"Column '{column_to_filter_by}' not found.")
        return None

    # Ask the user for the value to filter by
    filter_value = input(f"Enter the value to filter {column_to_filter_by} by: ").lower()  # Make case-insensitive

    # Filter the data (convert both column and filter value to lowercase)
    filtered_data = df[df[column_to_filter_by].astype(str).str.lower() == filter_value]

    if filtered_data.empty:
        print(f"No data found for {column_to_filter_by} = {filter_value}")
        return None

    return filtered_data

# Step 3: Sort the filtered data based on user input
def sort_data(df):
    """
    This function allows the user to sort the DataFrame based on a specific column and order.
    """
    # Display available columns to the user
    print("Available columns in the dataset:")
    print(df.columns)

    # Ask the user which column to sort by
    column_to_sort_by = input("Enter the column you want to sort by: ").lower()  # Make case-insensitive

    # Check if the column exists in the dataset
    if column_to_sort_by not in df.columns.str.lower():
        print(f"Column '{column_to_sort_by}' not found.")
        return None

    # Ask the user if they want to sort in ascending or descending order
    sort_order = input("Do you want to sort in ascending or descending order? (asc/desc): ").lower()  # Case-insensitive

    # Validate user input for sort order
    if sort_order == 'asc':
        ascending = True
    elif sort_order == 'desc':
        ascending = False
    else:
        print("Invalid input for sort order. Please enter 'asc' or 'desc'.")
        return None

    # Sort the data
    sorted_data = df.sort_values(by=column_to_sort_by, ascending=ascending)

    return sorted_data

# Step 4: Display or save the sorted data
def display_or_save_data(df):
    """
    This function allows the user to either display the sorted data or save it to a CSV file.
    """
    action = input("Do you want to (d)isplay or (s)ave the data? (d/s): ").lower()  # Make case-insensitive

    if action == 'd':
        # Display the first few rows of the data
        print(df.head())
    elif action == 's':
        # Save the data to a CSV file
        output_file = input("Enter the filename to save the data (e.g., 'filtered_sorted_data.csv'): ")
        try:
            df.to_csv(output_file, index=False)
            print(f"Data saved to {output_file}")
        except Exception as e:
            print(f"Error saving the data: {e}")
    else:
        print("Invalid choice. Please enter 'd' to display or 's' to save.")

# Main program loop
def main_loop():
    while True:
        # Step 1: Load the dataset
        # Specify the absolute path to your file or ensure the relative path is correct
        file_path = r'C:\Users\Zeeha\Projects-Jobs\DataSorter\car_price_prediction_.csv'  # Replace with your actual file path
        
        # Check if the file exists and load data
        df = load_data(file_path)

        if df is not None:
            # Step 2: Search/filter the data based on user input
            filtered_data = search_data(df)

            if filtered_data is not None:
                # Step 3: Sort the filtered data based on user input
                sorted_data = sort_data(filtered_data)

                if sorted_data is not None:
                    # Step 4: Display or save the sorted and filtered data
                    display_or_save_data(sorted_data)

        # Ask the user if they want to run the program again
        rerun = input("Do you want to run the program again? (y/n): ").lower()  # Make case-insensitive
        if rerun != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main_loop()
