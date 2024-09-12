class Page:
    def print_footer(self):
        print("Hola")

class LegalPage(Page):
    def print_footer(self):
        print("Mundo")
        super().print_footer()

# Mundo Hola