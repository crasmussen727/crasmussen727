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
    "#FFB6C1": ["D5", "E5", "F5", "C6", "D6", "E6", "F6", "G6", "C7", "G7", "B8", "C8", "G8", "H8", "B9", "D9", "E9", "F9", "H9", "B10", "C10", "G10", "H10"],
    "#FF69B4": ["D11", "F11"],  # Cheeks
    "#FF4500": ["C12", "G12"],  # Feet
    "#000000": ["D7", "F7", "C9", "G9"],  # Eyes and outline
    "#FFFFFF": ["D6", "F6"]  # Eye highlights
}

# Step 3: Apply colors to the specified cells
for color, cells in pixel_art_data.items():
    fill = PatternFill(start_color=color[1:], end_color=color[1:], fill_type="solid")
    for cell in cells:
        sheet[cell].fill = fill

# Save the workbook
wb.save("pixel_art.xlsx")
