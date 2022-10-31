# DaisyUI Code Markup Script

Scripts that generate HTML or JSX to be used in [DaisyUI's Code Markup Blocks](https://daisyui.com/components/mockup-code/)

# Usage

## Args

```
[file_name] - name of the file containing code
[jsx] - Output file returns jsx instead of html
```

To use, simply run the script specifying the file name and specify if you want jsx. Note that the input file must be in the same directory, and all the code within the file will be read, line by line.

**Ex.**

```
python daisy_ui_code_markup.py my_file.jsx jsx
```

**output file will be [file_name]_output, and placed in the same directory**

# Changelog

## Todo:
- Syntax highlighting support