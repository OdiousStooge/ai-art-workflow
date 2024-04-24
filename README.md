# AI Art Workflow

## 📚 Overview

Sharing [Odious Stooge's](https://linktr.ee/OdiousStooge) workflow for generating AI art. See this article for more context:

**Civitai Article on Workflow**:

https://civitai.com/articles/5029

## 🧩 Dependencies/Setup

- Required: Latest version of [Python](https://www.python.org/downloads/)
- Optional: Install [pipx](https://github.com/pypa/pipx) for global package management
- Optional: `pipx install black flake8`
- Required: `pipx install pipenv` or `pip install pipenv` if not using `pipx`

## 📂 Important Files

Roughly in order of how you might use them. Instructions on how to use these are in associated `README`s.

- `leonardo/`: Scripts and readmes for interfacing with ChatGPT to help generate prompts in a DB migration format and then bulk post prompts to [Leonardo AI](https://leonardo.ai/)
- `image-fix/`: Scripts for resizing (and blurring if smaller than HD) images in bulk
- `vid-fix/`: Scripts for resizing videos (and blurring as needed) in bulk similar to `image-fix`
- `yt-audio/`: Scripts for downloading audio `.mp3` from YouTube (⚠️ be sure to check licenses for a given video before doing this!)
- `convert-sqlite/`: Scripts to convert your `leonardo/prompts.db` to CSV if you want to share prompts
- `editing/`: Just a workspace to store any files for editing, I put my [ShotCut](https://shotcut.org/) and [Gimp](https://www.gimp.org/) stuff here and keep it `gitignored`.

## 🙏 Contact and Thanks

Thanks for reading and showing interest. Always happy to chat with folks so feel free to reach out and collab, [heres my links](https://linktr.ee/OdiousStooge).

Probably easiest to reach me on [Civitai](https://civitai.com/user/OdiousStooge).

I encourage others to share their workflows as well and let me know if this helped you. Please check out my links if interested and "like" if you like:
https://linktr.ee/OdiousStooge

and if willing/able, any donations to gen costs are much appreciated:

https://buymeacoffee.com/odiousstooge

but I will still do this for free and share regardless.

Thank you!

## 🪪 License

[License Link](./LICENSE.md)
