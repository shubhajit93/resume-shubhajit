"""Create the Carrier Platform cover letter using the verified letter layout."""
from pathlib import Path

root = Path(__file__).resolve().parent
source = (root / 'build_zalando_backend_cover_letter.py').read_text(encoding='utf-8')
setup, rest = source.split('paragraphs = [', 1)
_, renderer = rest.split('\nstyles = {', 1)
setup = setup.replace('Shubhajit_Nandi_Zalando_Software_Backend_Java_Kafka_Cover_Letter', 'Shubhajit_Nandi_Zalando_Carrier_Platform_Cover_Letter')
exec(compile(setup, 'cover_letter_setup', 'exec'))
paragraphs = [
    'Dear Zalando Hiring Team,',
    'I am applying for the Senior Software Engineer - Carrier Platform position in Berlin. The opportunity to build services that connect Zalando with carriers and support delivery, returns, and tracking appeals to me because it combines backend engineering with a clear customer outcome. My experience spans over 11 years in production software, including Java services, external payment integrations, event-driven systems, and hands-on technical leadership.',
    'At Aspire Tech Services and Solutions Corp., I lead five engineers delivering ASAT-V2, a security-awareness SaaS platform. I own backend architecture and build Spring Boot services for authentication, billing, simulations, and reporting, including Stripe and PayPal integrations. I also mentor frontend engineers on micro-frontend design and coordinate backend APIs with user-facing workflows. This work requires me to stay close to implementation while helping colleagues make consistent design decisions across the product.',
    'My responsibility extends to production infrastructure and DevOps operations. I prepare development, test, and staging environments, maintain GitHub Actions pipelines for deployment and versioned rollback, and operate services on AWS. Monitoring, logging, alerts, incident response, and Grafana k6 load testing are part of that work. I would bring this ownership to your team\'s focus on stable, high-performance services.',
    'Previously, at Verbex, I built seven Java 21 and Spring Boot services and a Kafka/Kafka Connect pipeline that reduced processing latency by approximately 50%. At Dotlines Bangladesh, I developed Java payment-gateway services integrating third-party providers on Grameenphone and Banglalink platforms. I also built a telecom messaging system handling 3,000 transactions per second while reducing per-message routing costs by 90%. These projects strengthened my ability to connect systems, investigate performance constraints, and deliver measurable improvements.',
    'I would welcome the opportunity to apply this experience to Carrier Platform, learn the delivery and returns domain, and contribute to engineering decisions alongside your senior engineers and product colleagues. Thank you for considering my application.',
    'Kind regards,',
    'Shubhajit Nandi',
]
renderer = '\nstyles = {' + renderer
renderer = renderer.replace('Application: Software Backend Engineer - Java / Kafka<br/>Zalando | ERP Engineering | Bucharest', 'Application: Senior Software Engineer - Carrier Platform<br/>Zalando | Berlin')
renderer = renderer.replace('Application: Software Backend Engineer - Java / Kafka, Zalando, Bucharest', 'Application: Senior Software Engineer - Carrier Platform, Zalando, Berlin')
renderer = renderer.replace('Shubhajit Nandi - Zalando Java / Kafka Cover Letter', 'Shubhajit Nandi - Zalando Carrier Platform Cover Letter')
renderer = renderer.replace("['Kafka Connect', '50%', 'Terraform', 'Kind regards', 'Shubhajit Nandi']", "['Carrier Platform', '50%', '3,000', 'Kind regards', 'Shubhajit Nandi']")
exec(compile(renderer, 'carrier_letter_render', 'exec'))
