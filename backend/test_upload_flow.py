"""
Test the full PDF upload and parsing flow
Simulates what happens when a user uploads a PDF through the API
"""
import asyncio
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.document_parser import DocumentParser

# Real agreement text
REAL_AGREEMENT = """
ARTICLE I: IDENTIFICATION OF PARTIES

This Marital Settlement Agreement ("Agreement") is entered into by:

Parent 1: Emma Rose Turner
DOB: 06/02/1988
Address: 2145 Maple Ridge Drive, Aurora, CO

Parent 2: Michael Joseph Carter
DOB: 09/17/1986
Address: 118 Westbrook Lane, Aurora, CO

Marriage Date: June 12, 2012
Separation Date: March 4, 2024

Children:
1. Oliver Carter – DOB: 02/11/2016
2. Ava Carter – DOB: 10/05/2020

This Agreement resolves all financial, custodial, and property matters.

ARTICLE II: LEGAL CUSTODY

The parties shall share Joint Legal Custody, giving both parents equal decision-making
authority over:
● Medical and dental care
● Education, tutoring, and special needs services
● Religious upbringing
● Extracurricular activities
● Counseling and mental-health decisions

Both parents shall communicate significant issues within 24 hours.

ARTICLE III: PHYSICAL CUSTODY

The parties agree to a shared physical custody arrangement using a 2-2-3 rotating
schedule, repeating every 14 days.

ARTICLE IV: PARENTING TIME

SCHEDULE (2-2-3 ROTATING)

WEEK 1
● Parent 1:
  ○ Monday & Tuesday
● Parent 2:
  ○ Wednesday & Thursday
● Parent 1:
  ○ Friday, Saturday, Sunday

WEEK 2
● Parent 2:
  ○ Monday & Tuesday
● Parent 1:
  ○ Wednesday & Thursday
● Parent 2:
  ○ Friday, Saturday, Sunday

ARTICLE VI: SUMMER PARENTING TIME

The 2-2-3 rotation continues during summer unless the parents choose to follow a
week-on/week-off plan for smoother scheduling.
"""

async def test_upload_flow():
    print("=" * 70)
    print("🧪 Testing PDF Upload Flow")
    print("=" * 70)
    
    # Simulate what happens in the backend when a file is uploaded
    print("\n1. Simulating file upload...")
    file_content = REAL_AGREEMENT.encode('utf-8')
    file_type = "txt"
    
    # Create parser (without API key, so it uses pattern matching)
    parser = DocumentParser(ai_provider="none")
    
    print("\n2. Parsing document...")
    try:
        result = await parser.parse_document(file_content, file_type)
        
        print("\n3. Parse Results:")
        print("-" * 70)
        print(f"Custody Schedule: {result.get('custodySchedule')}")
        print(f"Custody Arrangement: {result.get('custodyArrangement')}")
        print(f"Holiday Schedule: {result.get('holidaySchedule')}")
        print(f"Decision Making: {result.get('decisionMaking')}")
        print(f"Expense Split: {result.get('expenseSplit')}")
        print(f"Confidence: {result.get('confidence')}")
        
        print("\n4. Verification:")
        print("-" * 70)
        if result.get('custodySchedule') == "2-2-3 schedule":
            print("✅ SUCCESS! Custody schedule correctly identified as '2-2-3 schedule'")
            print("\n📝 To see this result in the UI:")
            print("   1. Click 'Delete' on the existing agreement")
            print("   2. Re-upload the same PDF file")
            print("   3. The new parser will process it with the correct result")
            return True
        else:
            print(f"❌ FAILED! Got '{result.get('custodySchedule')}' instead of '2-2-3 schedule'")
            return False
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_upload_flow())
    sys.exit(0 if success else 1)

