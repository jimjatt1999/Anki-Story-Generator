# Anki-Story-Generator
Fuelled by a blend of laziness and creativity, this Anki add-on swaps dull card reviews for captivating tales. Using OpenAI's GPT-3/GPT-4, it crafts stories in Japanese with your due cards. Learn and be entertained, all in one go. Because why yawn when you can be entertained.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contribute](#contribute)
5. [Credits](#credits)

## Installation
1. Clone this repo to your local machine using `https://github.com/jimjatt1999/Anki-Story-Generator.git` (replace with your repo link).
2. Move the cloned folder to your Anki add-ons directory.
For our Anki add-on, the __init__.py isn't just a formality - it's where the main logic of the add-on resides.
When Anki tries to load add-ons, it specifically looks for this file. So, without __init__.py, our add-on won't be recognized or loaded by Anki.
Note: Ensure you don't rename this file or change its location. It should always be in the root directory of your add-on.
3. Restart Anki.


## Usage

1. Head to `Tools` in your Anki menu.
2. Click on `Story Generator`.
3. Follow the on-screen prompts:
   - **OpenAI API Key**: Input your OpenAI API key to enable story generation.
   - **Number of Cards**: Decide how many due cards you want to include in the story.
   - **Select Topic**: Choose a theme for your narrative (Action, Romance, Mystery, Comedy).
   - **Story Length**: Determine the length of your story (Short, Medium, Long).
4. Engage with the produced story, listening to it, saving it, or reviewing associated cards.

## Features

- **Dynamic Story Generation**: Convert your due cards into engaging narratives based on user-chosen topics.
- **Customizable Story Length**: Opt for a short, medium, or long narrative based on your preference.
- **Batch Card Reviews**: Mark multiple cards with ease as 'Again', 'Hard', 'Good', or 'Easy'.
- **Auditory Learning**: Make Kyoko (macOS voice) read the story aloud for you.
- **Save Stories**: Preserve your generated tales by saving them to a file.
- **GUI Integration**: All features are accessible through a user-friendly graphical interface.

## Contribute

Wanna spice things up even more? Your contributions are welcome!
1. Fork this repo.
2. Create your feature branch.
3. Commit your magic.
4. Push it.
5. Open a pull request.

## Credits
- OpenAI for their  GPT API.
- Anki for the platform to build upon.

---

