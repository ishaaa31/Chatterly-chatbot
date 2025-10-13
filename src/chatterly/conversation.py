from chatterly.llm_engines.llm_router import get_llm_response

def get_bot_reply(user_input, context=None):
    system_prompt = (
        "You are Chatterly, a helpful, witty assistant with access to semantic memory. "
        "Respond clearly, cite memory if available, and maintain a friendly tone."
    )
    if context:
        user_input = context + "\n\nUser: " + user_input
    return get_llm_response(user_input, system_prompt)
