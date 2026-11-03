"""Build the Flyte Solutions Java/Spring Boot application resume only."""
from pathlib import Path

source = (Path(__file__).parent / 'build_resume_versions.py').read_text(encoding='utf-8')
setup, remainder = source.split('for v in versions:', 1)
exec(compile(setup, 'build_resume_versions.py', 'exec'))

B['flyte_lead'] = 'Lead five engineers delivering ASAT-V2, a security-awareness SaaS platform, with ownership of backend architecture, Spring Boot services, and production delivery.'
B['flyte_backend'] = 'Built Spring Boot services for authentication, billing, phishing simulations, notifications, and reporting; integrated Stripe and PayPal with coupon, VAT, and discount calculations.'
B['flyte_deploy'] = 'Own production infrastructure and DevOps operations, including development, test, and staging server setup, environment preparation, and GitHub Actions CI/CD pipelines for service deployment and versioned rollback.'
B['flyte_ops'] = 'Operate production services on AWS, maintaining Nginx/TLS, Grafana dashboards, logging, alerts, and incident response; use Grafana k6 for load testing and performance analysis.'

versions = [dict(
    slug='08_Flyte_Senior_Java_Spring_Boot',
    title='Senior Java / Spring Boot Engineer',
    summary='Senior software engineer with 11+ years building production systems across telecom, cybersecurity, and voice AI, including Java payment integrations and Spring Boot microservices. Lead a five-engineer team and own backend architecture and production operations. Experience includes payment-provider integrations, Kafka pipelines with approximately 50% lower processing latency, and telecom messaging systems handling 3,000 TPS.',
    skills=[
        ('Java & Backend', 'Java (including Java 21), Spring Boot, Spring Cloud, Hibernate, REST APIs, Python, C'),
        ('Architecture & Messaging', 'Microservices, event-driven architecture, Apache Kafka, Kafka Connect, NATS JetStream, CQRS, Axon Framework'),
        ('Databases', 'SQL, PostgreSQL, MySQL, MongoDB replica sets, Redis'),
        ('Cloud & CI/CD', 'AWS, Docker, Docker Compose, Kubernetes, Terraform, GitHub Actions, Git, Nginx, TLS'),
        ('Performance & Operations', 'Grafana k6, load testing, Grafana, logging, alerting, production incident response'),
        ('Integration & Leadership', 'Payment gateways, Stripe, PayPal, third-party APIs, backend architecture, team leadership, frontend mentoring'),
    ],
    aspire=['flyte_lead', 'flyte_backend', 'flyte_deploy', 'flyte_ops', 'mongo', 'mentor', 'cdn'],
    verbex=['java', 'pipeline', 'plugin', 'deploy'],
    dots=['pay', 'sms', 'call'],
)]

for key in ['body', 'bullet']:
    styles[key].fontSize = 10.4
    styles[key].leading = 14.7
    styles[key].spaceAfter = 7
styles['skill'].fontSize = 9.5
styles['skill'].leading = 13
styles['job'].spaceBefore = 4
styles['meta'].spaceAfter = 8

render = 'for v in versions:' + remainder.split("\nguide='''", 1)[0]
render = render.replace('Dhaka, Bangladesh | Remote (UTC+6) |', 'Dhaka, Bangladesh |')
exec(compile(render, 'flyte_resume_render', 'exec'))
