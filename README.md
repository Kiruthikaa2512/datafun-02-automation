````markdown
# datafun-02-automation

## Project Overview

This repository supports a **Supplier Performance Analytics** automation project using Python. The goal is to automate the creation of organized folder structures for supplier data across years and formats. This structure enables clean storage and easy access to inputs, outputs, and periodic reports. The project follows professional setup practices including Git version control, virtual environments, and dependency tracking.

---

## Local Machine Setup

### Step 1: Install Python (if not installed)

- Download from: https://www.python.org/downloads/
- Verify installation:

```bash
python --version
````

---

##  Project Initialization & GitHub Setup

### Step 2: Create and Clone GitHub Repo

1. Navigate to [GitHub](https://github.com/)
2. Create a new repository named: `datafun-02-automation`
3. Select:  **Add a README.md**
4. Clone the repo locally:

```bash
git clone https://github.com/YOUR-USERNAME/datafun-02-automation.git
cd datafun-02-automation
```

---

### Step 3: Set Up Version Control

#### Add `.gitignore`

```bash
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
```

#### Track Files with Git

```bash
git add .
git commit -m "Initial commit with project structure"
git push origin main
```

---

##  Virtual Environment & Dependency Setup

### Step 4: Set Up Python Environment

#### Create virtual environment:

```bash
python -m venv venv
```

#### Activate environment:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

---

### Step 5: Manage Dependencies

#### Add Required Libraries

```bash
pip install pandas
```

#### Freeze dependencies

```bash
pip freeze > requirements.txt
```

---

##  Automation Script Execution

### Step 6: Run Folder Creation Utility

Ensure the utility script exists under:

```
/utils/create_folders.py
```

Run it using:

```bash
python utils/create_folders.py
```

It will create the entire folder structure:

---

## Final Folder Structure Created

### Year-Based Folders:

```
2020/
2021/
2022/
2023/
```

### Supplier-Specific Folders:

```
abclogistics/
evergreendistribution/
globalfreightco/
nextgentransport/
```

### Input/Output Format Folders:

```
data-csv/
data-excel/
data-json/
output-csv/
output-excel/
output-json/
```

### Periodic Batch Folders:

```
periodic_folder_1/
periodic_folder_2/
periodic_folder_3/
periodic_folder_4/
```

These folders provide structured organization for your analytics and automation work.

---

## Weekly Progress Summary

* Created Python utility script for automated folder generation.
* Completed all TODO items:

  * Dynamic year and supplier lists
  * Existence checks to avoid duplicates
  * Logging of created folders
* Matched actual output with expected structure using screenshots
* Updated `README.md` for full documentation
* Project committed and pushed to GitHub

---

## Common Git Commands

```bash
# Check status
git status

# Stage changes
git add .

# Commit with message
git commit -m "Completed folder utility script and structure setup"

# Push to GitHub
git push origin main
```

---

## Best Practices

* Use virtual environments for isolation.
* Commit regularly with clear messages.
* Always run scripts from the project root.
* Organize data clearly by type and time.

---

##  Acknowledgements

* **Dr. Denise Case** – for course guidance and practical feedback.
* **Open-source Python community** – for tools and libraries that support automation.

---

