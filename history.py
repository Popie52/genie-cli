import json
import os
from google.genai import types

HISTORY_FILE = 'chat_history.json'


def content_to_dict(content: types.Content) -> dict:
    """Convert types.Content to plain dict for JSON."""
    return {
        'role': content.role,
        'parts': [{'text': p.text, 'function_response': p.function_response.__dict__ if p.function_response else None}
                  for p in content.parts]
    }


def content_from_dict(data: dict) -> types.Content:
    """Convert dict back to types.Content."""
    parts = []
    for p in data.get('parts', []):
        part = types.Part(text=p.get('text', ''))
        # Skip function_response reconstruction for simplicity
        parts.append(part)
    return types.Content(role=data.get('role', 'user'), parts=parts)


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:  # empty file
                return []
            data = json.loads(content)
            return [content_from_dict(m) for m in data]
    return []


def save_history(history):
    with open(HISTORY_FILE, 'w', encoding="utf-8") as f:
        json.dump([content_to_dict(m) for m in history], f, indent=2)
