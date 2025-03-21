# Chess Macro

![Chess Icon](fps_chess.ico)

A Python macro to automate room creation in FPS Chess.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Troubleshooting](#troubleshooting)
- [How to Change Description & Room Name](#how-to-change-description--room-name)
- [Contributing](#contributing)
- [License](#license)

## Overview

This macro automates the process of creating rooms in FPS Chess. It navigates through the menu,
sets up a room with a custom name and description, and can optionally activate shiny game-mode.
This script expects a resolution of 1920 by 1080.

## Features

- Automatic room creation
- Custom room name and description
- Optional shiny mode activation
- Automatic leave after enemy player leaves

## Requirements

- Python 3.x
- FPS Chess game installed
- Libraries inside of [requirements](requirements.txt)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/chess_macro.git
   ```
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure FPS Chess is running and on the main menu.
2. Open a terminal in the project directory.
3. Run the script:
   ```
   python main.py
   ```
4. Follow the on-screen prompts or use command-line arguments.

## Options

- Interactive mode: `python main.py`
- Enable shiny mode: `python main.py -y`
- Disable shiny mode: `python main.py -n`

## Troubleshooting

- Ensure your game window is visible and not minimized.
- Check that your screen resolution matches the script's expectations. (1920 x 1080)

## How to Change Description & Room Name

1. Open [config.py](main/config.py) found in the root directory using an IDE or text editor.
2. Make changes.
3. Save Changes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
