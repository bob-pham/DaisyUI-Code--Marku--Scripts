import os
import sys
import re 
import json

INVALID_INPUT = 'Invalid Input, Exitting...'

def parse_input(fp, jsx):
    lines = fp.readlines()

    keywords = []
    other = []

    if os.path.exists('config.json'):
        with open('config.json', 'r') as cfg:
            j = json.load(cfg)
            keywords = j["keywords"]
            other = j["other"]

    if jsx:
        for i in range(len(lines)):
            curr = lines[i].replace('\n', '').replace('\\', '\\\\').replace('\'', '\\\'').replace('\"', '\\\"')

            # if other:
            #     for (regex, edit) in other:
            #         words = re.findall(regex, curr)

            #         visited = {}

            #         for word in words:
            #             if word not in visited.keys():
            #                 visited[word] = 1
            #                 curr = curr.replace(word, '\"}{<span className=\"' + edit + '\">' + word + '</span>}{\"')

            temp = curr.split(' ')

            if keywords:
                curr = ''
                for word in temp:
                    for (regex, edit) in keywords:
                        if re.search(regex, word):
                            word = '\"}{<span className=\"' + edit + '\">' + word + '</span>}{\"'
                            break
                    curr += word + ' '

            # curr = curr.replace('\"\"', '\"')

            lines[i] = f'<pre data-prefix=\"{i}\">' + '<code>{\"'+ curr + '\"}</code></pre>\n'
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