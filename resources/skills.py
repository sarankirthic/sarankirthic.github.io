# ─────────────────────────────────────────────────────────────────────────────
# skills.py  —  the ONLY file you need to touch to manage the Skills carousel.
#
# Each dict has one key:
#   icon  (str)  required — the skill-icons identifier passed to render_icon().
#                           Format: "skill-icons:<name>"
#                           Browse all icons at https://skillicons.dev
#
# To add a skill:    append a new dict.
# To remove a skill: delete its dict.
# To reorder:        move dicts up/down — carousel reflects the order exactly.
# The template duplicates the list automatically for the seamless scroll loop.
# ─────────────────────────────────────────────────────────────────────────────

SKILLS = [
    # ── Languages ──
    {"icon": "skill-icons:python-light"},
    {"icon": "skill-icons:java-light"},
    {"icon": "skill-icons:javascript"},

    # ── Frameworks ──
    {"icon": "skill-icons:flask-light"},
    {"icon": "skill-icons:spring-light"},
    {"icon": "skill-icons:django"},
    {"icon": "skill-icons:react-light"},
    {"icon": "skill-icons:nodejs-light"},
    {"icon": "skill-icons:expressjs-light"},

    # ── Cloud ──
    {"icon": "skill-icons:aws-light"},
    {"icon": "skill-icons:gcp-light"},
    {"icon": "skill-icons:azure-light"},

    # ── Databases ──
    {"icon": "skill-icons:postgresql-light"},
    {"icon": "skill-icons:mongodb"},
    {"icon": "skill-icons:redis-light"},

    # ── DevOps / Infra ──
    {"icon": "skill-icons:docker"},
    {"icon": "skill-icons:kubernetes"},
    {"icon": "skill-icons:kafka"},
    {"icon": "skill-icons:nginx"},
    {"icon": "skill-icons:git"},
    {"icon": "skill-icons:github-light"},

    # ── ML / Data ──
    {"icon": "skill-icons:tensorflow-light"},
    {"icon": "skill-icons:pytorch-light"},

    # ── Web ──
    {"icon": "skill-icons:html"},
    {"icon": "skill-icons:css"},
    {"icon": "skill-icons:npm-light"},

    # ── OS / Tools ──
    {"icon": "skill-icons:linux-light"},
]
