import asyncio
import os
from services.document_parser import DocumentParser

async def test_parser():
    # Mock text that simulates a PDF extraction
    sample_text = """
    CUSTODY AGREEMENT
    
    1. CUSTODY SCHEDULE
    The parents shall share joint legal custody.
    Physical custody shall be shared as follows:
    - Mother shall have the children on Mondays and Tuesdays.
    - Father shall have the children on Wednesdays and Thursdays.
    - The parents shall alternate weekends (Friday through Sunday).
    
    2. HOLIDAYS
    Holidays shall be alternated each year.
    
    3. EXPENSES
    Father shall pay 60% of agreed upon expenses, and Mother shall pay 40%.
    """
    
    print("Testing DocumentParser with sample text...")
    
    # Initialize parser (mocking API key if needed, or relying on env)
    # For this test, we might hit the API if a key is present, or fallback to patterns.
    # To test the PROMPT update, we ideally need the AI to run.
    
    parser = DocumentParser(ai_provider="openai")
    
    # We can test the _build_parsing_prompt method directly to see if it contains our changes
    prompt = parser._build_parsing_prompt(sample_text)
    
    if "EXPLICITLY state which days belong to which parent" in prompt:
        print("✅ Prompt successfully updated with detailed schedule request.")
    else:
        print("❌ Prompt update NOT found.")
        
    print("\nGenerated Prompt Preview:")
    print(prompt[:500] + "...")

if __name__ == "__main__":
    asyncio.run(test_parser())
