import re


name_regex = re.compile(r"Agent \w+")
print(name_regex.sub("Khan", "Agent Shahzaib back to Agent Usman"))


agent_regex = re.compile(r"Agent (\w)\w*", re.I)
print(
    agent_regex.sub(
        r"\1***",
        "Agent Shahzaib back to Agent Usman for death of agent Rose which is killed by agent dala",
    )
)
