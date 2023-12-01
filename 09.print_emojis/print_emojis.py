import emoji

# Get all emojis from the emoji module
all_emojis = emoji.EMOJI_DATA

# Print each emoji
for emoji_name, emoji_details in all_emojis.items():
    print(f"{emoji_name}: {emoji_details['en']}")