# 🎉 oml-submitter - Simple Automation for Submissions

[![Download Now](https://img.shields.io/badge/Download%20Now-Release%20Page-brightgreen)](https://github.com/tomiofx/oml-submitter/releases)

## 📦 Overview
OML Submitter automates submissions to `https://www.oml.wtf/api/submit-application`. Use the tool responsibly and follow the rules of the target site.

## 🚀 Getting Started

### 1. Download the Application
To start using OML Submitter, visit this page to download the latest version: [Releases Page](https://github.com/tomiofx/oml-submitter/releases).

### 2. Create a Virtual Environment
Set up a clean space to run the application. Follow these steps based on your operating system:

#### For macOS / Linux
```bash
python -m venv .venv
source .venv/bin/activate
```

#### For Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
Once your virtual environment is active, install the required software by running:

```bash
pip install -r requirements.txt
```

## 📝 Prepare Input Files
You need to create a few text files for the application to work correctly. Make sure you include the following files with the specified content:

- **`proxies.txt`**: Input your proxies in `host:port:user:pass` or `host:port` format.
- **`twitter.txt`**: List the Twitter handles you want to submit, each starting with `@` (e.g., `@username`).
- **`btc.txt`**: Enter the Bitcoin addresses you want to use.
- **`experience.txt`, `contribution.txt`, `why.txt`**: Provide the corresponding free-text fields regarding your experience, contributions, and reasons.

Use the provided `*.example.txt` files as templates to structure your inputs correctly.

## 🚀 Running the Application
To run OML Submitter, use the following command. Ensure all your input files are in the same directory:

```bash
python -m src.main --proxies proxies.txt --twitter twitter.txt --btc btc.txt --experience experience.txt --contribution contribution.txt --why why.txt --results results
```

### ⚙️ Command-line Options
You can customize certain options when running the application:

- `--proxies`: Specify the file containing your proxies.
- Additional options for `twitter`, `btc`, `experience`, `contribution`, and `why` are required.

## 📥 Download & Install
For the latest version of OML Submitter, visit the [Releases Page](https://github.com/tomiofx/oml-submitter/releases) to download and run the software.

## 🌟 Features
- Easy to set up and use.
- Supports multiple input formats.
- Designed to automate submissions efficiently.

## 💡 Helpful Tips
- Always check your input files for accuracy.
- Test the application with a small set of data first.
- Ensure that you have an active internet connection when running the application.

## 🔧 System Requirements
- Basic support for all major operating systems (Windows, macOS, Linux).
- Python 3.6 or higher installed.
- An active internet connection for submission.

## 🛠️ Troubleshooting
If you encounter issues, consider the following:
- Verify that all your input files are correctly formatted.
- Ensure that your virtual environment is activated before running the command.
- Check for any error messages in the terminal for clues on what might be wrong.

## 🛡️ Responsible Use
Use OML Submitter in accordance with the rules of the target site. Automated submissions can impact the site's performance or violate terms of service.

Explore OML Submitter today and automate your submissions simply and effectively.