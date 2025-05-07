from http.client import responses

from assistant import handle_input

def main():
    print("Hello Shubham! I'm your personal assistant.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input=input("You:").strip().lower()
        if user_input=="exit":
            print("Assistant: Goodbye! Have a great day")
            break
        response=handle_input(user_input)
        print("Assistant: ",response)

if __name__ == "__main__":
    main()