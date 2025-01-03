from fpdf import FPDF

user_name = input("Name: ").title()

if not isinstance(user_name, str):
    raise ValueError("Invalid Name")
else:
    pdf = FPDF(format="A4")
    pdf.add_page()

    #image
    page_width = pdf.w
    page_height = pdf.h
    image_path = "shirtificate.png"
    image_width = 190
    image_height = 190

    x_position = (page_width - image_width) / 2
    y_position = (page_height - image_height) / 2
    pdf.image(image_path, x=x_position, y=y_position, w=image_width, h=image_height)

    #cs50 shirtificate text
    pdf.set_font("Helvetica", size=45, style="")
    pdf.cell(0, 40, "CS50 Shirtificate", border=0, ln=True, align="C")

    #took cs50 text
    pdf.set_font("Helvetica", size=25, style="")
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 150, f"{user_name} took CS50", border=0, ln=True, align="C")

    pdf.output("shirtificate.pdf")

