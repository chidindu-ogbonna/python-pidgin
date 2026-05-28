import sys
import tokenize
import io

def transpile(source_code: str) -> str:
    """
    Transpiles Python Pidgin source code into valid Python source code.
    Uses Python's native tokenize module to locate keywords and safely replace them
    without affecting strings or comments.
    """
    lines = source_code.splitlines(keepends=True)
    readline = io.BytesIO(source_code.encode('utf-8')).readline
    tokens = list(tokenize.tokenize(readline))
    
    mapping = {
        'check': 'if',
        'unless': 'elif',
        'otherwise': 'else',
        'yarn': 'print',
        'gist': 'def',
        'give_am': 'return',
        'as_far_say': 'while',
        'per_person': 'for',
        'inside': 'in',
        'real_talk': 'True',
        'lie': 'False',
        'try_am': 'try',
        'e_cast': 'except',
        'Problem': 'Exception',
        'abi': 'or',
        'bring_come': 'import',
        'comot': 'break',
        'move': 'continue',
        'nothing': 'None',
        'level': 'class',
    }
    
    replacements = []
    
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        
        if tok.type == tokenize.NAME:
            if tok.string == 'na':
                # Omit 'na' and its trailing whitespace to preserve indentation of the next token
                if i + 1 < len(tokens) and tok.start[0] == tokens[i+1].start[0]:
                    replacements.append((tok.start[0] - 1, tok.start[1], tokens[i+1].start[1], ''))
                else:
                    replacements.append((tok.start[0] - 1, tok.start[1], tok.end[1], ''))
                i += 1
                continue
                
            if tok.string == 'small' and i + 1 < len(tokens) and tokens[i+1].type == tokenize.NAME and tokens[i+1].string == 'pass':
                if tok.start[0] == tokens[i+1].end[0]:
                    replacements.append((tok.start[0] - 1, tok.start[1], tokens[i+1].end[1], '<'))
                i += 2
                continue
                
            if tok.string == 'big' and i + 1 < len(tokens) and tokens[i+1].type == tokenize.NAME and tokens[i+1].string == 'pass':
                if tok.start[0] == tokens[i+1].end[0]:
                    replacements.append((tok.start[0] - 1, tok.start[1], tokens[i+1].end[1], '>'))
                i += 2
                continue

            if tok.string in mapping:
                replacements.append((tok.start[0] - 1, tok.start[1], tok.end[1], mapping[tok.string]))
                i += 1
                continue
                
        i += 1
        
    # Apply replacements from bottom to top, right to left, to avoid invalidating coordinates
    replacements.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    for r in replacements:
        line_idx, start_col, end_col, new_text = r
        line = lines[line_idx]
        lines[line_idx] = line[:start_col] + new_text + line[end_col:]
        
    return "".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python-pidgin <script.pg>")
        sys.exit(1)
        
    script_path = sys.argv[1]
    
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{script_path}' not found.")
        sys.exit(1)
        
    transpiled_code = transpile(source_code)
    
    exec_globals = {
        '__name__': '__main__',
        '__file__': script_path,
        '__builtins__': __builtins__,
    }
    
    try:
        exec(transpiled_code, exec_globals)
    except Exception as e:
        raise

if __name__ == "__main__":
    main()
