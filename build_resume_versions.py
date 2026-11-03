from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader
import subprocess
import os

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output' / os.environ.get('RESUME_OUTPUT_FOLDER', 'resumes')
QA = ROOT / 'tmp' / 'pdfs'
OUT.mkdir(parents=True, exist_ok=True)
QA.mkdir(parents=True, exist_ok=True)

B = {
'lead': 'Lead a five-engineer team delivering ASAT-V2, a security-awareness SaaS platform, owning backend architecture, Spring Boot services, and production delivery.',
'cdn': 'Reduced JavaScript asset loading time by approximately 50% by moving asset delivery to Amazon S3 and CloudFront.',
'backend': 'Built Spring Boot services for authentication, billing, phishing simulations, notifications, and reporting; integrated Stripe and PayPal with coupon, VAT, and discount handling.',
'deploy': 'Own the production environment and DevOps delivery for ASAT-V2. Set up development, test, and staging servers, configure deployment environments, and build GitHub Actions CI/CD pipelines for service deployment and versioned rollback.',
'ai': 'Built LLM content-generation workflows with structured outputs and tool calling, handling timeouts, retries, and rate limits for customer-specific phishing simulations.',
'aiops': 'Manage latency, token cost, caching, and tracing for AI integrations in ASAT-V2.',
'mentor': 'Mentored frontend engineers on micro-frontend design and implementation, aligning backend APIs and UI workflows across phishing, billing, and training modules.',
'k6': 'Used Grafana k6 for load testing and performance-metrics analysis of backend services.',
'mongo': 'Configured a three-member MongoDB replica set with automatic failover for the SaaS platform.',
'ops': 'Operate production services on AWS, maintaining Nginx/TLS, Grafana dashboards, logging, alerts, and incident response.',
'devops_owner': 'Own ASAT-V2 production infrastructure and DevOps operations, including server setup, environment configuration, and service deployment across development, test, staging, and production.',
'devops_pipeline': 'Build and maintain GitHub Actions CI/CD pipelines for container builds, service deployments, and versioned rollback; provision AWS infrastructure with Terraform and maintain Docker, Docker Compose, and Kubernetes configurations.',
'infra': 'Provisioned AWS infrastructure with Terraform and maintained container deployment configurations using Docker, Docker Compose, and Kubernetes.',
'voice': 'Built email, SMS, and voice phishing simulations, integrating Twilio and ElevenLabs and capturing participant responses for security-awareness risk reporting.',
}
V = {
'pipeline': 'Built a Kafka and Kafka Connect data-warehousing pipeline, reducing processing latency by approximately 50% for downstream analytics.',
'plugin': 'Developed a custom Kafka Connect transformation plugin to reshape complex source data for BI dashboards.',
'java': 'Built seven Spring Boot services for a conversational voice AI platform using Java 21, Axon Framework, and CQRS, covering agent management, call orchestration, and transcription analysis.',
'sip': 'Integrated LiveKit SIP trunking to support inbound and outbound calls for the conversational AI platform.',
'deploy': 'Implemented GitHub Actions pipelines with Docker and Kubernetes for containerized service deployments.',
}
D = {
'sms': 'Built a C-based SMSC using SMPP, SS7, and SCTP, handling 3,000 TPS and reducing per-message routing costs by 90% compared with third-party providers.',
'call': 'Developed an asynchronous outbound-call gateway using Python, FastAPI, asyncio, and NATS JetStream to increase parallel call-processing capacity.',
'pay': 'Developed Java payment-gateway services deployed on Grameenphone and Banglalink platforms, integrating multiple third-party payment providers.',
}
S = ['Developed SMS delivery systems in C and PHP with MySQL and Redis, running on Banglalink\'s production platform at 2,000 TPS.', 'Built reusable SMPP and SIP libraries in C for multiple telecom projects; implemented call-patching and conference-call features using Asterisk.']

common = [
('Languages & Backend', 'Java, Python, C, Spring Boot, Spring Cloud, Hibernate, FastAPI'),
('Messaging & Data', 'Apache Kafka, Kafka Connect, NATS JetStream, AWS SQS, PostgreSQL, MySQL, MongoDB, Redis'),
('Cloud & Delivery', 'AWS, Terraform, Docker, Docker Compose, Kubernetes, GitHub Actions, Amazon S3, CloudFront'),
('Operations & Performance', 'Grafana, Grafana k6, load testing, logging, alerting, incident response'),
]

versions = [
dict(slug='01_Senior_Backend_Java', title='Senior Backend Engineer | Java, Spring Boot, AWS',
 summary='Senior software engineer with 11+ years building backend systems across telecom, cybersecurity, and voice AI. Lead five engineers delivering a Spring Boot SaaS platform, owning backend architecture, production operations, and DevOps delivery. Experience includes Kafka data pipelines, operator payment integrations, and messaging systems handling 3,000 TPS.',
 skills=common+[('Architecture & Integrations','Microservices, event-driven architecture, CQRS, Axon Framework, LLM APIs, Stripe, PayPal')],
 aspire=['lead','cdn','backend','ai','deploy','mentor','mongo'], verbex=['pipeline','plugin','java','deploy'], dots=['sms','pay','call']),
dict(slug='02_Technical_Lead', title='Senior Software Engineer | Backend Architecture & Technical Leadership',
 summary='Senior software engineer with 11+ years of experience and current leadership of a five-engineer SaaS team. Own backend architecture, production operations, and DevOps delivery while mentoring frontend engineers on micro-frontends and API integration. Background spans telecom platforms, payment services, voice AI, and security-awareness products.',
 skills=common+[('Technical Leadership','Team leadership, backend architecture, frontend mentoring, cross-stack integration, micro-frontends, event-driven systems')],
 aspire=['lead','mentor','cdn','backend','deploy','ai','ops'], verbex=['java','pipeline','plugin','sip'], dots=['sms','pay','call']),
dict(slug='03_DevOps_Cloud', title='Senior Software Engineer | DevOps & Cloud Infrastructure',
 summary='Senior software engineer with 11+ years in production systems and current ownership of ASAT-V2 production infrastructure and DevOps operations. Manage development, test, staging, and production environments, from server setup and Terraform provisioning to GitHub Actions CI/CD, service deployment, monitoring, and incident response. Combine infrastructure ownership with hands-on backend development.',
 skills=[('Cloud & Infrastructure','AWS EC2, EKS, S3, CloudFront, ECR, Terraform, Nginx, TLS'),('Containers & Delivery','Docker, Docker Compose, Kubernetes, GitHub Actions, CI/CD, versioned rollback'),('Reliability & Performance','MongoDB replica sets, Grafana, Grafana k6, load testing, logging, alerting, incident response'),('Languages & Services','Java, Python, C, Spring Boot, FastAPI'),('Messaging & Databases','Kafka, Kafka Connect, NATS JetStream, AWS SQS, MongoDB, PostgreSQL, MySQL, Redis')],
 aspire=['devops_owner','devops_pipeline','cdn','mongo','ops','k6','lead'], verbex=['deploy','pipeline','plugin','java'], dots=['sms','call','pay']),
dict(slug='04_Distributed_Applications', title='Senior Backend Engineer | Distributed Applications & Messaging',
 summary='Senior backend engineer with 11+ years across messaging, telecom protocols, payment services, and SaaS platforms. Built an SMSC handling 3,000 TPS and Kafka data pipelines that reduced processing latency by approximately 50%. Current work includes Spring Boot architecture, cloud delivery, and leadership of a five-engineer team.',
 skills=[('Backend & Architecture','Java, Python, C, Spring Boot, FastAPI, microservices, event-driven architecture, CQRS, Axon Framework'),('Messaging & Pipelines','Apache Kafka, Kafka Connect, NATS JetStream, AWS SQS'),('Data & Availability','PostgreSQL, MySQL, MongoDB replica sets, Redis'),('Cloud & Operations','AWS, Terraform, Docker, Kubernetes, GitHub Actions, Grafana, Grafana k6'),('Telecom & Voice','SMPP, SS7, SCTP, SIP, Asterisk, LiveKit, Twilio')],
 aspire=['lead','backend','mongo','voice','deploy','k6','cdn'], verbex=['pipeline','plugin','java','sip'], dots=['sms','call','pay']),
dict(slug='05_Applied_AI_Backend', title='Senior Backend Engineer | Applied AI & Voice Platforms',
 summary='Senior backend engineer with 11+ years across telecom, cybersecurity, and voice platforms, including LLM and voice integrations. Build AI content-generation workflows with structured outputs, tool calling, and operational controls. Lead five engineers delivering a Spring Boot SaaS platform with responsibility for backend architecture and cloud delivery.',
 skills=[('AI Integration','OpenAI and Gemini APIs, structured outputs, tool calling, timeouts, retries, rate-limit handling, token-cost monitoring, caching, tracing'),('Voice & Communications','ElevenLabs, Twilio, LiveKit, SIP, Asterisk'),('Backend & Messaging','Java, Python, Spring Boot, FastAPI, Kafka, Kafka Connect, NATS JetStream, CQRS'),('Cloud & Delivery','AWS, Terraform, Docker, Kubernetes, GitHub Actions, Amazon S3, CloudFront'),('Data & Performance','PostgreSQL, MongoDB, Redis, Grafana, Grafana k6, load testing')],
 aspire=['lead','ai','aiops','voice','cdn','deploy','mentor'], verbex=['java','sip','pipeline','plugin'], dots=['call','sms','pay']),
]

styles = {
'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=22, leading=26, spaceAfter=5),
'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceAfter=7),
'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=12, spaceAfter=3),
'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceBefore=13, spaceAfter=6, keepWithNext=True),
'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10, leading=14, spaceAfter=6),
'skill': ParagraphStyle('skill', fontName='Helvetica', fontSize=9.4, leading=13, spaceAfter=3),
'job': ParagraphStyle('job', fontName='Helvetica-Bold', fontSize=10.5, leading=14, spaceAfter=3, keepWithNext=True),
'meta': ParagraphStyle('meta', fontName='Helvetica', fontSize=9.3, leading=12, spaceAfter=7, keepWithNext=True),
'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=10, leading=14, leftIndent=10, firstLineIndent=-10, spaceAfter=6),
}

def footer(canvas, doc):
    canvas.setFont('Helvetica',8)
    canvas.setFillColor(HexColor('#666666'))
    canvas.drawString(43,28,'Shubhajit Nandi')
    canvas.drawRightString(552,28,str(doc.page))

for v in versions:
    v.setdefault('github', 'github.com/shubhajit93')
    flow=[]; md=[]
    def add(text,kind='body',raw=False):
        flow.append(Paragraph(text if raw else escape(text),styles[kind]))
    def heading(text):
        add(text,'section'); md.extend(['', '## '+text, ''])
    def job(company,title,dates,location,bullets):
        add(company,'job'); add(f'{title} | {dates} | {location}','meta')
        md.extend(['### '+company,'',f'**{title}** | {dates} | {location}',''])
        for b in bullets:
            add('- '+b,'bullet'); md.append('- '+b)
        flow.append(Spacer(1,5)); md.append('')
    add('SHUBHAJIT NANDI','name'); add(v['title'],'title')
    contact='Dhaka, Bangladesh | Remote (UTC+6) | +8801779014069 | shubhajitcse59@gmail.com'
    add(contact,'contact')
    profile_line = '<link href="https://linkedin.com/in/shubhajit-nandi">linkedin.com/in/shubhajit-nandi</link>'
    if v.get('github'):
        profile_line += ' | <link href="https://' + escape(v['github']) + '">' + escape(v['github']) + '</link>'
    add(profile_line,'contact',True)
    md.extend(['# Shubhajit Nandi','',v['title'],'',contact,'','[LinkedIn](https://linkedin.com/in/shubhajit-nandi)'])
    if v.get('github'):
        md[-1] += ' | [' + v['github'] + '](https://' + v['github'] + ')'
    heading('SUMMARY'); add(v['summary']); md.append(v['summary'])
    heading('TECHNICAL SKILLS')
    for label,content in v['skills']:
        add('<b>'+escape(label)+':</b> '+escape(content),'skill',True)
        md.append(f'**{label}:** {content}  ')
    heading('PROFESSIONAL EXPERIENCE')
    job('Aspire Tech Services and Solutions Corp. (US-based client)','Senior Software Engineer','Jun 2025 - Present','Remote, Dhaka',[B[x] for x in v['aspire']])
    flow.append(PageBreak())
    job('Verbex','Senior Software Engineer','Aug 2023 - Jun 2025','Dhaka, Bangladesh',[V[x] for x in v['verbex']])
    job('Dotlines Bangladesh','Senior Software Engineer','Nov 2020 - Aug 2023','Dhaka, Bangladesh',[D[x] for x in v['dots']])
    job('SSD-TECH','Software Engineer','Feb 2015 - Nov 2020','Dhaka, Bangladesh',S)
    heading('EDUCATION')
    edu="Bachelor's in Computer Science and Engineering | 2010 - 2014"
    add(edu); add('Chittagong University of Engineering and Technology (CUET), Chittagong, Bangladesh')
    md.extend([edu,'','Chittagong University of Engineering and Technology (CUET), Chittagong, Bangladesh'])
    heading('CERTIFICATION & LANGUAGES')
    for text in ['Splunk Certified Cybersecurity Defense Analyst','Bengali: Native | English: Fluent']:
        add(text); md.append(text)
    pdf=OUT/(v['slug']+'.pdf')
    SimpleDocTemplate(str(pdf),pagesize=(595.28,841.89),rightMargin=43,leftMargin=43,topMargin=37,bottomMargin=40,title='Shubhajit Nandi - '+v['title'],author='Shubhajit Nandi').build(flow,onFirstPage=footer,onLaterPages=footer)
    (OUT/(v['slug']+'.md')).write_text('\n'.join(md)+'\n',encoding='utf-8')
    reader=PdfReader(str(pdf))
    assert len(reader.pages)==2,(v['slug'],len(reader.pages))
    text='\n'.join(p.extract_text() for p in reader.pages)
    for required in ['Aspire','Verbex','Dotlines','SSD-TECH','2015','2025','CUET']:
        assert required in text,(v['slug'],required)
    subprocess.run([r'C:\Users\Lenovo\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe','-scale-to','1100','-png',str(pdf),str(QA/v['slug'])],check=True,capture_output=True)
    print(v['slug'],len(reader.pages),'pages',len(text.split()),'words')

guide='''# Resume versions

Each role has a two-page PDF and matching editable Markdown. The PDFs use a single-column layout and selectable text. No employer ATS was used to score them.

- 01 Senior Backend Java: default for Java/Spring Boot and general senior backend openings.
- 02 Technical Lead: hands-on leadership, architecture ownership and frontend mentoring.
- 03 DevOps Cloud: deployment and infrastructure roles that value a software engineering background. Official job titles are preserved; this is not a claim of a long-standing SRE title.
- 04 Distributed Applications: Kafka, messaging, telecom and distributed application roles. Avoid presenting this as specialist consensus/storage engine expertise.
- 05 Applied AI Backend: production LLM integration and voice applications, not ML research or model training.
- 06 Senior Full Stack: backend-heavy full-stack roles emphasizing frontend architecture mentoring and API integration.
- 07 Common Senior Software Engineer: general applications, recruiter introductions, and referrals.

All versions are intended to be recruiter-readable and ATS-compatible. Tailor terminology to each actual job description without adding skills you cannot defend.

## Claims to review before sending

- The approximately 50% JavaScript loading improvement is supplied by you, not independently benchmarked here. Be ready to explain the metric and conditions.
- Existing TPS, latency and routing-cost figures are retained from your resume; distinguish production measurements from load tests when explaining them.
- AI tool calling, token-cost monitoring, caching and tracing are included from your explicit account. The earlier targeted code review did not verify all of these mechanisms.
- Versioned rollback means selecting a prior release and executing the workflow; these resumes do not claim failure-triggered automatic rollback.
- AWS/Kubernetes and Docker Compose experience are listed without asserting that every environment uses the same deployment architecture.
- The client relationship at Aspire is preserved from the source. Confirm it accurately describes your employment arrangement.
- Leadership and mentoring are based on your account; repository contents do not independently prove attribution.

Original source resume files were not overwritten.
'''
(OUT/'README.md').write_text(guide,encoding='utf-8')
