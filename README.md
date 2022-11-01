# DaisyUI Code Markup Script

Scripts that generate HTML or JSX to be used in [DaisyUI's Code Markup Blocks](https://daisyui.com/components/mockup-code/)

# Usage

If you want syntax highlighting, add a ```.json``` file named ```config.json``` into the sample directory, which store the regex and highlight colour for syntax highlighting. Two categories, keywords and other. Example ReGex are within the configs directory, but these ```.json``` files need to be renamed and moved in order to work. 
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
- Syntax highlighting supported
## Todo:
- Support syntax highlighting of . operators and strings