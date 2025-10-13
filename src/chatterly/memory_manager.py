# in-memory "working" and "episodic" stores
working_memory = {}
episodic_memory = []

def add_fact(key, value):
    """Store facts like name, location, hobbies."""
    working_memory[key] = value

def get_fact(key):
    return working_memory.get(key, None)

def get_working_memory():
    return working_memory

def add_episodic(text):
    episodic_memory.append(text)

def get_recent_conversations(n=5):
    return episodic_memory[-n:]
