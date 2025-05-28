# AUTOMATED-REPORT-GENERATION

"COMPANY": CODTECH IT SOLUTIONS

"NAME": TEJAS K

"INTERN ID": CT12WN103

"DOMAIN": PYTHON PROGRAMMING

"DURATION": 12 WEEKS

"MENTOR": NEELA SANTHOSH

"DESCRIPTION"

This Python script is designed to automate the process of reading a dataset from a CSV file, performing basic data analysis, and generating a detailed PDF report summarizing the findings. It makes use of several libraries, including csv for handling CSV files, os for file and directory operations, datetime for timestamping, and fpdf for creating PDF documents.
The code begins by defining a custom class, PDFReport, which inherits from the FPDF class. This class customizes the PDF by implementing a header and footer. The header includes a title and the current date and time when the report is generated. The footer displays the page number, allowing for easy navigation through multiple pages.

The function read_data(filename) is responsible for reading the CSV file. It uses the csv.DictReader to load the data into a list of dictionaries, where each dictionary represents a row. It also handles the FileNotFoundError gracefully by printing the current working directory and raising the exception if the file isn't found.
The analyze_data(data) function conducts basic statistical analysis on the dataset. It first identifies numeric fields by attempting to convert each column's entries to floats. If successful, the field is classified as numeric. It then computes minimum, maximum, average, and total (sum) values for each numeric field and stores these statistics in a dictionary for easy access. It also collects metadata such as the total number of records and the list of all field names.

The generate_report(data, analysis, output_filename='report.pdf') function is in charge of creating the final PDF document. It starts by generating a summary page that includes the number of records and a list of all fields. If numeric fields are found, it lists their corresponding minimum, maximum, average, and sum values. The function also adds a second page that displays a sample of the data — specifically, the first ten rows and first four columns — in a table format. It dynamically adjusts column widths and uses different font styles and sizes for better readability.

At the bottom of the script, within the if __name__ == "__main__": block, the script specifies an example input file path and output filename. It then sequentially calls the three main functions: read_data, analyze_data, and generate_report. If successful, it prints confirmation messages and automatically opens the generated PDF using os.startfile.
This script is highly modular, making it easy to adapt for different datasets or extend with more complex analysis in the future. Error handling ensures that if something goes wrong (like a missing file), meaningful error messages are printed. Furthermore, the generated PDF report is professional in appearance, with organized sections and formatting, making it ideal for business, academic, or personal reporting purposes.
Overall, this code provides a neat, efficient pipeline for basic data reporting: from raw CSV to a polished, shareable PDF document — all with minimal manual intervention.



Output:

![Image](https://github.com/user-attachments/assets/b9a441e0-da21-49ce-ab40-97bc986c0574)

![Image](https://github.com/user-attachments/assets/5abbd759-0661-4792-af00-318ebbcc66d3)
