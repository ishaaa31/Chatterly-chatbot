from chatterly.llm_engines.gemini import generate as gemini_generate

def get_llm_response(prompt, system_prompt=None, engine="gemini"):
    if engine == "gemini":
        return gemini_generate(prompt, system_prompt)
    # i can add other engines here later like Hugging Face, OpenAI
    return "[LLM Error] No valid engine selected."
