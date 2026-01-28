# Chemical Equipment Parameter Visualizer (Hybrid App)

A hybrid data analytics platform featuring a shared **Django REST API** serving both a **React.js Web Frontend** and a **PyQt5 Desktop Application**.

## 🚀 Features
- **User Authentication**: Secure Login/Signup using JWT (JSON Web Tokens).
- **CSV Data Analytics**: Automated parsing of chemical equipment parameters using Pandas.
- **Hybrid Visualization**: 
  - **Web**: Interactive charts using Chart.js with Light/Dark mode.
  - **Desktop**: Native data visualization using Matplotlib.
- **History Management**: Tracks and displays the last 5 uploaded datasets.
- **Report Generation**: Ability to download analyzed data summaries.

## 🛠️ Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, Django, Django REST Framework |
| **Frontend (Web)** | React.js, Tailwind CSS, Chart.js |
| **Frontend (Desktop)** | PyQt5, Matplotlib |
| **Data Handling** | Pandas, SQLite |

## 📦 Installation & Setup

### 1. Backend Setup
```bash
cd chemical_backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver