import json
import os
from dotenv import load_dotenv
import google.genai as genai
from google.genai import types

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
    client = genai.Client()
    system_prompt = (
        "You are 'The Habit Warden,' a witty, slightly sassy AI accountability coach. "
        "The user has failed to complete a routine task. Assign them a minor, funny, "
        "and non-brutal punishment or chore.\n\n"

        "CRITICAL VARIETY RULES:\n"
        "1. NEVER use the 'stand in front of a mirror and apologize' punishment. It is banned.\n"
        "2. You MUST rotate between different punishment styles for every request. "
        "Categories include: Fitness (e.g., 15 squats), Micro-chores (e.g., wipe down one kitchen counter), "
        "or Mindful Actions (e.g. drink a massive glass of water right now).\n"
        "3. Do not suggest physical harm or cold showers. Keep it under 4 sentences."
    )

    chat = client.chats.create(
        model='gemini-3.6-flash',
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.8
        )
    )

    response = chat.send_message(f"I failed my routine: I didn't do these: {unfinished}.")
    return response.text

routine = ["clean your face", "brush your teeth", "do exercise"]

unfinished = ask_user(routine)
if unfinished:
    print(f"Unfinished routines: {len(unfinished)}")
    for i in range(len(unfinished)):
         print(f"{i + 1}: {unfinished[i]}")

    print("Generating punishment...")
    print(generate_punishment(unfinished))
else:
    print("No unfinished routines. Good Job!")
