## Devowser

A lightweight, undetectable browser automation tool that launches a Chrome browser instance without triggering anti-bot detection systems. Devowser helps you automate browsing tasks while maintaining a natural browsing profile.

## Features

- Launches a clean Chrome browser instance without detectable automation flags
- Clears cookies and settings on each run
- Maintains a natural browsing profile to avoid detection
- Works with standard Chrome browser installations
- Lightweight with minimal resource usage


## Requirements

- Python 3.6+
- Chrome browser installed
- Required Python packages:
  - selenium
  - pywin32
  - pyinstaller (for building executable)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/devowser.git
   cd devowser
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application directly:
```
python app.py
```

This will launch a new Chrome browser window that opens Google by default. The browser will remain open until closed manually.

## Building Executable

You can build a standalone Windows executable using the included build script:

```
python build-win.py
```

Or run the build command directly:
```
build-win.cmd
```

The compiled executable will be created in the `dist` folder.

## Customization

To customize browser behavior, modify the `app.py` file:
- Change the URL on line 39 (`driver.get("https://www.google.com/")`)
- Add additional Chrome options in the options configuration section
- Implement custom browsing logic as needed

## Legal Disclaimer

This tool is provided for educational and research purposes only. Users are responsible for complying with all applicable laws and website terms of service when using Devowser. The developers assume no liability for misuse of this software.
