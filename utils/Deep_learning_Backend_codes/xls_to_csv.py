import pandas as pd


def convert_xls_to_csv(input_file, output_file):
    try:
        # Read the Excel file, skipping the header row
        df = pd.read_excel(input_file, header=None)

        # Write the DataFrame to CSV without including headers
        df.to_csv(output_file, index=False, header=False)

        print("Conversion successful!")
    except Exception as e:
        print(f"Conversion failed. Error: {str(e)}")

