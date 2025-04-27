import csv
import os
from datetime import datetime
from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        # Logo
        
        # Title
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Data Analysis Report', 0, 1, 'C')
        # Date
        self.set_font('Arial', '', 10)
        self.cell(0, 10, f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 1, 'C')
        # Line break
        self.ln(10)
    
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

def read_data(filename):
    """Read data from CSV file and return as list of dictionaries"""
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        print(f"Current directory: {os.getcwd()}")
        raise

def analyze_data(data):
    """Perform basic analysis on the data"""
    if not data:
        return {}
    
    # Get all numeric fields (safer implementation)
    numeric_fields = []
    for key in data[0].keys():
        try:
            # Test if all values in this column can be converted to float
            for row in data:
                float(str(row[key]).replace(',', ''))
            numeric_fields.append(key)
        except (ValueError, TypeError):
            continue
    
    analysis = {
        'total_records': len(data),
        'fields': list(data[0].keys()),
        'numeric_fields': numeric_fields,
        'stats': {}
    }
    
    for field in numeric_fields:
        values = []
        for row in data:
            try:
                value = float(str(row[field]).replace(',', ''))
                values.append(value)
            except (ValueError, TypeError):
                continue
        
        if values:  # Only calculate if we found valid numbers
            analysis['stats'][field] = {
                'min': min(values),
                'max': max(values),
                'avg': sum(values) / len(values),
                'sum': sum(values)
            }
    
    return analysis

def generate_report(data, analysis, output_filename='report.pdf'):
    """Generate PDF report from data and analysis"""
    pdf = PDFReport()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    
    # Report Summary
    pdf.cell(0, 10, 'Report Summary', 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, f'Total records analyzed: {analysis["total_records"]}', 0, 1)
    pdf.cell(0, 6, f'Data fields: {", ".join(analysis["fields"])}', 0, 1)
    pdf.ln(5)
    
    # Statistics for numeric fields
    if analysis['numeric_fields']:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Numeric Field Statistics', 0, 1, 'L')
        pdf.set_font('Arial', '', 10)
        
        for field in analysis['numeric_fields']:
            stats = analysis['stats'][field]
            pdf.cell(0, 6, f'Field: {field}', 0, 1)
            pdf.cell(0, 6, f'  Minimum: {stats["min"]:.2f}', 0, 1)
            pdf.cell(0, 6, f'  Maximum: {stats["max"]:.2f}', 0, 1)
            pdf.cell(0, 6, f'  Average: {stats["avg"]:.2f}', 0, 1)
            pdf.cell(0, 6, f'  Sum: {stats["sum"]:.2f}', 0, 1)
            pdf.ln(2)
    
    # Sample Data Table
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Sample Data (First 10 Rows)', 0, 1, 'L')
    
    # Table header
    pdf.set_font('Arial', 'B', 10)
    col_widths = [40, 30, 30, 30]  # Adjust based on your data
    headers = analysis['fields'][:4]  # Show first 4 columns
    
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 7, header, 1, 0, 'C')
    pdf.ln()
    
    # Table rows
    pdf.set_font('Arial', '', 8)
    for row in data[:10]:  # Show first 10 rows
        for i, header in enumerate(headers):
            pdf.cell(col_widths[i], 6, str(row.get(header, '')), 1, 0, 'C')
        pdf.ln()
    
    # Save the PDF with verification
    output_path = os.path.abspath(output_filename)
    pdf.output(output_path)
    if os.path.exists(output_path):
        print(f"Success! Report saved to: {output_path}")
        return True
    else:
        print("Error: Failed to create PDF file")
        return False

if __name__ == "__main__":
    # Example usage
    input_file = r'filePath.csv'  #Put your File here 
    output_file = 'sales_report.pdf'
    
    try:
        print("Reading data...")
        data = read_data(input_file)
        
        print("Analyzing data...")
        analysis = analyze_data(data)
        
        print("Generating report...")
        if generate_report(data, analysis, output_file):
            print("Process completed successfully!")
            # Optionally open the PDF
            os.startfile(os.path.abspath(output_file))
    except Exception as e:
        print(f"Error occurred: {str(e)}")
