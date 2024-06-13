# Goal Maker

Summer just started and I'm not good at time management or planning..

So here's the goal maker! Put in activities and weigh them based on how much effort or time an activity will take. It will then make a list of activities for you to do!

### ACTIVITY ATTRIBUTES:

```json
"name": "name of the activity",
"description": "basic description of the activity",
"extras_meta": "the number of extras there are (zero indexed)",
"extras": "allows randomization for activities (see example)",
"extras{n}": "allows even more randomization for activities (see example)",
"weight": "a list of weights related to each extra."
```

### ACTIVITY EXAMPLE:

```json
"name": "Bike",
"description": "Go bike for a bit",
"extras_meta": 1,
"extras": ["on trail 1", "on trail 2"],
"extras1": ["for 30 minutes","for 45 minutes","for an hour"],
"weight": [1,1.5,2]
```

Valid activities from this are:

- Go bike for a bit on trail 1 for 30 minutes (with weight 1)
- Go bike for a bit on trail 1 for 45 minutes (with weight 1.5)
- Go bike for a bit on trail 1 for an hour (with weight 2)

- Go bike for a bit on trail 2 for 30 minutes (with weight 1)
- Go bike for a bit on trail 2 for 45 minutes (with weight 1.5)
- Go bike for a bit on trail 2 for an hour (with weight 2)

### What's a weight?

The more time and/or effort an activity takes, the higher the weight.
In the categories.json file, you can alter the amount of weight you need per category.

Read ahead to learn more.

### CATEGORY ATTRIBUTES:

```json
"category": "The name of the category",
"location": "The location of the activity category file (ending in .json)",
"min": "the minimum possible amount of weight",
"max": "the maximum possible amount of weight"
```

### CATEGORY EXAMPLE:

```json
"category": "Biking",
"location": "biking.json",
"min": 1,
"max": 4
```

Let's say

random.randrange(min,max) returns 2:

This means the program will look for activities in biking.json, and randomly choose activities and extras until the total weight is greater than or equal to 2.

The program might say:

- Go bike for a bit on trail 2 for 30 minutes (with weight 1)

- Go bike for a bit on trail 1 for 30 minutes (with weight 1)

or 

- Go bike for a bit on trail 2 for 30 minutes (with weight 1)

- Go bike for a bit on trail 1 for 45 minutes (with weight 1.5)

etc.

You can always make more activities.json files and add them to your categories.json file!