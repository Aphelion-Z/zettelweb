# ZettelWeb Quick Start Guide

Get ZettelWeb running in less than 5 minutes.

## Prerequisites

- Python 3.8 or higher
- Zettelstore installed and running

## Step 1: Start Zettelstore

```bash
cd path/to/zettelstore
./zettelstore.exe run  # Windows
# or
./zettelstore run      # Linux/macOS
```

Verify at: http://127.0.0.1:23123

## Step 2: Setup ZettelWeb

```bash
cd zettelweb-code
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
# or: venv\Scripts\activate   # Windows CMD/PowerShell
# or: source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

## Step 3: Run Application

```bash
python app.py
```

## Step 4: Open Browser

Navigate to: http://127.0.0.1:5000

You should see a table listing all your Zettel with IDs and titles.

## Troubleshooting

**"Connection refused"**
- Ensure Zettelstore is running on port 23123
- Check firewall settings

**"ModuleNotFoundError"**
- Activate virtual environment
- Run `pip install -r requirements.txt`

**"Empty list"**
- Create some Zettel in Zettelstore first
- Check Zettelstore is accessible at http://127.0.0.1:23123/z

## Architecture

```
Browser → Flask (app.py) → Zettelstore API → Zettel Files
```

Current implementation fetches Zettel list via GET /z endpoint without authentication.
