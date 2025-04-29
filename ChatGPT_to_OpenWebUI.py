import json
import os
import uuid

# ===== CONFIGURATION =====
SOURCE_FOLDER = 'chatgpt123'               # <-- Your extracted ChatGPT folder
CONVERSATIONS_FILE = 'conversations.json'  # <-- The actual JSON file inside the folder
OUTPUT_JSON_FILE = 'openwebui_import.json' # <-- Output file to import into OpenWebUI
# ==========================

def load_conversations(source_folder):
    convos_path = os.path.join(source_folder, CONVERSATIONS_FILE)
    with open(convos_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_to_openwebui_format(chat_data):
    conversations = []
    
    # Checking for the 'mapping' structure
    if "mapping" not in chat_data:
        print("Invalid chat data structure!")
        return conversations  # If no valid mapping, return empty

    mapping = chat_data["mapping"]

    # Iterating over the mapping to extract messages
    for entry in mapping.values():
        if 'message' in entry:
            msg = entry['message']
            role = msg['author']['role']
            content = msg['content'].get('parts', [])

            # Ensuring we only store valid message content
            if content:
                conversation = {
                    "id": str(uuid.uuid4()),  # Generate a unique ID for each conversation
                    "messages": [
                        {
                            "role": role,
                            "content": content[0]  # Assuming the first part holds the message
                        }
                    ]
                }
                conversations.append(conversation)

    return {"conversations": conversations}

def main():
    print(f"Loading conversations from {SOURCE_FOLDER}/{CONVERSATIONS_FILE}...")
    chat_data = load_conversations(SOURCE_FOLDER)

    print("Converting to OpenWebUI format...")
    openwebui_data = convert_to_openwebui_format(chat_data)

    # Output the data as a JSON file
    print(f"Saving as {OUTPUT_JSON_FILE}...")
    with open(OUTPUT_JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(openwebui_data, f, indent=2)

    print("Done! You can now import 'openwebui_import.json' into OpenWebUI.")

if __name__ == "__main__":
    main()
