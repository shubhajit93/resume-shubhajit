from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader
import subprocess

root = Path(__file__).resolve().parent
out = root / 'output' / 'cover_letters'
qa = root / 'tmp' / 'pdfs'
out.mkdir(parents=True, exist_ok=True)
qa.mkdir(parents=True, exist_ok=True)
pdf = out / 'Shubhajit_Nandi_Zalando_Java_Kafka_Cover_Letter.pdf'
body = ParagraphStyle('body', fontName='Helvetica', fontSize=10.8, leading=15.8, spaceAfter=11)
name = ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=20, leading=24, spaceAfter=7)
small = ParagraphStyle('small', fontName='Helvetica', fontSize=9.4, leading=13, spaceAfter=4)
subject = ParagraphStyle('subject', fontName='Helvetica-Bold', fontSize=11, leading=15, spaceAfter=15)
paragraphs = [
"Dear Zalando Hiring Team,",
"I'm applying for the Senior Software Backend Engineer - Java / Kafka position in Bucharest. Your team's work connecting SAP with the wider Zalando ecosystem interests me because it closely relates to my experience building backend integrations, Kafka data pipelines, and services that I help operate in production.",
"At Verbex, I built a data-warehousing pipeline using Apache Kafka and Kafka Connect that reduced processing latency by approximately 50%. I also developed a custom Kafka Connect transformation plugin to reshape complex source data for downstream reporting. Alongside this work, I built Java 21 and Spring Boot services for a conversational voice platform using Axon Framework and CQRS.",
"Currently, I lead a five-engineer team delivering ASAT-V2, a security-awareness SaaS platform. I remain hands-on with Spring Boot services and backend APIs, including Stripe and PayPal integrations. I also own the production environment and DevOps operations: preparing development, test, and staging environments, building GitHub Actions CI/CD pipelines, deploying services, and maintaining monitoring, alerting, and incident response. This responsibility keeps me involved beyond implementation, through release and ongoing operation.",
"Earlier, at Dotlines, I developed Java payment-gateway services deployed on Grameenphone and Banglalink platforms, integrating multiple external payment providers. That experience would be valuable when working through integration challenges with Zalando's application and platform teams.",
"Across more than 11 years in software engineering, I have worked with different technologies and business domains. My strongest contribution to this role would be practical Java and Kafka integration experience, production ownership, and a collaborative approach to delivery. I also mentor frontend engineers on architecture and API integration, helping keep service behavior and user workflows aligned.",
"I would welcome the opportunity to bring this experience to ERP Engineering, learn your SAP integration landscape, and contribute to reliable data exchange across Zalando.",
]
flow = [Paragraph('SHUBHAJIT NANDI', name),
        Paragraph('Dhaka, Bangladesh | +8801779014069 | shubhajitcse59@gmail.com', small),
        Paragraph('<link href="https://linkedin.com/in/shubhajit-nandi">linkedin.com/in/shubhajit-nandi</link> | <link href="https://github.com/shubhajit93">github.com/shubhajit93</link>', small),
        Spacer(1,15), Paragraph('3 November 2026', small), Spacer(1,10),
        Paragraph('Application for Senior Software Backend Engineer - Java / Kafka', subject)]
flow.extend(Paragraph(escape(p), body) for p in paragraphs)
flow.append(Paragraph('Kind regards,<br/><b>Shubhajit Nandi</b>',body))
SimpleDocTemplate(str(pdf),pagesize=(595.28,841.89),leftMargin=48,rightMargin=48,topMargin=40,bottomMargin=40,title='Cover Letter - Senior Software Backend Engineer Java Kafka - Zalando',author='Shubhajit Nandi').build(flow)
reader=PdfReader(pdf)
assert len(reader.pages)==1
text=reader.pages[0].extract_text()
assert all(s in text for s in ['Bucharest','Kafka Connect','50%','ERP Engineering','Kind regards'])
subprocess.run([r'C:\Users\Lenovo\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe','-scale-to','1400','-png',str(pdf),str(qa/'zalando-java-kafka-cover-letter')],check=True,capture_output=True)
print(f'Verified one-page PDF: {pdf}')
