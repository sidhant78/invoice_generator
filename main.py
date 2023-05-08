import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
list = glob.glob("xlx files/*xlsx")
for l in list:
    pdf = FPDF(orientation="p",unit="mm",format="A4")
    pdf.add_page()
    filename = Path(l).stem
    invoice_no = filename.split("-")[0]
    pdf.set_font(family="Times",style='B',size=16)
    pdf.cell(w=50,h=8,txt=f"Invoice no:{invoice_no}", ln=1)
    date = filename.split("-")[1]
    pdf.set_font(family="Times", style='B', size=16)
    pdf.cell(w=50, h=8, txt=f"date:{date}",ln=1)
    df = pd.read_excel(l, sheet_name="Sheet 1")
    columns = df.columns
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=50, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    for index,row in df.iterrows():
        pdf.set_font(family="Times",  size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]),border=1)
        pdf.cell(w=50, h=8, txt=str(row["product_name"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1, ln=1)
    summation = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(summation), border=1, ln=1)
    pdf.set_font(family="Times", size=14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=25, h=8, txt=f"The total sum is {summation}",ln=1)
    pdf.image("pythonhow.png",w=10)
    pdf.output(f"PDF/{filename}.pdf")


