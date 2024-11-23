import warnings
warnings.simplefilter('default', DeprecationWarning)


from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=48)
pdf.cell(text="hello world")
pdf_bytes = pdf.output()


WIDTH, HEIGHT = 800, 400
from base64 import b64encode
from IPython.display import display, HTML
base64_pdf = b64encode(pdf_bytes).decode("utf-8")
display(HTML(f'<embed src="data:application/pdf;base64,{base64_pdf}" width="{WIDTH}" height="{HEIGHT}" type="application/pdf">'))

display(HTML(f'<a download="fpdf2-demo.pdf" href="data:application/pdf;base64,{base64_pdf}">Click to download PDF</a>'))