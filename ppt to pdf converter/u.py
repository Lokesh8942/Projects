import os
import comtypes.client
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_pptx_to_pdf(input_file, output_file=None):
    """Convert a PPTX file to PDF using Microsoft PowerPoint."""
    try:
        # Create PowerPoint application object
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        powerpoint.Visible = 1

        # Open the presentation
        presentation = powerpoint.Presentations.Open(input_file)

        # Save as PDF
        presentation.SaveAs(output_file, 32)  # 32 is the format for PDF

        # Close the presentation and PowerPoint application
        presentation.Close()
        powerpoint.Quit()
        print(f"Converted '{input_file}' to PDF as '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

def choose_file(title):
    """Open a file dialog to choose a file."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=title, filetypes=[("PowerPoint files", "*.pptx")])
    return file_path

def choose_output_file(title):
    """Open a file dialog to choose the output PDF file path."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(title=title, defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    return file_path

if __name__ == "__main__":
    # Choose the input PPTX file
    input_pptx_file = choose_file("Select a PPTX file")
    
    if input_pptx_file:
        # Choose the output PDF file
        output_pptx_file = choose_output_file("Save PDF as")
        
        if output_pptx_file:
            # Check if the input PPTX file exists
            if os.path.exists(input_pptx_file):
                # Check if the output file already exists
                if os.path.exists(output_pptx_file):
                    if messagebox.askyesno("File Exists", f"The file '{output_pptx_file}' already exists. Do you want to overwrite it?"):
                        convert_pptx_to_pdf(input_pptx_file, output_pptx_file)
                    else:
                        print("Conversion cancelled.")
                else:
                    convert_pptx_to_pdf(input_pptx_file, output_pptx_file)
            else:
                print(f"The file '{input_pptx_file}' does not exist.")
        else:
            print("No output file selected.")
    else:
        print("No input file selected.")