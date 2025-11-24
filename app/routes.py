from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import ContactForm
from flask_mail import Message
from app import mail

main = Blueprint('main', __name__)

PROJECTS = [
    {
        "id": "financial-llm",
        "title": "Financial Advice LLM Integration",
        "image": "img/financial_llm.png",
        "link" : "https://flask-loan-advisor-1.onrender.com",
        "short": "AI-driven loan recommendation engine (Flask + LLMs).",
        "details": "Integrated a large language model into a banking web app to recommend loan amounts, explain decisions and provide financial guidance. Built with Flask and SQLAlchemy; includes inference and simple explainability features."
    },
    {
        "id": "medical-models",
        "title": "Predictind servierness of lumbar deseases",
        "image": "img/lumbar.png",
        "link" : "https://www.kaggle.com/code/wangapa106g/fork-of-lumbar-desease-diag",
        "short": "Developed a CNN model to predict the extent of a lumbard degenerative spine deseases.",
        "details": "this was on a competition posted on kaggle the ,used tranfer learning,with Efficient Net where the model showed good performance on prediction"
    },
    {
        "id": "inteructive web ML game developement",
        "title": "Accident risk predictor game on web interface",
        "image": "img/accident_risk.png",
        "link" : "https://accident-risk-predictor.onrender.com/game_page",
        "short": "this was on stack overflow competition ",
        "details": "intergrated a ML catboost model into a web application where users can interuct with the model on a gaming interface"
    },
    {
        "id": "mecor-ai",
        "title": "Mecor AI Competition - NLP Classifier",
        "image": "img/mecor.png",
        "link" : "https://www.kaggle.com/code/wangapa106g/roberta-model",
        "short": "High-performance NLP model for authentic vs inauthentic text (0.9935 AUC).",
        "details": "Built an NLP classification pipeline with modern tokenization and ensembling. Optimized for ROC-AUC, deployed evaluation pipelines, and tuned for generalization using cross-validation."
    },
    {
        "id": "green ai",
        "title": "LLM-powered chemical usage advice to farmers",
        "image": "img/agri_smart.png",
        "link" : "https://farmer360.onrender.com/",
        "short": "agri-chemical usage advisor for farmers providing multilingual advice",
        "details": "used gemini model to develope a chemical usage intructor and advisor for famers just by image uploading"
    }
]

@main.route('/')
def index():
    intro = {
        'name': 'Peter Wanga Otieno',
        'title': 'Python Developer & ML Engineer',
        'location': 'Kerugoya, Kirinyaga County, Kenya',
        'summary': 'Python Developer with real-world experience building and deploying AI/ML solutions. Skilled in Python, Flask, SQL, data pipelines and model deployment.'
    }
    return render_template('index.html', intro=intro, projects=PROJECTS)

@main.route('/about')
def about():
    experience = [
        {
            "role": "Technical AI & ML Lead — Kirinyaga University Computer Society",
            "dates": "Sep 2025 – Present",
            "details": [
                "Lead technical ML sessions and mentor student developers.",
                "Coordinate model experimentation, fine-tuning and cloud deployment projects."
            ]
        },
        {
            "role": "Software Engineer (Intern) — Bumala Financial Services Association",
            "dates": "Apr 2024 – Present",
            "details": [
                "Developed and deployed LLM-powered loan recommendation module (Python + Flask).",
                "Evaluated customer credit risk and improved backend reliability."
            ]
        },
        {
            "role": "Junior ML Engineer / Data Analyst — Raha Premium Flour Milling Company",
            "dates": "Jan 2024 – Jan 2025",
            "details": [
                "Built ML model to predict production output and improved planning.",
                "Worked with Kubernetes/GCP for containerization and scalable inference."
            ]
        }
    ]

    skills = [
        "Python (Strong)", "Flask", "scikit-learn", "TensorFlow", "PyTorch", "Hugging Face",
        "Docker", "Kubernetes", "GCP (BigQuery)", "SQL", "Git/GitHub", "LLMs, ML pipelines"
    ]

    education = "Kirinyaga University of Science and Technology (Undergraduate)"

    contacts = {
        "github": "https://github.com/Wangadeveloper",
        "kaggle": "https://www.kaggle.com/wangapa106g",
        "linkedin": "https://www.linkedin.com/in/peter-wanga-822208322/",
        "cv_pdf": url_for('static', filename='docs/PETER_WANGA_OTIENO.pdf')
    }

    return render_template('about.html', experience=experience, skills=skills, education=education, contacts=contacts)

@main.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)

@main.route('/project/<proj_id>')
def project_details(proj_id):
    proj = next((p for p in PROJECTS if p['id'] == proj_id), None)
    if not proj:
        return render_template('project_not_found.html', proj_id=proj_id), 404
    return render_template('project_details.html', project=proj)


@main.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
#         # Build email
#         msg = Message(
#             subject=f"New Portfolio Message from {form.name.data}",
#             recipients=["your_email@gmail.com"],  # where you receive messages
#             body=f"""
# You received a new message from your portfolio website:

# Name: {form.name.data}
# Email: {form.email.data}

# Message:
# {form.message.data}
# """
#         )

#         # Send the email
#         mail.send(msg)

        flash(f"Thank you, {form.name.data}! Your message has been sent.", "success")
        return redirect(url_for("main.contact"))

    return render_template("contact.html", form=form)

