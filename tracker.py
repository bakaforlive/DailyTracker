import json
import os
from dotenv import load_dotenv
import google.genai as genai
from google.genai import types

load_dotenv()
client = genai.Client()

routine = ["clean your face", "brush your teeth", "do exercise"]

def ask_user(routine) -> list:
    unfinished = []
    for i in range(len(routine)):
        print(f"Did you {routine[i]}? [y/n]")
        answer = input().lower().strip()

        if answer not in ["y", "n"]:
            raise SystemExit("Incorrect input. Exiting...")
        if answer == "n":
            unfinished.append(routine[i])
    return unfinished

def generate_punishment(unfinished) -> string:
    system_prompt = (
        "You are 'The Habit Warden,' a witty, slightly sassy AI accountability coach. "
        "The user has failed to complete a routine tasks. Assign them a minor, funny, "
        "and non-brutal punishment/chore. Never suggest physical harm, dangerous tasks, "
        "or cold showers. Keep it under 4 sentences."
    )

    chat = client.chats.create(
        model='gemini-3.6-flash',
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.7
        )
    )

    response = chat.send_message(f"I failed my routine: I didn't do these: {unfinished}.")
    return response.text

unfinished = ask_user(routine)
if unfinished:
    print(f"Unfinished routines: {len(unfinished)}")
    for i in range(len(unfinished)):
         print(f"{i + 1}: {unfinished[i]}")

    print("Generating punishment...")
    print(generate_punishment(unfinished))
else:
    print("No unfinished routines. Good Job!")
