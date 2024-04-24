# AI Art Workflow - Leonardo

## 📚 Overview

[Context](../README.md)

This script helps to create a collaborative LLM experience with bulk prompt generation. See the article linked in `Context` above for more details.

[Article mentioned here](../README.md#📚-overview)

High Level:

- Use guidance prompts to hydrate an LLM context with the concept of prompt generation and the format we want it to return data in
- Create a SQLite DB with a set schema that we can load prompts into
- Seed data into the DB
- Ad-hoc run, mod, and refine `main.py` and some of the `util/*` files to get the desired effect
- The script will concat a core theme string to all prompts

## 🧩 Dependencies

This workflow requires a paid Leonardo AI account with [API access](https://leonadoai.com/api/).

You will need to generate an API key, follow the guidance in the link above to do this.

You will optionally need access to an Chat Based LLM such as [ChatGPT](https://chat.openai.com/).

## 🏃‍♀️ How to Run

### Get setup

```bash
pipenv shell
pipenv install
```

### Run the DB migrations

This will build a `prompts.db` at the root. Recommend getting this [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) or other similar SQLite viewer.

```bash
pipenv run migrate
```

### Update seed data

Populate `db/seed.py` following the commented instructions. See article reference in [📚 Overview](README.md#📚-overview) for more details.

You can use `01_leo.md`, `02_theme.md`, `03_prompt.md` to help with getting ChatGPT primed to assist with this workflow see article above for details [📚 Overview](README.md#📚-overview).

### Run the prompt seed data

You can/will likely run this script multiple times throughout the process as you add more prompts.

The results will be upserted so no worries about re-running the seed as long as you have unique `id`s. See article referenced above for more details.

```bash
pipenv run seed
```

### Add .env

Copy past `.env.template` and rename to `.env`.

Add you Leonardo API key.

⚠️ DO NOT COMMIT THIS FILE IF YOU ARE USING SOURCE CONTROL

It should already be `gitignored`.

### Update the core routine to specify which prompts to run

In `main.py` find the `TODO:`s and address them.

`Realism mode` uses Leo's Photo Real v1 model, while `Magick mode` runs prompts iteratively through several more stylized models (see section below for details).

### (Optional) Mod util

If you want to control model IDs/elements/negative prompts/image size.

For getting info like model/elements (LoRA) ids use the Leo API:

https://docs.leonardo.ai/reference/getuserself

**Optional Tweaks**:

- Model IDs: change `MODEL_IDS` array in `util/leo.py`
- Negative prompt: change `NEGATIVE_PROMPT` string in `util/leo.py`
- Elements (LoRAs): change `elementals` array in `util/leo.py` this only applies to `Magick mode`.
- Size/aspect ratio: change `width`/`height` in the `leo_generate_image` function params

### Set start/end for prompts

In `main.py` find `START` and `END` `TODO:`s and set them to `id`s from your SQLite DB.

### Run

```bash
pipenv run start
```

Check the `app.log` and/or Leonardo AI Web UI to make sure the API generate requests were sent.

### Repeat

Seed/refine/change `START` and `END`/re-run as needed.

## 🙏 Contact and Thanks

[Thank you!](../README.md#🙏-contact-and-thanks)

## 🪪 License

[License Link](../LICENSE.md)
