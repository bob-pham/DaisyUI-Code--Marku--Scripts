import os
import sys

INVALID_INPUT = 'Invalid Input, Exitting...'

def parse_input(fp, jsx):
    lines = fp.readlines()

    if jsx:
        for i in range(len(lines)):
            lines[i] = f'<pre data-prefix=\"{i}\">' + '<code>{\"'+ lines[i].replace('\n', '').replace('\'', '\\\'').replace('\"', '\\\"').replace('\\', '\\\\') + '\"}</code></pre>\n'
    else:
        for i in range(len(lines)):
            lines[i] = f'<pre data-prefix=\"{i}\">' + '<code>'+ lines[i].replace('\n', '') + '</code></pre>\n'
    
    output_name = 'output_jsx' if jsx else 'output_html'

    with open(output_name, 'w') as out:
        out.writelines(lines)

def handle_inputs():
    if len(sys.argv) != 2:
        print(INVALID_INPUT)
    else:
        if (os.path.exists(sys.argv[1])):
            with open(sys.argv[1], 'r') as fp:
                parse_input(fp)

        else:
            print(INVALID_INPUT)

handle_inputs()