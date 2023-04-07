"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["-------.", "omg"],
            "answer": 2,
        },
        {
            "input": [".....-.-----", "morse"],
            "answer": 4,
        },
        {
            "input": ["-..----.......-..-.", "xtmisuf"],
            "answer": 4,
        },
    ],
    "Extra": [
        {
            "input": ["...-----.-..-.-..-..-..-..-..", "vocalnedxi"],
            "answer": 15,
        },
        {
            "input": [".-.----..-.........-.-...-....-", "etaoinshrdlu"],
            "answer": 122,
        },
        {
            "input": [".-..-..-...--........--..-.---.-.--....--...-..--", "rlbzsvxagyiunfw"],
            "answer": 1,
        },
    ]
}
