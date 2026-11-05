"""Generate the tailored resume for ZEOS requisition 2724250."""
from pathlib import Path

source = (Path(__file__).parent / 'build_resume_versions.py').read_text(encoding='utf-8')
setup, remainder = source.split('for v in versions:', 1)
exec(compile(setup, 'build_resume_versions.py', 'exec'))

B['zeos_lead'] = 'Lead five engineers delivering ASAT-V2, a security-awareness SaaS platform, owning backend architecture and delivery from Spring Boot development through production operations.'
B['zeos_api'] = 'Built Spring Boot REST APIs for authentication, billing, phishing simulations, notifications, and reporting; integrated Stripe and PayPal with coupon, VAT, and discount calculations.'
B['zeos_architecture'] = 'Designed the API gateway and campaign orchestration across email, SMS, and voice simulations, integrating delivery providers and capturing participant responses for risk reporting.'
B['zeos_ops'] = 'Own production infrastructure and DevOps operations, including development, test, and staging server setup, deployment environment preparation, and service releases.'
B['zeos_ci'] = 'Maintain GitHub Actions CI/CD pipelines for Gradle builds, container deployment, and versioned rollback; the backend deployment workflow includes unit, integration, and functional test stages.'
B['zeos_monitor'] = 'Operate services on AWS with Grafana dashboards, logging, alerts, and incident response; use Grafana k6 for load testing and performance analysis.'
B['zeos_infra'] = 'Provision AWS infrastructure with Terraform and maintain Docker, Docker Compose, and Kubernetes deployment configurations; configured a three-member MongoDB replica set with automatic failover.'

versions = [dict(
    slug='09_Zalando_ZEOS_Senior_Backend_Engineer',
    title='Senior Backend Engineer | Java, Spring Boot, AWS',
    summary='Senior software engineer with 11+ years building production systems across SaaS, payments, and telecom. Lead five engineers delivering a Spring Boot platform, owning backend architecture, cloud deployment, and production operations. Experience includes Java 21 services, REST APIs, Kafka pipelines with approximately 50% lower processing latency, and close collaboration with frontend engineers to deliver complete features.',
    skills=[
        ('Java & APIs', 'Java (including Java 21), Spring Boot, Spring Cloud, Hibernate, REST API design, API gateways, Gradle, Jackson'),
        ('Architecture & Messaging', 'Microservices, distributed applications, event-driven architecture, Apache Kafka, Kafka Connect, CQRS, Axon Framework, NATS JetStream'),
        ('Cloud & Delivery', 'AWS, Kubernetes, Docker, Docker Compose, Terraform, GitHub Actions, CI/CD'),
        ('Data', 'PostgreSQL, MySQL, MongoDB replica sets, Redis'),
        ('Performance & Operations', 'Grafana k6, load testing, Grafana, logging, alerting, incident response'),
        ('Collaboration', 'Team leadership, backend architecture, frontend mentoring, micro-frontends, API integration'),
    ],
    aspire=['zeos_lead', 'zeos_api', 'zeos_architecture', 'zeos_ops', 'zeos_ci', 'zeos_monitor', 'zeos_infra', 'mentor', 'cdn'],
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
render = render.replace("pdf=OUT/(v['slug']+'.pdf')", """pdf=OUT/(v['slug']+'.pdf')
    if pdf.exists():
        try:
            with pdf.open('r+b'):
                pass
        except PermissionError:
            pdf=OUT/(v['slug']+'_Updated.pdf')""")
exec(compile(render, 'zeos_resume_render', 'exec'))
