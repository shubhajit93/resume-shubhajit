"""Generate the general-purpose senior engineering resume only."""
from pathlib import Path

source = (Path(__file__).parent / 'build_resume_versions.py').read_text(encoding='utf-8')
setup, remainder = source.split('for v in versions:', 1)
exec(compile(setup, 'build_resume_versions.py', 'exec'))

B['common_lead'] = 'Lead five engineers delivering ASAT-V2, a security-awareness SaaS platform, owning backend architecture, AWS infrastructure, and production delivery.'
B['common_backend'] = 'Built Spring Boot services for authentication, phishing simulations, billing, notifications, and reporting; integrated Stripe and PayPal with coupon, VAT, and discount calculations.'
B['common_deploy'] = 'Provisioned AWS infrastructure with Terraform and automated container builds, deployment, and versioned rollback through GitHub Actions; prepare servers for new deployment environments.'
B['common_ai'] = 'Integrated OpenAI and Gemini for customer-specific simulation content, implementing structured outputs, tool calling, timeouts, retries, and rate-limit handling.'
B['common_mentor'] = 'Mentored frontend engineers on micro-frontend design and implementation, aligning backend APIs and UI workflows across phishing, billing, and training modules.'
B['common_ops'] = 'Use Grafana k6 for load testing and performance analysis; maintain Grafana dashboards, logging, alerts, and production incident response.'

versions = [dict(
    slug='07_Common_Senior_Software_Engineer',
    github='github.com/shubhajit93',
    title='Senior Software Engineer | Backend Systems & Cloud Delivery',
    summary='Senior software engineer with 11+ years building production systems across telecom, cybersecurity, and voice AI. Lead a five-engineer SaaS team with ownership of backend architecture and cloud delivery. Built a messaging platform handling 3,000 TPS with 90% lower per-message routing costs. Combine Java/Spring Boot development with frontend mentoring, AI integration, and production operations.',
    skills=[
        ('Languages & Backend', 'Java, Python, C, JavaScript, Spring Boot, Spring Cloud, Hibernate, FastAPI, REST APIs'),
        ('Messaging & Architecture', 'Apache Kafka, Kafka Connect, NATS JetStream, AWS SQS, microservices, event-driven systems, CQRS, Axon Framework'),
        ('Databases', 'PostgreSQL, MySQL, MongoDB replica sets, Redis'),
        ('Cloud & DevOps', 'AWS, Terraform, Docker, Docker Compose, Kubernetes, GitHub Actions, CI/CD, Amazon S3, CloudFront, Nginx'),
        ('Performance & Operations', 'Grafana k6, load testing, Grafana, logging, tracing, alerting, incident response'),
        ('AI & Cross-Stack Integration', 'OpenAI and Gemini APIs, structured outputs, tool calling, micro-frontends, frontend mentoring'),
    ],
    aspire=['common_lead', 'cdn', 'common_backend', 'common_deploy', 'common_ai', 'common_mentor', 'mongo', 'common_ops'],
    verbex=['pipeline', 'plugin', 'java', 'sip', 'deploy'],
    dots=['sms', 'pay', 'call'],
)]

for key in ['body', 'bullet']:
    styles[key].fontSize = 10.4
    styles[key].leading = 14.7
    styles[key].spaceAfter = 7
styles['skill'].fontSize = 9.5
styles['skill'].leading = 13
styles['job'].spaceBefore = 4
styles['meta'].spaceAfter = 8
exec(compile('for v in versions:' + remainder.split("\nguide='''", 1)[0], 'common_resume_render', 'exec'))
