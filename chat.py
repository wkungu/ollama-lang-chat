import argparse
from langchain_ollama import ChatOllama


def get_system_prompt(language: str) -> str:
    return f"You are a helpful translator. Translate the user sentence to {language}."


def run_single_prompt(model, temperature, language, text):
    try:
        llm = ChatOllama(
            model=model,
            temperature=temperature,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

        messages = [
            ("system", get_system_prompt(language)),
            ("human", text),
        ]

        ai_msg = llm.invoke(messages)
        print(f"\n🗨️ Translation: {ai_msg.content}\n")

    except Exception as e:
        print(f"❌ Error: {e}")


def chat_loop(model, temperature, language):
    print(f"💬 Enter text to translate to {language} (type 'exit' to quit):\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        run_single_prompt(model, temperature, language, user_input)


def main():
    parser = argparse.ArgumentParser(description="Translate text using LangChain + Ollama")
    parser.add_argument("--model", default="gemma3:1b", help="Model to use (default: gemma3:1b)")
    parser.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature (default: 0.0)")
    parser.add_argument("--language", default="French", help="Target language (default: French)")
    parser.add_argument("--text", help="Text to translate. If omitted, runs in interactive mode.")
    args = parser.parse_args()

    if args.text:
        run_single_prompt(args.model, args.temperature, args.language, args.text)
    else:
        chat_loop(args.model, args.temperature, args.language)


if __name__ == "__main__":
    main()
