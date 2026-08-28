# import json
routine = ["clean your face", "brush your teeth", "do exercise"]

def ask_user(routine) -> list:
    unfinished = []
    for i in range(len(routine)):
        print(f"Did you {routine[i]}? [y/n]")
        answer = input().lower().strip()

        if answer not in ["y", "n"]:
            raise SystemExit("Incorrect input. Exiting...")
        if answer == "n":
            unfinished.append(i)
    return unfinished

unfinished = ask_user(routine)
if unfinished:
    print(f"Unfinished routines: {len(unfinished)}:")
    for i in unfinished:
        print(f"{i + 1}: {routine[i]}")
else:
    print("No unfinished routines. Good Job!")
