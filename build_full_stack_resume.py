"""Build only the full-stack variant using the existing resume renderer."""
from pathlib import Path

source = (Path(__file__).parent / 'build_resume_versions.py').read_text(encoding='utf-8')
setup, remainder = source.split('for v in versions:', 1)
exec(compile(setup, 'build_resume_versions.py', 'exec'))

B['fullstack_lead'] = 'Lead five engineers delivering ASAT-V2, a security-awareness SaaS platform, owning Spring Boot backend services, frontend integration, and production delivery.'
B['fullstack_mentor'] = 'Mentored frontend engineers on React and TypeScript micro-frontends, aligning API integration and UI workflows across phishing, billing, and training modules.'
B['fullstack_backend'] = 'Built backend APIs for authentication, billing, phishing simulations, notifications, and reporting; integrated Stripe and PayPal payments with coupon, VAT, and discount calculations.'
B['fullstack_ai'] = 'Enabled customer-specific phishing email and landing-page generation through LLM integrations with structured outputs, tool calling, timeouts, retries, and rate-limit handling.'
B['fullstack_deploy'] = 'Built GitHub Actions workflows for frontend asset publishing and backend container deployment, with versioned rollback; manage deployment environments from server setup through releases.'
B['fullstack_perf'] = 'Used Grafana k6 to benchmark backend performance under load; maintain production dashboards, logging, alerts, and incident response.'

versions = [dict(
    slug='06_Senior_Full_Stack',
    github='github.com/shubhajit93',
    title='Senior Full Stack Engineer | Java, Spring Boot & React Integration',
    summary='Senior software engineer with 11+ years of experience across telecom, cybersecurity, and voice AI. Lead a five-engineer SaaS team, combining hands-on backend development with frontend architecture mentoring, API integration, and cloud delivery. Reduced JavaScript asset loading time by approximately 50% through Amazon S3 and CloudFront.',
    skills=[
        ('Backend & APIs', 'Java, Spring Boot, Spring Cloud, Hibernate, REST APIs, Python, FastAPI'),
        ('Frontend Architecture & Integration', 'React, TypeScript, JavaScript, Vite, module federation, micro-frontends'),
        ('Databases & Messaging', 'PostgreSQL, MySQL, MongoDB, Redis, Kafka, Kafka Connect, NATS JetStream'),
        ('Cloud & Delivery', 'AWS, Amazon S3, CloudFront, Terraform, Docker, Docker Compose, Kubernetes, GitHub Actions'),
        ('Performance & Integrations', 'Grafana k6, Grafana, load testing, Stripe, PayPal, OpenAI and Gemini APIs'),
    ],
    aspire=['fullstack_lead', 'cdn', 'fullstack_mentor', 'fullstack_backend', 'fullstack_ai', 'fullstack_deploy', 'fullstack_perf'],
    verbex=['java', 'pipeline', 'plugin', 'deploy'],
    dots=['pay', 'sms', 'call'],
)]

# Use the available page space for more readable text, not additional claims.
for key in ['body', 'bullet']:
    styles[key].fontSize = 10.5
    styles[key].leading = 15.5
    styles[key].spaceAfter = 8
styles['skill'].fontSize = 9.7
styles['skill'].leading = 13.8
styles['job'].spaceBefore = 5
styles['meta'].spaceAfter = 9
exec(compile('for v in versions:' + remainder.split("\nguide='''", 1)[0], 'full_stack_render', 'exec'))
