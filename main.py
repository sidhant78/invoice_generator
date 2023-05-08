import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
list = glob.glob("xlx files/*xlsx")
for l in list:
    df = pd.read_excel(l, sheet_name="Sheet 1")
    pdf = FPDF(orientation="p",unit="mm",format="A4")
    pdf.add_page()
    filename = Path(l).stem
    invoice_no = filename.split("-")
    pdf.set_font(family="Times",style='B',size=16)
    pdf.cell(w=50,h=8,txt=f"Invoice no:{invoice_no}")
    pdf.output(f"PDF/{filename}.pdf")


