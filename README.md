# Notee

## Notee is python CLI that is able to fully replace your note making app or just be your fast way to create notes in terminal with additional functionality.

Sometimes I have an idea that comes from nowhere and to note it I have to open my obsidian app, create file and only then write my note, it's too slow. I created python CLI that will allow you to start writing your notes just after one command of 9 characters. Also there is functionality like ai module or search with vector database included.

## Technologies

* [Typer](https://typer.tiangolo.com/) - to realize CLI functionality.
* [Chroma DB](https://www.trychroma.com/) - vector db for AI context and extendet search through your notes.
* [MdUtils](https://pypi.org/project/mdutils/) - for the md files creation.
* [Rich](https://rich.readthedocs.io/en/stable/index.html) - to make prints prettier.

---

## How to use

! **Requires python version between 3.12-3.14, it might work on older ones but won't work on 1.14.. because of chroma db bug**
1. Install package by running `pipx install notee`.
2. Run `notee setup` and go throught instuctions in the console.

**Done!** Now you can use it freely🎉

---

## Commands

- `setup` - setup notee before using it. 
- `idea` - create idea note.
- `movie` - create movie review note.
- `book` - create book review note.
- `source` - create note about source to something.
- `todo` - create todo note.
- `search QUERY` - search notes related to your query.
- `open` - open your note in the terminal.
- `scan` - scan your vault and add new notes to the database.
- `obsidian_mode --on/--off` - use to manage obsidian mode(only affects how tags are created).
- `different_folders --on/--off` - toggle between creating folder for each tipe of template or store all notes in core folder.
- `ai_module --on/-off` - toggle between using ai module or not.
- `setup_ai` - change Ai provider/api key.
- `ask QUERY` - ask AI question and it'll answer it based on your notes.
- `change_ai_model AI_MODEL_NAME` - change default ai model. Please be careful and make sure that you're passing correct model name.

| AI provider | Default model |
|----------|----------|
| Open AI | `gpt-4.1-mini-2025-04-14` |
| Google Gemini | `gemini-2.5-flash` |
| Hack Club AI API | `google/gemini-2.5-flash` |

## Found error?

Please let me know about it by submitting issue on the github repository. I'll try to fix it as fast as possible!
