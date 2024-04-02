from fpdf import FPDF


class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self.add_page()
        # Add image to pdf
        self.image("shirtificate.png", w=190, h=200, x=10, y=60)
        # Change style and position for heading
        self.set_font("Helvetica", size=50)
        self.set_xy(10, 27)
        self.cell(0, 10, text="CS50 Shirtificate", align="C")
        self.ln()
        # Change style and position for text on shirt
        self.set_xy(10, 120)
        self.set_font("Helvetica", size=20, style="B")
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, text=f"{self._name} took CS50", align="C")
        # Output pdf
        self.output("shirtificate.pdf")


Shirtificate(input("Name: "))
