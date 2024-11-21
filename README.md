# PDF to Markdown Converter

This project converts PDF slides into a Markdown file with images. Each slide in the PDF is processed and saved as a high-quality image in a dedicated folder. Additionally, a Markdown file is created, referencing these images for easy integration into note-taking applications like Obsidian. The script ensures all images are organized in a specified folder, and the Markdown file is stored in a separate directory as per user-defined paths.

## Requirements

- Python 3.6 or higher
- `pip` (Python package installer)

## Installation

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run:
    ```sh
    git clone https://github.com/yourusername/pdf-to-markdown-converter.git
    cd pdf-to-markdown-converter
    ```

3. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

5. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script**:
    ```sh
    python main.py
    ```

2. **Follow the prompts**:
    - Enter the path where the note file should be saved.
    - Enter the name for the note file (without `.md`).
    - Enter the base path where images should be stored.
    - Enter the name for the images folder.
    - Enter the path to your PDF file.

3. **Check the output**:
    - The images will be saved in the specified folder.
    - The Markdown file will be created at the specified path.

## User Guide

### Step-by-Step Instructions

1. **Install Python**:
    - Go to [python.org](https://www.python.org/downloads/).
    - Download the latest version of Python.
    - Follow the installation instructions for your operating system.

2. **Open a Terminal**:
    - On Windows, press `Win + R`, type `cmd`, and press Enter.
    - On macOS, press `Cmd + Space`, type `Terminal`, and press Enter.
    - On Linux, open your preferred terminal emulator.

3. **Clone the Repository**:
    - In the terminal, type:
        ```sh
        git clone https://github.com/yourusername/pdf-to-markdown-converter.git
        cd pdf-to-markdown-converter
        ```

4. **Create and Activate a Virtual Environment**:
    - In the terminal, type:
        ```sh
        python -m venv venv
        ```
    - Activate the virtual environment:
        - On Windows:
            ```sh
            venv\Scripts\activate
            ```
        - On macOS/Linux:
            ```sh
            source venv/bin/activate
            ```

5. **Install Required Packages**:
    - In the terminal, type:
        ```sh
        pip install -r requirements.txt
        ```

6. **Run the Script**:
    - In the terminal, type:
        ```sh
        python main.py
        ```

7. **Follow the Prompts**:
    - Enter the required paths and names as prompted by the script.

8. **Check the Output**:
    - The images will be saved in the specified folder.
    - The Markdown file will be created at the specified path.

### Troubleshooting

- **Python not found**: Ensure Python is installed and added to your system's PATH.
- **Permission errors**: Ensure you have the necessary permissions to read the PDF file and write to the specified directories.
- **Missing packages**: Ensure all required packages are installed by running `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.