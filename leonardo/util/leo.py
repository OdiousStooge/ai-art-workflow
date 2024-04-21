import os
import requests
import logging

# Constants
LEONARDO_API = os.getenv("LEONARDO_API")
STANDARD_HEADERS = headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {LEONARDO_API}",
}
GENERATIONS_URL = "https://cloud.leonardo.ai/api/rest/v1/generations"
MODEL_IDS = [
    "aa77f04e-3eec-4034-9c07-d0f619684628",
    # "5c232a9e-9061-4777-980a-ddc8e65647c6",
    # "1e60896f-3c26-4296-8ecc-53e2afecc132",
]
NEGATIVE_PROMPT = "close up, two heads, two faces, plastic, Deformed, blurry, bad anatomy, bad eyes, crossed eyes, disfigured, poorly drawn face, mutation, mutated, ((extra limb)), ugly, poorly drawn hands, missing limb, blurry, floating limbs, disconnected limbs, malformed hands, blur, out of focus, long neck, long body, ((((mutated hands and fingers)))), (((out of frame))), blender, doll, cropped, low-res, close-up, poorly-drawn face, out of frame double, two heads, blurred, ugly, disfigured, too many fingers, deformed, repetitive, black and white, grainy, extra limbs, bad anatomyHigh pass filter, airbrush, portrait, zoomed, soft light, smooth skin, closeup, deformed, extra limbs, extra fingers, mutated hands, bad anatomy, bad proportions , blind, bad eyes, ugly eyes, dead eyes, blur, vignette, out of shot, out of focus, gaussian, closeup, monochrome, grainy, noisy, text, writing, watermark, logo, oversaturation , over saturation, over shadow"  # noqa


def leo_get(url):
    logging.info(f"Sending request to {url}")
    response = requests.get(url, headers=STANDARD_HEADERS)
    logging.info(f"Received response with status code {response.status_code}")

    return response.text


def leo_post(url, payload):
    logging.info(f"POST to {url} with payload {payload}")
    response = requests.post(url, headers=STANDARD_HEADERS, json=payload)
    logging.info(f"Received response with status code {response.status_code}")

    return response.text


def leo_generate_image(
    prompt,
    negative_prompt,
    model_id="6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",
    num_images=4,
    alchemy=True,
    nsfw=True,
    width=1024,
    height=576,
    preset_style="DYNAMIC",
    photo_real=False,
    elements=None,
):
    payload = {
        "height": height,
        "modelId": model_id,
        "prompt": prompt,
        "width": width,
        "alchemy": alchemy,
        "negative_prompt": negative_prompt,
        "nsfw": nsfw,
        "num_images": num_images,
        "presetStyle": preset_style,
        "photoReal": photo_real,
        "elements": elements,
    }
    logging.info(f"Sending payload {payload} to {GENERATIONS_URL}")
    response_data = leo_post(GENERATIONS_URL, payload)
    logging.info(f"Received response data {response_data}")

    return response_data


def clean_prompt(prompt):
    # Trim carriage returns and new lines from prompt
    prompt = prompt.replace("\r", "")
    prompt = prompt.replace("\n", "")

    return prompt


def combine_prompt(prompt, core_theme=None):
    # Wrap prompt in core theme if present
    if core_theme:
        prompt = f"{prompt}, {core_theme}"

    return prompt


def prepare_prompt(prompt, core_theme=None, negative_prompt=NEGATIVE_PROMPT):
    prompt = clean_prompt(prompt)
    prompt = combine_prompt(prompt, core_theme)

    return prompt


def leo_realism(prompt, core_theme=None, negative_prompt=NEGATIVE_PROMPT):
    logging.info("Doing Realism")
    # style = "RETRO"
    style = "CINEMATIC"

    # Clean and combine prompt
    prompt = prepare_prompt(prompt, core_theme, negative_prompt)

    # Generate for each model
    output_images = []

    # With negative prompt
    # response_data = leo_generate_image(
    #     prompt, negative_prompt, None, photo_real=True, preset_style=style
    # )
    use_photo_real = True
    response_data = leo_generate_image(
        prompt,
        negative_prompt,
        None,
        photo_real=use_photo_real,
        preset_style=style,
    )
    output_images.append(response_data)

    # Without negative prompt
    # response_data = leo_generate_image(
    #     prompt, None, None, photo_real=True, preset_style=style
    # )
    response_data = leo_generate_image(
        prompt,
        None,
        None,
        photo_real=use_photo_real,
        preset_style=style,
    )
    output_images.append(response_data)

    logging.info("Finished Realism")

    return output_images


def leo_magick(prompt, core_theme=None, negative_prompt=NEGATIVE_PROMPT):
    logging.info("Doing Magick")

    # Clean and combine prompt
    prompt = prepare_prompt(prompt, core_theme, negative_prompt)

    # Generate for each model
    output_images = []
    # elementals = [{"akUUID": "815de207-d352-4d46-9310-3fcd5324a7e2", "weight": 1}]
    # elementals = [
    #     {"akUUID": "d5d5ce55-5f3b-4bea-bb37-df6a4b5f3519", "weight": 0.1},
    #     {"akUUID": "62667fde-70da-4db5-b047-8c70b43c38e7", "weight": -0.1},
    #     {"akUUID": "5db13b9c-0b0b-4684-87ca-01f59c97aae0", "weight": 0.2},
    #     {"akUUID": "d0ebdbf7-a570-4b93-8406-306bbb2a3469", "weight": -0.1},
    # ]
    # elementals = [
    #     {"akUUID": "5db13b9c-0b0b-4684-87ca-01f59c97aae0", "weight": 0.5},
    # ]
    elementals = []

    for model_id in MODEL_IDS:
        # With negative prompt
        response_data = leo_generate_image(
            prompt,
            negative_prompt,
            model_id,
            elements=elementals,
            preset_style="ILLUSTRATION",
        )
        output_images.append(response_data)

        # Without negative prompt
        response_data = leo_generate_image(
            prompt, None, model_id, elements=elementals, preset_style="ILLUSTRATION"
        )
        output_images.append(response_data)
    logging.info("Finished Magick")

    return output_images
