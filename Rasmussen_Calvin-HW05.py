import openpyxl
from openpyxl.styles import PatternFill

# Initialize a workbook and set up the active sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Pixel Art"

# Step 1: Set cell dimensions to create a square appearance
cell_width = 2  # Adjust as needed
cell_height = cell_width * 6  # Approximate to keep cells square
for col in range(1, 20):  # Adjust range for the size of your art
    col_letter = openpyxl.utils.get_column_letter(col)
    sheet.column_dimensions[col_letter].width = cell_width
for row in range(1, 20):  # Adjust range for the size of your art
    sheet.row_dimensions[row].height = cell_height

# Step 2: Define the pixel art pattern using a dictionary
# Format: {color_code: [cell_coordinates]}
pixel_art_data = {
    "#FF5733": ["A1", "A2", "B1", "B2"],  # Example cells for one color
    "#33FF57": ["A3", "A4", "B3", "B4"],  # Example cells for another color
    "#3357FF": ["C1", "C2", "D1", "D2"],  # And so on
    "#FFFF33": ["C3", "C4", "D3", "D4"],
    "#FF33FF": ["E1", "E2", "F1", "F2"]
}

# Step 3: Apply colors to the specified cells
for color, cells in pixel_art_data.items():
    fill = PatternFill(start_color=color[1:], end_color=color[1:], fill_type="solid")
    for cell in cells:
        sheet[cell].fill = fill

# Save the workbook
wb.save("pixel_art.xlsx")
