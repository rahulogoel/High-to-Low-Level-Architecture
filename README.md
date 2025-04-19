# AI-Powered High to Low-Level Architecture Tool
This tool uses Google Gemini (Generative AI) to automatically convert **high-level business requirements** into detailed **low-level technical specifications**, making it easier for product managers, analysts, and developers to align on implementation.

## Features
- Accepts natural language input describing a business idea or system
- Automatically generates:
  - Functional Modules
  - Database Schemas (with key fields)
  - Pseudocode for core features
- Outputs results to console and saves them in a text file (`output_examples.txt`)

## Sample Inputs Used
### Example 1:
**Input:** "Build an app where users can create and share workout plans."

### Example 2:
**Input:** "Create a platform where users can browse products, add them to a cart, purchase them, and track their orders."

Each input produces a detailed breakdown of modules, schemas, and pseudocode, all saved in `output_examples.txt`.

## Tech Stack
- Python
- Google Gemini API (`gemini-2.0-flash`)

## How to Use
1. Install dependencies:
   ```bash
   pip install google-generativeai
   ```
2. Replace `YOUR_GEMINI_API_KEY` in `generate_tech_spec.py` with your Gemini API key.
3. Run the script:
   ```bash
   python generate_tech_spec.py
   ```
4. Check `output_examples.txt` to view saved outputs for each business idea.

## TODOS/Future Improvements
- Better Input Parsing by adding a GUI interface
- Fine-tune the AI model with more domain-specific training examples so that it produces better, more context-aware output.
