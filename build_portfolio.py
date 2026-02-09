import webbrowser
import os
from jinja2 import Template

# ==========================================
#  SECTION 1: YOUR DATA
# ==========================================
profile_data = {
    "personal_info": {
        "name": "Ifeoma Precious Ogwu",
        "title": "Electrical & Computer Engineering Graduate",
        "location": "US Citizen",
        "bio": "Driven and passionate electrical & computer engineer. Recent graduate from The University Of Tulsa with Cum Laude honors. Particularly interested in power systems, energy, electronics (analog and digital). Open to opportunities including internships, contract work, full-time positions in hardware design and development, embedded systems, PCB design, Power Systems, R&D, electrical engineering and computer engineering.",
        "linkedin": "https://www.linkedin.com/in/ifeoma-ogwu/",
        "github": "https://github.com/Ifeoma16",
        "email": "ifeomalockwood@gmail.com",
        "resume_link": "assets/master_resume_Ogwu.pdf" 
    },
    "skills": {
        "Hardware": ["PCB Design", "Arduino", "STM32", "Raspberry Pi", "Embedded Systems", "R&D"],
        "Programming": ["Python", "C", "Verilog", "MIPS", "RISC-V"],
        "Software": ["MATLAB", "Simulink", "Firmware", "SolidWorks", "KiCAD", "Microsoft Office", "CymeTCC", "CYMEDist", "PowerBI", "SharePoint", "Power Automate"],
        "Equipment": ["Oscilloscope", "Multimeter", "Function Generator", "3D Printer", "Circuit Elements", "Soldering"]
    },
    "projects": [
        {
            "title": "Reverse Engineering PCBs [In Progress]",
            "tag": "AI",
            "description": "Fine-tuned a YOLOv8 object detection model with a custom dataset of PCB images, divided into 6 main classifications. This project is sill in progress.",
            "image": "assets/yolo_fine_tuning_results.png", 
            "video": "assets/video_demo_senior_design.mp4", 
            "tech": ["Roboflow", "Google Colab", "Neural Network"],
            "link": "https://www.linkedin.com/posts/ifeoma-ogwu_this-past-semester-i-did-another-senior-activity-7407789348772909056-KVSS?utm_source=share&utm_medium=member_desktop&rcm=ACoAADMD_n8Bf8OKs7h1ObbI2UMxcHzIJcsLgXw"
        },
        {
            "title": "Ambient Light Energy Harvesting For Microcontroller",
            "tag": "Energy & Power",
            "description": "Prototyping work of harvesting ambient energy from indoor lighting for a low-power Arduino data logger. A PCB design was also made for a custom solution for trickle charging the battery from the solar cells while it powers the load.",
            "image": "assets/energy_harvesting_setup.png",
            "link": "https://www.linkedin.com/posts/ifeoma-ogwu_energharvesting-embedded-iot-activity-7375253090427531264-PY2g?utm_source=share&utm_medium=member_desktop&rcm=ACoAADMD_n8Bf8OKs7h1ObbI2UMxcHzIJcsLgXw",
            "tech": ["Energy Harvesting", "Solar Cells", "Arduino", "AEM10941 Harvester", "KiCAD", "Sensors & Peripherals"]
        },
        {
            "title": "Simulation Of RF Energy Harvesting",
            "tag": "Energy & Power",
            "description": "A simulation of a typical quarter-wave monopole antenna with centre frequency of 189 MHz and bandwidth of 6MHz. An impedance matching circuit was designed and the load simulated was 100Ω",
            "image": "assets/rf_matching_circuit.png",
            "link": "https://www.linkedin.com/posts/ifeoma-ogwu_engineering-energyharvesting-wirelesspowertransfer-activity-7401258839725092864-Rosj?utm_source=share&utm_medium=member_desktop&rcm=ACoAADMD_n8Bf8OKs7h1ObbI2UMxcHzIJcsLgXw",
            "tech": ["Simulink", "Radio Frequency", "Energy Harvesting", "Impedance Matching"]
        },
        {
            "title": "Simulation Of Solar Energy Harvesting",
            "tag": "Energy & Power",
            "description": "A simulation of LL200-2.4-75 PowerFilm solar cells and a capacitor to store charge. A 5kΩ resistor was added to reduce voltage to load and the load simulated was a 2.2V, 20mA LED.",
            "image": "assets/solar_energy_harvesting.png",
            "link": "https://www.linkedin.com/posts/ifeoma-ogwu_engineering-energyharvesting-wirelesspowertransfer-activity-7401258839725092864-Rosj?utm_source=share&utm_medium=member_desktop&rcm=ACoAADMD_n8Bf8OKs7h1ObbI2UMxcHzIJcsLgXw",
            "tech": ["Simulink", "Energy Harvesting", "Solar Energy"]
        },
        {
            "title": "Portable Gaming System",
            "tag": "Embedded Systems",
            "description": "A portable gaming system done as a group project. Main microcontroller was an STM32 and my sub-team was in charge of a piano tiles-esque game shwon in video. Project in LinkedIn project section.",
            "video-embed": "https://youtube.com/embed/2PcFNbeu9rk",
            "link": "https://www.linkedin.com/in/ifeoma-ogwu/",
            "tech": ["STM32", "STM32CubeIDE", "Kalman Filtering", "Embedded Systems", "Displays", "MPU6050"]
        },
        {
            "title": "AM Modulation / Demodulation System",
            "tag": "Communications",
            "description": "A simulation of a simple Amplitude Modulation (AM) modulation / demodulation system in Simulink. The system is set up to pass frequencies up to 3.5 kHz and stop frequencies after 5 kHz, so only my voice goes through.",
            "video": "assets/am_system_demo.mp4",
            "link": "https://www.linkedin.com/posts/ifeoma-ogwu_engineering-communicationsystems-electricalengineering-activity-7404165468397174784-nxgj",
            "tech": ["Simulink", "Communication Systems", "Amplitude Modulation"]
        }
    ],
    "experience": [
        {
            "company": "American Electric Power",
            "role": "Distribution Engineer Intern",
            "duration": "June 2025 - December 2025",
            "details": [
                "Worked in the distribution reliability group and supported CVR and DACR efforts",
                "Configured base cases for 400+ feeders in CYMDIST and exported datasets to SQL supporting Perfect Power initiatives",
                "Conducted load allocation, ampacity studies, new load studies and short circuit studies to inform protection planning",
                "Assisted commissioning of IntelliRupter reclosers and the configuring of protection settings and resetting modules, reducing outage resolution time in the field",
                "Performed coordination analyses in CYMETCC to optimize feeder performance and inform reliability improvements",
                "Created dashboards using PI Vision for displaying feeders, their devices and various status points for YFA and CVR efforts",
                "Conducted Arc Flash studies in CYMDIST per customer requests to gain analysis results on specified nodes"
            ]
        },
        {
            "company": "SageNet",
            "role": "Business Analyst Intern",
            "duration": "May 2024 - August 2024",
            "details": [
                "Published 100s of SharePoint subsites used as runbooks for the purpose of a document repository project",
                "Decreased the gap between operational cost and net profit by 4% through new documentation system",
                "Created Python scripts to automate data migration from old database to Microsoft SharePoint",
                "Implemented Power Automate to automate workflow actions for the runbooks made in SharePoint",
                "Analyzed cybersecurity reports for data validation and segmentation purposes",
                "Utilized Power BI to create report dashboards for operational organization and data analysis",
                "Optimized Raspberry Pi boot sequence to load into browser in under 15 seconds"
            ]
        },
        {
            "company": "The University Of Tulsa",
            "role": "Apprentice 3D Print Technician",
            "duration": "August 2024 - December 2025",
            "details": [
                "Operating and maintaining 3D printers (Bambu, Creality, UltiMaker) to produce high-quality prints for student and faculty projects",
                "Utilizing SolidWorks for designing parts and components, ensuring compatibility with 3D printing specifications",
                "Slicing and preparing models for printing using Bambu Studio and Creality software, optimizing print settings for efficiency and quality",
                "Assembling and post-processing printed components, ensuring proper fit and finish for final use",
                "Provide technical support to students and faculty, assisting with design modifications and print troubleshooting"
            ]
        },
        {
            "company": "The University Of Tulsa",
            "role": "Robotics Researcher",
            "duration": "May 2024 - August 2024",
            "details": [
                "Designed PCB schematics and models for a controller to integrate with the Boston Dynamics’ mobile robot: Spot",
                "Utilized KiCAD to create detailed schematics and multi-layer PCB layouts",
                "Researched and tested best components to use for the controller and best ways for production using Raspberry Pi",
                "Collaborated with a multidisciplinary team to ensure seamless integration with Spot's existing systems"
            ]
        },
        {
            "company": "Access Optics",
            "role": "Manufacturing Engineer Intern",
            "duration": "May 2023 - July 2023",
            "details": [
                "Worked under Atento Capital for one of their portfolio companies, Access Optics, as a manufacturing engineering intern",
                "Built documentation libraries to support project-specific and continuous use to improve operational efficiency",
                "Created project reports, assembly processes and work instructions documentation",
                "Performed research for pricing and purchasing benefit",
                "Interpreted technical drawings and manufacturer specifications to support experienced engineers",
                "Refined engineering designs to incorporate new information and specifications"
            ]
        },
    ]
}

# ==========================================
#  SECTION 2: UPDATED TEMPLATE
# ==========================================
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.personal_info.name }} | Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #ffffff;
            --text: #1a1a1a;
            --accent: #2563eb;
            --card-bg: #f8fafc;
            --border: #e2e8f0;
        }
        [data-theme="dark"] {
            --bg: #0f172a;
            --text: #f8fafc;
            --accent: #3b82f6;
            --card-bg: #1e293b;
            --border: #334155;
        }

        * { transition: all 0.25s ease; box-sizing: border-box; }
        body { 
            margin: 0; 
            font-family: 'Inter', sans-serif; 
            background-color: var(--bg); 
            color: var(--text);
            line-height: 1.6;
        }

        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--card-bg);
            border: 1px solid var(--border);
            padding: 10px;
            border-radius: 50%;
            cursor: pointer;
            z-index: 1000;
        }

        .container { max-width: 900px; margin: 0 auto; padding: 0 20px; }

        header { padding: 100px 0 60px 0; }
        h1 { font-size: 3.5rem; margin: 0; font-weight: 800; letter-spacing: -2px; }
        .subtitle { font-size: 1.2rem; color: var(--accent); font-weight: 600; }
        
        section { padding: 60px 0; border-bottom: 1px solid var(--border); }
        h2 { font-size: 1.8rem; margin-bottom: 30px; }

        .skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
        .skill-list span { 
            display: inline-block; 
            background: var(--card-bg); 
            padding: 5px 12px; 
            margin: 4px; 
            border-radius: 6px; 
            border: 1px solid var(--border);
            font-size: 0.85rem;
        }

        .project-card { 
            margin-bottom: 60px; 
            display: grid; 
            grid-template-columns: 1fr 1fr; 
            gap: 40px; 
            align-items: start;
        }
        @media (max-width: 768px) { .project-card { grid-template-columns: 1fr; } }
        
        .project-media { 
            width: 100%; 
            border-radius: 12px; 
            overflow: hidden; 
            background: #000;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        .project-media img, .project-media video { width: 100%; display: block; }
        
        .tag { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; color: var(--accent); font-weight: 800; }
        
        .contact-links a, .project-link { 
            margin-right: 20px; 
            text-decoration: none; 
            color: var(--text); 
            font-weight: 600;
            border-bottom: 2px solid var(--accent);
            display: inline-block;
        }

        .project-link { margin-top: 15px; font-size: 0.9rem; border-bottom: 2px solid var(--accent); color: var(--accent); }
        .project-link:hover { opacity: 0.7; }

        .btn-resume {
            background: var(--accent);
            color: white !important;
            padding: 10px 20px;
            border-radius: 8px;
            border: none !important;
            margin-top: 20px;
        }
    </style>
</head>
<body data-theme="dark">

    <button class="theme-toggle" onclick="toggleTheme()" id="toggleBtn">🌙</button>

    <div class="container">
        <header>
            <div class="tag">Available for Work</div>
            <h1>{{ data.personal_info.name }}</h1>
            <p class="subtitle">{{ data.personal_info.title }} • {{ data.personal_info.location }}</p>
            <p style="max-width: 600px;">{{ data.personal_info.bio }}</p>
            <div class="contact-links">
                <a href="{{ data.personal_info.linkedin }}">LinkedIn</a>
                <a href="{{ data.personal_info.github }}">GitHub</a>
                <a href="mailto:{{ data.personal_info.email }}">Email</a>
                {% if data.personal_info.resume_link %}
                <a href="{{ data.personal_info.resume_link }}" class="btn-resume" target="_blank">View Resume</a>
                {% endif %}
            </div>
        </header>

        <section id="skills">
            <h2>Technical Skills</h2>
            <div class="skills-grid">
                {% for category, items in data.skills.items() %}
                <div class="skill-group">
                    <h4>{{ category }}</h4>
                    <div class="skill-list">
                        {% for item in items %}<span>{{ item }}</span>{% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>

        <section id="projects">
            <h2>Selected Projects</h2>
            {% for project in data.projects %}
            <div class="project-card">
                <div class="project-media">
                    {% if project.video_embed %}
                        <iframe width="100%" height="250" src="{{ project.video_embed }}" frameborder="0" allowfullscreen></iframe>
                    {% elif project.video %}
                        <video controls preload="metadata"><source src="{{ project.video }}" type="video/mp4"></video>
                    {% elif project.image %}
                        <img src="{{ project.image }}" alt="{{ project.title }}">
                    {% endif %}
                </div>
                <div class="project-info">
                    <div class="tag">{{ project.tag }}</div>
                    <h3 style="margin: 10px 0;">{{ project.title }}</h3>
                    <p style="font-size: 0.95rem; opacity: 0.9;">{{ project.description }}</p>
                    <div class="skill-list" style="margin-bottom: 15px;">
                        {% for t in project.tech %}<small style="margin-right:10px; color:var(--accent); font-weight:bold;">#{{ t }}</small>{% endfor %}
                    </div>
                    
                    {% if project.link and project.link != "#" %}
                    <a href="{{ project.link }}" target="_blank" class="project-link">View Project Details →</a>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </section>

        <section id="experience">
            <h2>Experience</h2>
            {% for job in data.experience %}
            <div style="margin-bottom: 40px;">
                <h4 style="margin:0">{{ job.role }} — {{ job.company }}</h4>
                <small style="color: var(--accent); font-weight: bold;">{{ job.duration }}</small>
                
                {# This logic creates the bullets #}
                {% if job.details is iterable and job.details is not string %}
                    <ul class="exp-list">
                        {% for point in job.details %}
                        <li>{{ point }}</li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <p>{{ job.details }}</p>
                {% endif %}
            </div>
            {% endfor %}
        </section>

        <footer style="padding: 60px 0; opacity: 0.4; font-size: 0.8rem; text-align: center;">
            © {{ data.personal_info.name }} | Created with Python
        </footer>
    </div>

    <script>
        function toggleTheme() {
            const body = document.body;
            const btn = document.getElementById('toggleBtn');
            const isDark = body.getAttribute('data-theme') === 'dark';
            body.setAttribute('data-theme', isDark ? 'light' : 'dark');
            btn.innerHTML = isDark ? '☀️' : '🌙';
            localStorage.setItem('theme', isDark ? 'light' : 'dark');
        }
        
        if(localStorage.getItem('theme') === 'light') {
            document.body.setAttribute('data-theme', 'light');
            document.getElementById('toggleBtn').innerHTML = '☀️';
        }
    </script>
</body>
</html>
"""

def build():
    template = Template(html_template)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(template.render(data=profile_data))
    print("Build Successful.")
    webbrowser.open('file://' + os.path.realpath("index.html"))

if __name__ == "__main__":
    build()
