# Data Sorting and Filtering Tool

This project is a Python-based tool for sorting and filtering data from a CSV file. It allows users to load a dataset, filter the data based on specified criteria, sort the filtered data, and either display or save the results. The tool is designed to be user-friendly and interactive.

## Features

1. **Load Data**:
   - Reads data from a CSV file into a pandas DataFrame.
   - Handles file existence checks and error handling for invalid files.

2. **Search and Filter Data**:
   - Allows filtering the dataset based on user-selected column values.
   - Provides a list of available columns for easy navigation.

3. **Sort Data**:
   - Enables sorting the filtered data based on a user-specified column and order (ascending or descending).

4. **Display or Save Data**:
   - Offers the choice to either display the sorted data in the console or save it to a new CSV file.

## Requirements

- Python 3.6+
- pandas
- matplotlib

To install the required libraries, run:
```bash
pip install pandas matplotlib
```

## Usage

1. Clone or download the project.
2. Ensure your CSV file is available and update the `file_path` variable in the `main_loop` function.
3. Run the script using:
   ```bash
   python script_name.py
   ```

### Main Workflow

1. **Load Dataset**:
   - The script prompts the user to provide the file path to the dataset. It loads the CSV file into a DataFrame.

2. **Filter Data**:
   - The script displays the available columns.
   - The user specifies a column and a value to filter the data.

3. **Sort Data**:
   - The script allows the user to select a column for sorting and choose the sort order (ascending/descending).

4. **Display or Save Data**:
   - The user can display the processed data in the console or save it to a CSV file.

5. **Repeat or Exit**:
   - After completing a cycle, the script prompts the user to rerun or exit the program.

## Example

Suppose you have a CSV file named `car_price_prediction_.csv` with the following columns:
```
['Make', 'Model', 'Year', 'Price']
```

### Sample Interaction:

1. **Filter**:
   - Select the column `Make`.
   - Enter the value `Toyota`.

2. **Sort**:
   - Sort the filtered results by the `Price` column in descending order.

3. **Display/Save**:
   - Save the filtered and sorted data to `filtered_sorted_data.csv`.

## Customization

- Update the `file_path` in the `main_loop` function to specify the path to your CSV file.
- Modify the filtering and sorting logic as needed to fit your dataset requirements.

## Error Handling

- The script checks for file existence and provides clear error messages if the file is not found or cannot be loaded.
- Validates user inputs for filtering and sorting to ensure the program runs smoothly.

## License

This project is open-source and available under the MIT License.
