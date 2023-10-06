# Anki-Story-Generator
Fuelled by a blend of laziness and creativity, this Anki add-on swaps dull card reviews for captivating tales. Using OpenAI's GPT-3/GPT-4, it crafts stories in Japanese with your due cards. Learn and be entertained, all in one go. Because why yawn when you can be enthralled, yeah?

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
1. Once installed, go to `Tools` in your Anki menu.
2. Click on `Story Generator`.
3. Follow the on-screen instructions, from entering your OpenAI API key to selecting the number of cards and the story's topic and length.
4. Enjoy your custom story!

## Features
- **Dynamic Story Generation**: Craft unique narratives that integrate your Anki due cards.
- **Audio Integration**: Hear the story with macOS's in-built 'say' command.
- **Custom Preferences**: Choose the story's topic and length to match your mood.
  
## Contribute
Got ideas to make this even cooler? We'd love to collaborate! 
1. Fork this repo.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Credits
- OpenAI for their  GPT API.
- Anki for the platform to build upon.

---

