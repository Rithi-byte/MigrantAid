📌 MigrantAid – Empowering Migrant Workers
MigrantAid is a web platform built with Flask, HTML, CSS, JS, and AI/NLP libraries to support migrant workers by providing:

🎓 Upskilling courses
📰 Latest news and policies
🆘 Helpline chatbot
🤝 Legal and social aid
🌐 Website Sections
Home – Introduction to the platform
Courses – Free learning resources for skill-building
News – Migrant-related policy updates and news
Helpline – A chatbot that helps users ask questions and get quick help
⚙️ Tech Stack
Frontend: HTML, CSS, Bootstrap, AOS, LottieFiles
Backend: Flask (Python)
Database: SQLite / MySQL (optional)

🛠️ Running the Project Locally
Clone the repository
CopyRun
git clone https://github.com/your-username/MigrantAid.git
cd MigrantAid
Create a virtual environment (optional but recommended)
CopyRun
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Install dependencies
CopyRun
pip install -r requirements.txt
Run the Flask app
CopyRun
python app.py
Open in browser
Navigate to http://127.0.0.1:5000
🚀 Deployment (To Be Done)
You can deploy this app for free using Render:

Go to https://render.com
Create an account and click "New Web Service"
Connect your GitHub repository
Set the Build Command:
CopyRun
pip install -r requirements.txt
Set the Start Command:
CopyRun
python app.py
Set environment variable (if required):
CopyRun
PORT=10000
Choose "Python" as the environment
📁 Folder Structure
CopyRun
MigrantAid/
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── courses.html
│   ├── news.html
│   └── helpline.html
├── app.py
├── requirements.txt
└── README.md
🧠 Features
🔹 Real-time chatbot responses (via API)
🔹 Clean and responsive design
🔹 Easy-to-navigate interface
🔹 Dynamic content updates
🤝 Contributions
Pull requests are welcome!
If you'd like to contribute, please fork the repository and create a pull request.
For major changes, open an issue first to discuss what you would like to change.

📄 License
This project is licensed under the MIT License.

✨ Author
Developed with ❤️ by Rithika
