def pythonise_string(text: str):
    new = ''.join(
        [char if char.islower() else f"_{char.lower()}" if i > 0 else char.lower() for i, char in enumerate(text) if char != ' ']
    )

    if new == "class":
        return "class_"

    return new

def camel_string(text: str):
    return text[0] + ''.join(
        [text[i] if text[i-1] != '_' else text[i].upper() for i in range(1, len(text)) if text[i] != '_']
    )

def type_check_string(text: str):
    try:
        v = float(text)
        iv = int(v)

        if v - iv == 0:
            return iv

        return v

    except Exception:
        return text
