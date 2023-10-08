import re

def remove_ansi_codes_from_file(filename):
    # Regular expression pattern to match ANSI codes
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

    with open(filename, 'r') as f:
        content = f.read()

    cleaned_content = ansi_escape.sub('', content)

    with open(filename, 'w') as f:
        f.write(cleaned_content)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 script_name.py filename")
    else:
        remove_ansi_codes_from_file(sys.argv[1])
