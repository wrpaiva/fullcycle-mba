from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatorio Corporativo SuperTechIABrazil 2024', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.chapter_title('1. Resumo Executivo')
pdf.chapter_body(
    "A SuperTechIABrazil e uma empresa lider em inovacao tecnologica no mercado brasileiro. "
    "No ano fiscal de 2023, a empresa consolidou sua posicao com resultados expressivos."
)

pdf.chapter_title('2. Desempenho Financeiro')
pdf.chapter_body(
    "O faturamento da Empresa SuperTechIABrazil no ultimo periodo foi de 10 milhoes de reais. "
    "Este valor representa um crescimento de 15% em relacao ao ano anterior. "
    "O lucro liquido apurado foi de 2 milhoes de reais, demonstrando a eficiencia operacional da companhia."
)

pdf.chapter_title('3. Estrutura e Localizacao')
pdf.chapter_body(
    "A sede da empresa esta localizada na cidade de Sao Paulo, no bairro do Itaim Bibi. "
    "Atualmente, contamos com uma equipe de 50 colaboradores altamente qualificados, "
    "focados no desenvolvimento de solucoes de Inteligencia Artificial para o setor varejista."
)

pdf.chapter_title('4. Projetos e Futuro')
pdf.chapter_body(
    "Para o ano de 2024, a SuperTechIABrazil planeja expandir suas operacoes para o mercado latino-americano, "
    "com foco inicial no Chile e na Colombia. Nao ha dados consolidados sobre o numero de clientes para 2024 ainda."
)

pdf.output('/home/ubuntu/SuperTechIABrazil.pdf')
print("PDF gerado com sucesso: SuperTechIABrazil.pdf")
