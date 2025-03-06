import functions as f
from tqdm import tqdm # Will be used to display a progress bar, as books can be quite extensive in pages
import os # For directory management

directory = "pdf-pages/The Hobit" # Set the starting Directory here! Trial run here
pdf_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.pdf')] # List comprehension for directory

for i in tqdm(pdf_files, desc="Converting Files", unit="file"): # tqdm for progress update, this takes a bit, depending on pages
    f.read_pdf(i, pdf_files.index(i) + 1) # See functions, but it is taking a page number as input, to create the file name.

f.join_audio_files() # Join it all together

