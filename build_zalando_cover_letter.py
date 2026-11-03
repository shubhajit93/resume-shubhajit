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
pdf = out / 'Shubhajit_Nandi_Zalando_Cover_Letter.pdf'
body = ParagraphStyle('body', fontName='Helvetica', fontSize=10.8, leading=15.8, spaceAfter=11)
name = ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=20, leading=24, spaceAfter=7)
small = ParagraphStyle('small', fontName='Helvetica', fontSize=9.4, leading=13, spaceAfter=4)
subject = ParagraphStyle('subject', fontName='Helvetica-Bold', fontSize=11, leading=15, spaceAfter=15)
paragraphs = [
"Dear Zalando Hiring Team,",
"I'm applying for the Software Engineer position in Fulfillment Core in Dortmund. The opportunity to build inventory services and integrate third-party logistics providers interests me because it combines work I enjoy: backend development, external-system integration, and responsibility for production operations.",
"Over the past 11 years, I have built systems across telecom, payments, and SaaS using Java, Spring Boot, Python, and C. At Dotlines, I developed Java payment-gateway services deployed on Grameenphone and Banglalink platforms, integrating multiple payment providers. I also built an SMS messaging platform handling 3,000 transactions per second while reducing per-message routing costs by 90% compared with third-party providers. These projects required attention to both technical performance and the business value of integration decisions.",
"In my current role, I lead five engineers delivering ASAT-V2, a security-awareness SaaS platform, while remaining hands-on with backend development. My responsibilities span Spring Boot services, AWS infrastructure, deployment pipelines, monitoring, alerting, and incident response. I also work closely with frontend engineers to align APIs and user workflows across billing, training, and phishing-simulation modules.",
"Previously, at Verbex, I built Kafka-based data pipelines that reduced processing latency by approximately 50%. My background also includes relational databases and earlier production development in PHP.",
"I would bring this combination of backend development, integration experience, and operational ownership to Fulfillment Core. I'm particularly interested in learning the inventory domain and working with engineering and product colleagues to turn business requirements into dependable services. Joining a new team and contributing to its technical decisions and working practices would be a meaningful next step for me.",
"I would welcome the opportunity to discuss how my experience could support Zalando's inventory platform and logistics integrations.",
"Kind regards,<br/><b>Shubhajit Nandi</b>",
]
flow = [Paragraph('SHUBHAJIT NANDI', name),
        Paragraph('Dhaka, Bangladesh | +8801779014069 | shubhajitcse59@gmail.com', small),
        Paragraph('<link href="https://linkedin.com/in/shubhajit-nandi">linkedin.com/in/shubhajit-nandi</link> | <link href="https://github.com/shubhajit93">github.com/shubhajit93</link>', small),
        Spacer(1, 15), Paragraph('3 November 2026', small), Spacer(1, 10),
        Paragraph('Application for Software Engineer - Fulfillment Core', subject)]
flow.extend(Paragraph(p if p.startswith('Kind regards') else escape(p), body) for p in paragraphs)
SimpleDocTemplate(str(pdf),pagesize=(595.28,841.89),leftMargin=48,rightMargin=48,topMargin=40,bottomMargin=40,title='Cover Letter - Software Engineer, Fulfillment Core - Zalando',author='Shubhajit Nandi').build(flow)
reader = PdfReader(pdf)
assert len(reader.pages)==1, len(reader.pages)
assert all(s in reader.pages[0].extract_text() for s in ['Fulfillment Core','3,000','90%','PHP','Kind regards'])
subprocess.run([r'C:\Users\Lenovo\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe','-scale-to','1400','-png',str(pdf),str(qa/'zalando-cover-letter')],check=True,capture_output=True)
print(str(pdf))
