import json
import os
from dotenv import load_dotenv
import google.genai as genai
from google.genai import types

load_dotenv()
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

    except Exception as e:
        print(f"[System Error] Something went wrong locally: {err}", file=sys.stderr)
        return "Fallback: Clean your desk for 2 minutes. (Local connection failure)"

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
