import openai
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import subprocess

def get_openai_api_key():
    api_key, ok = QInputDialog.getText(mw, "OpenAI API Key", "Enter your OpenAI API key:")
    if ok and api_key:
        openai.api_key = api_key.strip()
        return api_key.strip()
    else:
        showInfo("API key is required to proceed.")
        return None

def get_due_cards(num_cards):
    card_ids = mw.col.find_cards('is:due')
    card_ids = card_ids[:num_cards]  # Limit the number of cards here
    cards_info = []
    for card_id in card_ids:
        card = mw.col.getCard(card_id)
        note = card.note()
        expression = note.fields[0]  # Adjust index based on your Anki deck's structure
        meaning = note.fields[1]  # Adjust index based on your Anki deck's structure
        cards_info.append({"card_id": card_id, "expression": expression, "meaning": meaning})
    return cards_info

def generate_story_or_essay(topic, card_data, story_length):
    prompt = f"Write a {topic} incorporating the expressions and meanings provided in Japanese:\n" + \
             ''.join([f"Expression: {card['expression']}\nMeaning: {card['meaning']}\n" for card in card_data]) + \
             { "Short": "Create a short narrative. ", "Medium": "Develop a moderately detailed story. ", "Long": "Write a long and detailed narrative. "}[story_length] + \
             "Please weave these expressions into a cohesive and interesting narrative in Japanese."
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": prompt}])
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        showInfo(f"An error occurred while generating the story: {str(e)}")
        return None

def read_aloud(text):
    subprocess.run(["say", "-v", "Kyoko", text])

class PreviewWindow(QDialog):
    def __init__(self, story_text, card_data):
        super().__init__(mw)
        layout = QVBoxLayout()
        story_text_edit = QTextEdit()
        story_text_edit.setPlainText(story_text)
        story_text_edit.setReadOnly(True)
        story_text_edit.setMinimumSize(600, 400)  # Set a minimum size for the QTextEdit widget
        layout.addWidget(story_text_edit)
        layout.addWidget(QPushButton('Read Aloud', clicked=lambda: read_aloud(story_text)))
        layout.addWidget(QPushButton('Save to File', clicked=self.save_to_file))
        layout.addWidget(QPushButton('Mark Cards as Again', clicked=lambda: self.mark_cards_as(1, card_data)))
        layout.addWidget(QPushButton('Mark Cards as Hard', clicked=lambda: self.mark_cards_as(2, card_data)))
        layout.addWidget(QPushButton('Mark Cards as Good', clicked=lambda: self.mark_cards_as(3, card_data)))
        layout.addWidget(QPushButton('Mark Cards as Easy', clicked=lambda: self.mark_cards_as(4, card_data)))
        self.story_text = story_text
        self.setLayout(layout)
        self.setWindowTitle('Story Preview')
        self.show()

    def save_to_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w', encoding='utf-8') as file:
                file.write(self.story_text)

    def mark_cards_as(self, ease, card_data):
        for card in card_data:
            current_card = mw.col.getCard(card['card_id'])
            current_card.startTimer()  # Initializing the timer
            mw.col.sched.answerCard(current_card, ease)
        showInfo(f"Cards have been marked.")


def show_dialog():
    openai_api_key = get_openai_api_key()
    if not openai_api_key:
        showInfo("No API key provided. The add-on will not function correctly without a valid API key.")
        return

    num_cards, ok = QInputDialog.getInt(mw, "Number of Cards", "Enter the number of cards to use:", min=1)
    if not ok:
        return

    due_cards = get_due_cards(num_cards)

    topic, ok = QInputDialog.getItem(mw, "Select Topic", "Select a topic for your story:", ["Action Story", "Romance Story", "Mystery Story", "Comedy Story"], 0, False)
    if not ok:
        return

    story_length, ok = QInputDialog.getItem(mw, "Select Story Length", "Select a length for your story:", ["Short", "Medium", "Long"], 0, False)
    if not ok:
        return

    story = generate_story_or_essay(topic, due_cards, story_length)
    if story:
        preview_window = PreviewWindow(story, due_cards)
    else:
        showInfo("Failed to generate a story.")

action = QAction("Story Generator", mw)
action.triggered.connect(show_dialog)
mw.form.menuTools.addAction(action)
