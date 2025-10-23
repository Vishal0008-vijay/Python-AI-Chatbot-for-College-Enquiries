
import re

# Predefined responses
responses = {
    "courses": "Our college offers B.Tech, M.Tech, MBA, and PhD programs across multiple disciplines.",
    "admission": "You can apply online through our official website. The admission form and details are available there.",
    "fees": "The fee structure varies by program. Please visit the 'Admissions -> Fee Structure' section on our website.",
    "hostel": "Yes, we provide separate hostel facilities for boys and girls with Wi-Fi and mess facilities.",
    "placement": "We have a strong placement record with top recruiters visiting every year.",
    "contact": "You can reach us at contact@college.edu or call +91-9876543210.",
    "default": "I'm sorry, I didn't understand that. Could you please rephrase your question?"
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if re.search(key, user_input):
            return responses[key]
    return responses["default"]

def main():
    print("🤖 Hello! I'm your College Enquiry Chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
