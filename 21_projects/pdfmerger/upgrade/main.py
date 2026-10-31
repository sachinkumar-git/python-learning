import pypdf
import os

def merge_selected_pages(input_files, output_filename):
    merger = pypdf.PdfWriter()

    for file_path, pages in input_files:
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found. Skipping.")
            continue
            
        reader = pypdf.PdfReader(file_path)
        total_pages = len(reader.pages)
        
        for page_num in pages:
            if 0 <= page_num < total_pages:
                merger.add_page(reader.pages[page_num])
            else:
                print(f"Warning: {file_path} only has {total_pages} pages. Skipping index {page_num}.")

    with open(output_filename, "wb") as output_pdf:
        merger.write(output_pdf)
    
    print(f"\n Success! Merged file saved as: {output_filename}")

files_to_process = []
n = int(input("How many PDFs do you want to merge?\n"))

for i in range(n):
    name = input(f"\nEnter the name of PDF {i + 1} (include .pdf): ")
    
    print(f"Which pages from {name}?")
    print("Example: '1,3,5' for specific pages or '1-4' for a range.")
    page_input = input("Pages: ")
    
    pages = []
    try:
        if "-" in page_input:
            # Handle range like 1-4 -> [0, 1, 2, 3]
            start, end = map(int, page_input.split("-"))
            pages = list(range(start - 1, end))
        else:
            # Handle list like 1,2,3 -> [0, 1, 2]
            pages = [int(p.strip()) - 1 for p in page_input.split(",")]
    except ValueError:
        print("Invalid page format! Skipping this file.")
        continue

    files_to_process.append((name, pages))


if files_to_process:
    output_name = input("\nEnter the name for the final merged PDF: ")
    if not output_name.endswith(".pdf"):
        output_name += ".pdf"
        
    merge_selected_pages(files_to_process, output_name)
else:
    print("No files were added to merge.")