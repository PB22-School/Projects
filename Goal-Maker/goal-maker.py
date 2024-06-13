import datetime
import json
import random

now = datetime.datetime.now()

# print(f"\nYour goals for {now.month}/{now.day}:")

random.seed(f'{now.day} {now.month} {now.year}')

activities = []

with open("example-categories.json") as f:
    categories = json.load(f)[0]

for category in categories:
    total = random.randrange(int(category["min"]),category["max"])

    if total > 0:

        with open(category["location"]) as f:
            activs = json.load(f)[0]

        while total > 0:
            chosen_activity = activs[random.randint(0,len(activs) - 1)]

            if "extras_meta" in chosen_activity.keys():
                stop_at = chosen_activity["extras_meta"]
            else:
                stop_at = 0
            
            description = chosen_activity["description"]

            if chosen_activity["extras"] == "":
                activities.append(description)
                total -= chosen_activity["weight"]
                continue

            for i in range(stop_at + 1):
                act = chosen_activity["extras" + (str(i) if i != 0 else "")]

                rand = random.randint(0, len(act) - 1)

                if description:
                    description += " " + act[rand]
                else:
                    description = act[rand]

                if i == stop_at:
                    total -= chosen_activity["weight"][rand]

            activities.append(description)
            
random.shuffle(activities)

# for activity in activities:
#     print('\n',activity,'\n')

with open('goals.md', 'w') as f:
    f.write(f"# Your goals for {now.month}/{now.day}, {now.year}:\n\n- ")
    f.write("\n\n- ".join(activities))