# Atlas Project

A Django-based web application for managing geospatial or custom application data.

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/amir-ekhtiyari/atlas_project.git
   cd atlas_project
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Load initial data**
   ```bash
   python manage.py loaddata atlas_data.json
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

---

## 📁 Project Structure

- `atlas_project/` – Main Django project directory
- `your_app_name/` – Django app(s)
- `templates/` – HTML templates
- `static/` – Static files (CSS, JS, images)
- `fixtures/` – JSON data like `atlas_data.json`

---

## 🤝 Contributing

To contribute to this project:

- Fork the repo
- Create a new branch (`git checkout -b feature-name`)
- Commit your changes (`git commit -m 'Add feature'`)
- Push to your branch (`git push origin feature-name`)
- Submit a Pull Request

---

## 📝 License

This project is licensed under the MIT License.
