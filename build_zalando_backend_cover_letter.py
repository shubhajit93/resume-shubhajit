from pathlib import Path
from xml.sax.saxutils import escape
import subprocess
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader

root = Path(__file__).resolve().parent
out = root / 'output' / 'cover_letters'
out.mkdir(parents=True, exist_ok=True)
qa = root / 'tmp' / 'pdfs'
qa.mkdir(parents=True, exist_ok=True)
stem = 'Shubhajit_Nandi_Zalando_Software_Backend_Java_Kafka_Cover_Letter'
paragraphs = [
    'Dear Zalando Hiring Team,',
    'I am applying for the Software Backend Engineer - Java / Kafka position in Bucharest. Your ERP Engineering team\'s work connecting SAP with the wider Zalando ecosystem interests me because it brings together the areas I enjoy most: building backend services, integrating systems, and keeping data moving reliably in production. I bring over 11 years of software engineering experience, including Java payment integrations, Spring Boot services, and Kafka data pipelines.',
    'At Verbex, I built a Kafka and Kafka Connect data-warehousing pipeline that reduced processing latency by approximately 50%. I also developed a custom Kafka Connect transformation plugin to prepare source data for BI dashboards and built seven Java 21 and Spring Boot services using Axon Framework and CQRS. This experience is directly relevant to developing and maintaining the event-driven integrations your team operates.',
    'In my current role at Aspire Tech Services and Solutions Corp., I lead five engineers delivering ASAT-V2 while remaining hands-on with Spring Boot development and production operations. My work includes authentication and billing services, Stripe and PayPal integrations, and ownership of deployment environments and GitHub Actions CI/CD pipelines. I maintain monitoring, logging, and alerts, respond to production issues, and use Grafana k6 for load testing and performance analysis. I also work with AWS, Terraform, Docker, and Kubernetes.',
    'Earlier, at Dotlines Bangladesh, I developed Java payment-gateway services deployed on Grameenphone and Banglalink platforms, integrating third-party payment providers. Working across these systems has taught me to consider operational reliability alongside implementation. Although my current responsibilities include team leadership, I am particularly interested in this role\'s hands-on focus on integration pipelines and day-to-day service reliability.',
    'I would welcome the opportunity to contribute this experience to Zalando\'s ERP Engineering team, share knowledge with colleagues, and develop a deeper understanding of your SAP integration landscape. Thank you for considering my application.',
    'Kind regards,',
    'Shubhajit Nandi',
]
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=20, leading=24, spaceAfter=7),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=3),
    'subject': ParagraphStyle('subject', fontName='Helvetica-Bold', fontSize=11, leading=15, spaceAfter=17),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10.5, leading=15, spaceAfter=11),
}
flow = [Paragraph('SHUBHAJIT NANDI', styles['name']),
        Paragraph('Dhaka, Bangladesh | +8801779014069 | shubhajitcse59@gmail.com', styles['contact']),
        Paragraph('<link href="https://linkedin.com/in/shubhajit-nandi">linkedin.com/in/shubhajit-nandi</link> | <link href="https://github.com/shubhajit93">github.com/shubhajit93</link>', styles['contact']),
        Spacer(1, 20),
        Paragraph('Application: Software Backend Engineer - Java / Kafka<br/>Zalando | ERP Engineering | Bucharest', styles['subject'])]
flow += [Paragraph(escape(p), styles['body']) for p in paragraphs]
pdf = out / (stem + '.pdf')
SimpleDocTemplate(str(pdf), pagesize=(595.28, 841.89), leftMargin=48, rightMargin=48, topMargin=43, bottomMargin=43, title='Shubhajit Nandi - Zalando Java / Kafka Cover Letter', author='Shubhajit Nandi').build(flow)
(out / (stem + '.md')).write_text('# Shubhajit Nandi\n\nDhaka, Bangladesh | +8801779014069 | shubhajitcse59@gmail.com\n\nApplication: Software Backend Engineer - Java / Kafka, Zalando, Bucharest\n\n' + '\n\n'.join(paragraphs) + '\n', encoding='utf-8')
reader = PdfReader(str(pdf))
assert len(reader.pages) == 1
text = reader.pages[0].extract_text()
assert all(term in text for term in ['Kafka Connect', '50%', 'Terraform', 'Kind regards', 'Shubhajit Nandi'])
subprocess.run([r'C:\Users\Lenovo\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe', '-scale-to', '1200', '-png', str(pdf), str(qa / stem)], check=True, capture_output=True)
print(str(pdf))
print('Verified: one page, extractable text; words:', len(text.split()))
