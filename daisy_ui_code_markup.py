import os
import sys
import re 
import json

INVALID_INPUT = 'Invalid Input, Exitting...'

def find_and_replace_string(reg, line):
    for (regex, edit) in reg:
        words = re.findall(regex, line)
                
        visited = {}
        for word in words:
            if word not in visited.keys():
                visited[word] = 1
                line = line.replace(word, '\"}{<span className=\"' + edit + '\">{\"' + word + '\"}</span>}{\"')

    return line

def find_and_replace_word(reg, line):
    temp = line.split(' ')
    line = ''

    for word in temp:
        for (regex, edit) in reg:
            if re.search(regex, word):
                word = '\"}{<span className=\"' + edit + '\">{\"' + word + '\"}</span>}{\"'
                break
        line += word + ' '
    
    return line 

def parse_input(fp, jsx):
    lines = fp.readlines()

    keywords = []
    other = []
    strings = []
    comments= []

    if os.path.exists('config.json'):
        with open('config.json', 'r') as cfg:
            j = json.load(cfg)
            keywords = j["keywords"]
            other = j["other"]
            strings = j["strings"]
            comments = j["comments"]

    if jsx:
        for i in range(len(lines)):
            curr = lines[i].replace('\n', '').replace('\\', '\\\\').replace('\'', '\\\'').replace('\"', '\\\"')

            if strings:
               curr = find_and_replace_string(strings, curr) 

            if other:
                curr = find_and_replace_word(other, curr)

            if keywords:
                curr = find_and_replace_word(keywords, curr)

            lines[i] = f'<pre data-prefix=\"{i + 1}\">' + '<code>{\"'+ curr + '\"}</code></pre>\n'
    else:
        for i in range(len(lines)):
            lines[i] = f'<pre data-prefix=\"{i}\">' + '<code>'+ lines[i].replace('\n', '') + '</code></pre>\n'
    
    output_name = 'output_jsx' if jsx else 'output_html'

    with open(output_name, 'w') as out:
        out.writelines(lines)

def handle_inputs():
    if len(sys.argv) > 3:
        print(INVALID_INPUT)
    else:
        if (os.path.exists(sys.argv[1])):
            with open(sys.argv[1], 'r') as fp:
                parse_input(fp, 'jsx' in sys.argv)

        else:
            print(INVALID_INPUT)

handle_inputs()