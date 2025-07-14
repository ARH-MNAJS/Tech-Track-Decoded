import json

def evaluate_skills(skills: dict):
    user_total = sum(skills.values())
    max_total = len(skills) * 10
    user_score = round(user_total / max_total * 100)

    strengths = [k for k, v in skills.items() if v >= 7]
    low_skills = sorted(skills.items(), key=lambda x: x[1])[:3]
    weak_areas = [k for k, _ in low_skills]

    roadmap = get_roadmap(weak_areas)
    return user_score, strengths, roadmap



def get_roadmap(skills):
    try:
        with open("roadmap_templates.json", "r") as f:
            templates = json.load(f)
        return "\n\n".join([f"### {s}\n{templates.get(s, 'Coming Soon...')}" for s in skills])
    except:
        return "No roadmap templates found."
