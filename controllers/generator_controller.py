# controllers/generator_controller.py
from models.product_model import ProductModel
from views.report_view import ReportView

class GeneratorController:
    def __init__(self):
        self.model = ProductModel()
        self.view = ReportView()

    def run(self):
        geradores = self.model.criar_geradores()
        self.view.gerar_csv(geradores)
        self.view.gerar_pdf(geradores)
