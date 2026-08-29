import json
import os
import sys
from dotenv import load_dotenv
import google.genai as genai
from google.genai import types
from google.genai import errors

load_dotenv()

def ask_user(routine) -> list:
    unfinished = []
    for i in range(len(routine)):
        while True:
            print(f"Did you {routine[i]}? [y/n]")
            answer = input().lower().strip()

            if answer in ["y", "n"]:
                break

        if answer == "n":
            unfinished.append(routine[i])
    return unfinished

def generate_punishment(unfinished) -> str:
    read_prompt()
    try:
        client = genai.Client()
        chat = client.chats.create(
            model='gemini-3.6-flash',
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.8
            )
        )

        response = chat.send_message(f"I failed my routine: I didn't do these: {unfinished}.")
        return response.text
    except errors.APIError as err:
        # Handles Google API problems: Bad API keys, Rate limits, Model errors
        print(f"[AI Error] Google AI Studio rejected the request.", file=sys.stderr)
        print(f"Details: {err.message} (Status Code: {err.code})", file=sys.stderr)
        return "Fallback: Go do 15 jumping jacks right now. (AI is offline)"

    except Exception as err:
        print(f"[System Error] Something went wrong locally: {err}", file=sys.stderr)
        return "Fallback: Clean your desk for 2 minutes. (Local connection failure)"

def read_prompt():
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        global system_prompt
        system_prompt = f.read()

routine = ["clean your face", "brush your teeth", "do exercise"]

unfinished = ask_user(routine)
if unfinished:
    print(f"Unfinished routines: {len(unfinished)}")
    for i in range(len(unfinished)):
         print(f"{i + 1}: {unfinished[i]}")

    print("\nGenerating punishment...\n")
    print(generate_punishment(unfinished))
else:
    print("No unfinished routines. Good Job!")
