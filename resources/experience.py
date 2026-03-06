# ─────────────────────────────────────────────────────────────────────────────
# experience.py  —  the ONLY file you need to touch to manage Experience.
#
# Each dict can have:
#   company     (str)   required — company name
#   role        (str)   required — your job title
#   period      (str)   required — e.g. "Oct 2023 — July 2025"
#   highlights  (list)  optional — bullet points shown under the entry;
#                                  omit or set [] to show none
# ─────────────────────────────────────────────────────────────────────────────

EXPERIENCE = [
    {
        "company": "Seeedstack",
        "role": "Founding Engineer",
        "period": "July 2025 - Present",
        "highlights": [
            "Architected the end-to-end technical foundation of Lynk from the ground up, defining the core tech "
            "stack, system design, and service boundaries to support rapid feature scaling",
            "Engineered a cloud-native backend using Flask (Python) and PostgreSQL, with a React frontend, "
            "reducing average API response time to under 50ms and maintaining a 99.9% uptime SLA across all "
            "production endpoints",
            "Designed and implemented a CI/CD pipeline using GitHub Actions and Docker, cutting deployment time by "
            "60% and enabling daily production releases",
            "Built a real-time event-driven architecture using Kafka, decoupling 5+ core services and enabling "
            "asynchronous processing of 10,000+ events per minute",
            "Provisioned and managed cloud infrastructure on AWS (EC2, RDS, S3, CloudWatch), achieving infrastructure "
            "cost optimization of 30% through right-sizing and auto-scaling policies",
            "Designed a role-based access control (RBAC) system with JWT authentication, securing all API endpoints "
            "across 4 user permission levels",
            "Owned end-to-end observability by integrating structured logging, distributed tracing, and alerting, "
            "reducing mean time to resolve (MTTR) incidents by 50%",

        ],
    },
    {
        "company": "Cranberry.fit",
        "role": "Fullstack Engineer",
        "period": "Oct 2024 — July 2025",
        "highlights": [
            "Built Rasa chatbot with WhatsApp integration handling 50,000+ monthly interactions",
            "Designed and implemented RESTful APIs for the core platform",
            "Optimised database queries improving system performance by 40%",
        ],
    },
    {
        "company": "Temperstack",
        "role": "Fullstack Engineer",
        "period": "May 2024 — Oct 2024",
        "highlights": [
            "Integrated AWS WAF with multi-cloud monitoring systems",
            "Developed real-time threat detection and response pipelines",
            "Implemented automated security workflows reducing incident response time by 60%",
        ],
    },
]
