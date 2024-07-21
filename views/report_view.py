# views/report_view.py
import pandas as pd
from fpdf import FPDF

class ReportView:
    def gerar_csv(self, geradores):
        df_geradores = pd.DataFrame(geradores)
        df_geradores_exploded = df_geradores.explode(['ID Produto', 'Nome do Produto', 'Quantidade Item'])
        df_geradores_exploded.columns = ['ID Gerador', 'Potência do Gerador (em W)', 'ID Produto', 'Nome do Produto', 'Quantidade Item']
        df_geradores_exploded.to_csv('geradores_configurados.csv', index=False)

    def gerar_pdf(self, geradores):
        email_text = f"""
Prezada equipe de marketing,

Nesta semana, foram configurados {len(geradores)} geradores solares. Segue em anexo a tabela com os detalhes dos geradores.

Atenciosamente,
Equipe de Engenharia da Neosolar
"""

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Geradores Configurados - Relatório Semanal', 0, 1, 'C')
        pdf.ln(10)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, email_text)
        pdf.output('email_marketing.pdf')
