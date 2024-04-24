# AI Art Workflow - Vid Fix

## 📚 Overview

[Context](../README.md)

This script takes any videos (`.mp4` only) in `input/*` and resizes them to 1920x1080 (adding a blur effect for anything outside that aspect ratio) to `output/*`.

Additionally it can be used to resize landscape videos form `tok_input/*` to `tok_output/*` portrait for optimal TikTok/other platform shorts.

## 🏃‍♀️ How to Run

### Get setup

```bash
pipenv shell
pipenv install
```

### Resize Videos

Copy/paste videos to `input/*` and they will show up in `output/*`.

```bash
pipenv run start
```

### Resize to Portrait

Copy/paste videos to `tok_input/*` and they will show up in `tok_output/*`.

```bash
pipenv run tok
```

## 🙏 Contact and Thanks

[Thank you!](../README.md#🙏-contact-and-thanks)

## 🪪 License

[License Link](../LICENSE.md)
