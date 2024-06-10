import re
import os
from django.conf import settings
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from apps.information.models.service import Service


class PriceListService:
    def __init__(self, language):
        file_names = {
            'ru': 'Прейскурант цен.pdf',
            'en': 'Price list.pdf',
            'ky': 'Баалар тизмеси.pdf'
        }

        headers = {
            'ru': ['Название услуги', 'Статус услуги'],
            'en': ['Name of the service', 'Service status'],
            'ky': ['Кызматтын аталышы', 'Кызмат статусу']
        }

        self.file_name = file_names.get(language)
        header = headers.get(language)

        file_path = os.path.join(settings.MEDIA_ROOT, 'prices', self.file_name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        self.pdf = SimpleDocTemplate(file_path, pagesize=A4,
                                     rightMargin=20, leftMargin=20,
                                     topMargin=20, bottomMargin=20,
                                     )

        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))

        model = Service.objects.all()
        titles = list(model.values_list(f'title_{language}', flat=True))
        statuses = list(model.values_list(f'status_{language}', flat=True))

        self.data = [header]
        for tit, stat in zip(titles, statuses):
            if tit:
                tit_format = re.sub(r'(.{70,}?)\n?', r'\1\n', tit)  # Format long titles if needed
                query = [tit_format, stat]
                self.data.append(query)

        column_width = [400, 100]
        self.table = Table(self.data, colWidths=column_width)

        self.style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Arial-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Arial'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ])

        self.table.setStyle(self.style)

        self.elements = [self.table]
        self.pdf.build(self.elements)
