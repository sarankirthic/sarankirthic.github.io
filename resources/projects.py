# ─────────────────────────────────────────────────────────────────────────────
# projects.py  —  the ONLY file you need to touch to manage Featured Projects.
#
# Each dict in PROJECTS can have:
#   title        (str)  required — displayed project name
#   description  (str)  required — one-liner shown in the card header
#   problem      (str)  required — problem statement explained in 50 words or more
#   idea         (str)  required — the idea generated for the problem statement
#   solution     (str)  required — the solution implemented based on the idea
#   github       (str)  optional — full GitHub URL; omit or set "" to hide icon
#   tech         (list) required — list of tech-badge strings; can be empty []
# ─────────────────────────────────────────────────────────────────────────────

PROJECTS = [
    {
        "title": "Data Analytics Platform",
        "description": "End-to-end data pipeline with real-time analytics and visualization",
        "problem": "Organizations generate massive volumes of data from multiple sources, but lack a unified "
                   "system to ingest, process, and visualize it in real time. This leads to delayed "
                   "decision-making, fragmented insights, and inefficient manual reporting pipelines that "
                   "fail to scale with growing data demands.",
        "idea": "Build an end-to-end data platform that automates the flow of raw data from ingestion through "
                "transformation to real-time visualization, eliminating manual bottlenecks and giving stakeholders "
                "live, actionable insights.",
        "solution": "A fully integrated data pipeline that ingests data from multiple sources, processes and transforms"
                    " it in real time using event-driven architecture, and delivers interactive dashboards and "
                    "visualizations — enabling faster, data-driven decisions at scale.",
        "github": "https://github.com/sarankirthic/data-analytics",
        "tech": ["Python", "Apache Spark", "PostgreSQL", "Docker", "AWS"],
    },
    {
        "title": "E-Commerce Platform",
        "description": "Full-stack e-commerce solution with secure payment integration",
        "problem": "Small and mid-sized businesses struggle to establish a reliable online retail presence due to the "
                   "complexity of building secure, scalable storefronts. Existing solutions are either too costly, "
                   "heavily restricted, or lack robust payment security — making it difficult to serve customers "
                   "safely and efficiently.",
        "idea": "Develop a full-stack e-commerce platform that handles the complete shopping experience — from "
                "product browsing and cart management to checkout — with secure, end-to-end payment integration built "
                "in from the ground up.",
        "solution": "A scalable web application featuring product listings, user authentication, order management, "
                    "and seamlessly integrated secure payment gateways — giving businesses a reliable, "
                    "ready-to-deploy online store that ensures safe transactions and a smooth customer experience.",
        "github": "https://github.com/sarankirthic/ecommerce",
        "tech": ["Spring Boot", "React", "MySQL", "Redis", "Stripe API"],
    },
    {
        "title": "Learning Management System",
        "description": "Comprehensive LMS with role-based access and progress tracking",
        "problem": "Educational institutions and organizations struggle to manage course delivery, track learner "
                   "progress, and control access across different user roles — instructors, students, and admins — in "
                   "one place. Fragmented tools and manual tracking lead to poor learning outcomes and administrative "
                   "overhead.",
        "idea": "Build a centralized LMS that unifies course management, learner progress tracking, and role-based "
                "access control under a single platform — giving every stakeholder a tailored, permission-appropriate "
                "experience.",
        "solution": "A comprehensive web-based platform where admins manage users, instructors create and deliver "
                    "course content, and students track their own learning progress — all enforced through granular "
                    "role-based access control, ensuring a structured, secure, and measurable learning environment.",
        "github": "https://github.com/sarankirthic/lms",
        "tech": ["Java", "Spring Boot", "Thymeleaf", "MySQL", "Spring Security"],
    },
    {
        "title": "Paisley — News Recognition & Automation",
        "description": "AI-powered pattern analysis and recommendation engine",
        "problem": "The modern news landscape is overwhelmed with content from countless sources, making it nearly "
                   "impossible for users to filter relevant information, detect patterns across stories, or receive "
                   "personalized recommendations without spending hours manually sifting through feeds — leading to "
                   "information overload and missed insights.",
        "idea": "Leverage AI to automatically analyze incoming news content, recognize patterns, topics, and trends "
                "across sources, and deliver intelligent, personalized recommendations — turning raw news volume into "
                "a curated, meaningful experience for each user.",
        "solution": "An AI-powered engine that continuously ingests news data, applies pattern recognition to "
                    "identify recurring themes and emerging trends, and serves tailored content recommendations — "
                    "automating the discovery process and ensuring users always receive the most relevant, "
                    "timely news with minimal effort.",
        "github": "https://github.com/sarankirthic/Paisley",
        "tech": ["Python", "TensorFlow", "Flask", "MongoDB"],
    },
    {
        "title": "Kafka Routing Orchestrator",
        "description": "Intelligent message routing and orchestration for distributed architectures",
        "problem": "In large-scale distributed systems, messages flowing between microservices often require complex "
                   "routing logic based on content, priority, or destination. Hardcoded routing rules create brittle, "
                   "unmaintainable pipelines that struggle to adapt to changing architectures — leading to message "
                   "bottlenecks, misrouting, and cascading failures across services.",
        "idea": "Build an intelligent orchestration layer on top of Kafka that dynamically evaluates incoming "
                "messages and routes them to the correct topics, consumers, or services — decoupling routing logic "
                "from individual microservices and centralizing control.",
        "solution": "A Kafka-based routing orchestrator that applies configurable, rule-driven logic to intelligently "
                    "direct messages across distributed services in real time — improving pipeline reliability, "
                    "reducing inter-service coupling, and enabling seamless scaling and reconfiguration without "
                    "redeploying individual components.",
        "github": "https://github.com/sarankirthic/kafka-routing-orchestrato",
        "tech": ["Apache Kafka", "Java", "Spring Boot", "Docker", "Kubernetes"],
    },
    {
        "title": "Twitter Clone — Social Media Platform",
        "description": "Scalable social networking platform with real-time features",
        "problem": "Building a social networking platform that handles real-time interactions — posts, likes, "
                   "follows, and live feeds — at scale is a significant engineering challenge. Most prototype social "
                   "apps fail under concurrent user load, lack real-time responsiveness, or cannot efficiently "
                   "deliver personalized feeds as the user base grows.",
        "idea": "Design and develop a scalable social media platform inspired by Twitter's core mechanics, "
                "prioritizing real-time content delivery, user interaction, and a distributed architecture capable of "
                "handling high concurrency without performance degradation.",
        "solution": "A full-stack social networking application supporting user posts, follows, likes, and live feed "
                    "updates — built on a scalable backend with real-time WebSocket-driven interactions, "
                    "efficient data modeling for feed generation, and an architecture designed to handle growing user "
                    "demand reliably.",
        "github": "https://github.com/sarankirthic/twitter",
        "tech": ["React", "Node.js", "MongoDB", "WebSocket", "Redis"],
    },
]
