import google.generativeai as genai

API_KEY = "enter-your-gemini-api-key"
genai.configure(api_key=API_KEY)

# Function to generate technical specification
def generate_technical_spec(requirement):
    prompt = f"""
    You're a software architect assistant.
    
    Given the following high-level business requirement, break it down into:
    1. Functional Modules
    2. Suggested Database Schemas (tables and key fields)
    3. Basic Pseudocode for one or more core features

    High-Level Requirement:
    {requirement}

    Provide clear and structured output.
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
# Saving our output to .txt file
def save_output_to_file(requirement, output, filename="output_examples.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write("=====================================\n")
        f.write("High-Level Requirement:\n")
        f.write(requirement + "\n\n")
        f.write("Generated Technical Specification:\n")
        f.write(output + "\n\n")

if __name__ == "__main__":
    # Example 1
    business_idea1 = "Build an app where users can create and share workout plans."
    result1 = generate_technical_spec(business_idea1)
    print(result1)
    save_output_to_file(business_idea1, result1)

    # Example 2
    business_idea2 = "Create a platform where users can browse products, add them to a cart, purchase them, and track their orders."
    result2 = generate_technical_spec(business_idea2)
    print(result2)
    save_output_to_file(business_idea2, result2)
