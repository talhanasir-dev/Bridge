# Bridge Onboarding Flow - Implementation Guide

## Overview
Complete implementation of the PRD Phase 1 onboarding flow with Family Code system and AI-powered contract parsing.

## New Features Implemented

### 1. Family Code System (PRD 4.1)
**Dual-Instance Architecture** - Each parent maintains their own app instance while sharing core data.

#### First Parent (Creator)
1. Completes account setup
2. System generates unique 6-character Family Code (e.g., `X3KR9Y`)
3. Shares code with co-parent
4. Can proceed with contract upload and family setup

#### Second Parent (Joiner)
1. Creates their own Bridge account
2. Enters Family Code provided by first parent
3. Account automatically links to existing family
4. Gains access to shared calendars, messages, expenses

**Backend Endpoints:**
- `POST /api/v1/family` - Creates family and generates code
- `POST /api/v1/family/link` - Links second parent using code

### 2. AI Contract Parsing (PRD 4.2 & 4.6)
Upload custody agreements and automatically extract:
- Custody split arrangements (50/50, primary/secondary)
- Expense split ratios
- Decision-making terms
- Holiday scheduling patterns
- Legal custody types

**Backend Endpoint:**
- `POST /api/v1/family/contract` - Upload and parse contract
- `GET /api/v1/family/contract` - Get parsed data

**Supported Formats:**
- PDF (.pdf)
- Word Documents (.doc, .docx)
- Text Files (.txt)
- Max file size: 10MB

### 3. Complete Onboarding Flow

```
User Journey:
1. Click "Create Account" button
   ↓
2. OnboardingExplanation (Welcome & feature overview)
   ↓
3. AccountSetup (Personal info, email, password, timezone)
   ↓
4. FamilyCodeSetup (Generate code OR enter existing code)
   ↓
5. ContractUpload (Optional: AI-powered contract parsing)
   ↓
6. FamilyOnboarding (Children info, custody details)
   ↓
7. OnboardingFlow (Platform feature tour)
   ↓
8. Dashboard (Main application)
```

## Frontend Components

### FamilyCodeSetup.tsx
- **Mode: 'create'** - Generates and displays Family Code
- **Mode: 'join'** - Accepts Family Code input
- Auto-copies code to clipboard
- Shows linking instructions
- Animates Bridgette based on state

### ContractUpload.tsx
- File drag-and-drop or click to upload
- Real-time upload progress
- AI parsing simulation with progress bar
- Displays extracted terms with confidence scores
- Skippable (optional step)

## Data Models

### Updated Family Model
```typescript
{
  id: string
  familyName: string
  familyCode: string  // NEW: 6-character unique code
  parent1_email: string
  parent2_email?: string
  parent1_name?: string
  parent2_name?: string
  children: Child[]
  custodyArrangement: string
  custodyAgreement?: {    // NEW
    uploadDate: datetime
    fileName: string
    custodySchedule: string
    holidaySchedule: string
    decisionMaking: string
    expenseSplit: {
      ratio: string
      parent1: number
      parent2: number
    }
    parsedData: {
      confidence: number
      extractedTerms: Array<{
        term: string
        value: string
        confidence: number
      }>
    }
  }
  createdAt: datetime
  linkedAt?: datetime  // When parent2 joined
}
```

## API Usage Examples

### Create Family (First Parent)
```javascript
const response = await familyAPI.createFamily({
  familyName: "Smith Family",
  parent1_name: "John Smith",
  custodyArrangement: "50-50"
});
// Response includes: familyCode (e.g., "X3KR9Y")
```

### Link to Family (Second Parent)
```javascript
const response = await familyAPI.linkToFamily({
  familyCode: "X3KR9Y",
  parent2_name: "Jane Smith"
});
// Links current user as parent2
```

### Upload Contract
```javascript
// Convert file to base64
const reader = new FileReader();
reader.onload = async (e) => {
  const base64 = e.target.result.split(',')[1];
  
  const response = await familyAPI.uploadContract({
    fileName: file.name,
    fileContent: base64,
    fileType: "pdf"
  });
  // Returns parsed data with extracted terms
};
reader.readAsDataURL(file);
```

## Testing the Flow

1. **Start Servers**
   ```bash
   # Backend (in backend directory)
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   
   # Frontend (in frontend directory)
   npm run dev
   ```

2. **Test First Parent Flow**
   - Navigate to http://localhost:5137
   - Click "Create Account"
   - Complete account setup
   - Note the generated Family Code
   - Upload a sample custody agreement (optional)
   - Complete family profile

3. **Test Second Parent Flow**
   - Open incognito/private window
   - Create new account
   - Enter Family Code from step 2
   - Verify linking success

## AI Parsing Simulation

Current implementation simulates AI parsing by detecting patterns:
- "50/50" or "equal time" → 50/50 custody split
- "primary/secondary" → 60/40 split
- "joint legal custody" → Joint legal arrangement
- "alternate holiday" → Alternating holiday schedule

**Production Integration:**
Replace `parse_contract_with_ai()` function in `backend/routers/family.py` with:
- OpenAI GPT-4 API
- Anthropic Claude API
- Specialized legal AI service
- Custom fine-tuned model

## Security Considerations

- Family Codes avoid confusing characters (0, O, I, L, 1)
- Codes are unique and checked against database
- Only one parent2 can link per family
- All contract uploads are stored securely
- Base64 encoding for file transmission
- Authentication required for all endpoints

## Next Steps (Future Enhancements)

1. Add QR code generation for Family Codes
2. SMS/email sharing of Family Codes
3. Real-time AI parsing with streaming updates
4. Multi-document support (upload multiple contracts)
5. Manual questionnaire alternative (no upload)
6. Audit logging for all onboarding actions
7. Family Code expiration and renewal
8. Support for more than 2 parents (complex families)

## Troubleshooting

### Family Code Not Working
- Verify code is exactly 6 characters
- Check for typos (codes are case-insensitive)
- Ensure first parent completed setup
- Confirm family doesn't already have parent2

### Contract Upload Fails
- Check file size (< 10MB)
- Verify file format (PDF, DOC, DOCX, TXT)
- Ensure file is not corrupted
- Check backend logs for parsing errors

### Components Not Rendering
- Verify all imports in Index.tsx
- Check browser console for errors
- Ensure backend is running on port 8000
- Clear browser cache and reload

## Files Modified/Created

### Backend
- ✅ `backend/models.py` - Added Family Code and Contract models
- ✅ `backend/routers/family.py` - Added code generation, linking, and contract endpoints
- ✅ `backend/main.py` - Fixed database boolean check

### Frontend
- ✅ `frontend/src/lib/api.ts` - Added Family Code and contract API methods
- ✅ `frontend/src/components/FamilyCodeSetup.tsx` - NEW component
- ✅ `frontend/src/components/ContractUpload.tsx` - NEW component
- ✅ `frontend/src/pages/Index.tsx` - Integrated new components into flow
- ✅ `frontend/src/pages/Login.tsx` - Added redirect after login
- ✅ `frontend/src/App.tsx` - Added auth persistence

---

**Status: ✅ Phase 1 Onboarding Flow Complete**

All core features from PRD Section 4.1 (Onboarding & Account Management) have been implemented and integrated.


