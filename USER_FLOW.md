# Bridge Co-Parenting Platform - Complete User Flow

This document outlines the complete user flow as implemented according to the PRD.

## 📋 User Flow Overview (Per PRD Section 4.1 & 5.2)

### **Scenario 1: First Parent (Creates Family)**

```
1. Landing/Dashboard → Click "Create Account"
   ↓
2. OnboardingExplanation → "Start My Journey" or "Skip Preview"
   ↓
3. AccountSetup (Multi-step form)
   - Step 1: Basic Info (First Name, Last Name)
   - Step 2: Contact (Email)
   - Step 3: Security (Password)
   - Step 4: Review & Confirm
   - **Backend**: Creates user account + Auto-login
   ↓
4. FamilyCodeSetup (Mode: Create)
   - Click "Generate Family Code"
   - System generates unique 6-character code (e.g., "ABC123")
   - **Backend**: Creates family profile with familyCode
   - Display code for sharing with co-parent
   ↓
5. ContractUpload (Optional)
   - Upload custody agreement (PDF/DOC)
   - **AI Parsing**: Extracts key terms
   - Or click "Skip for Now"
   ↓
6. FamilyOnboarding (Detailed Profile)
   - Family Information
   - Parent 1 Details
   - Parent 2 Details (optional for now)
   - Children Information
   - Custody Arrangement
   - Special Accommodations
   - Review & Complete
   ↓
7. **Dashboard** (Personalized)
   - Shows: "Good morning, [FirstName]!"
   - Family profile summary
   - Children cards
   - Calendar, Messages, Expenses, Documents
```

### **Scenario 2: Second Parent (Joins Existing Family)**

```
1. Landing/Dashboard → Click "Create Account"
   ↓
2. OnboardingExplanation → "Start My Journey"
   ↓
3. AccountSetup (Multi-step form)
   - Same as Parent 1
   - **Backend**: Creates user account + Auto-login
   ↓
4. FamilyCodeSetup (Mode: Join)
   - Click "Already have a Family Code?"
   - Enter 6-character code received from Parent 1
   - **Backend**: Links account to existing family
   - Updates family with parent2_email and parent2_name
   ↓
5. ContractUpload (Skip - already uploaded by Parent 1)
   ↓
6. **Dashboard** (Shared Family View)
   - Shows: "Good morning, [FirstName]!"
   - Same family profile as Parent 1
   - Same children, calendar, etc.
   - **Dual-Instance Architecture**: Each parent has their own view
```

### **Scenario 3: Existing User (Already Logged In)**

```
1. App loads → Checks localStorage for authToken
   ↓
2. If token exists:
   - **Backend**: Fetch user profile via GET /api/v1/auth/me
   - **Backend**: Fetch family profile via GET /api/v1/family
   ↓
3. **Dashboard** (Personalized)
   - Displays actual user name: "Good morning, Sarah!"
   - Shows real family data
   - Shows real children information
   - All features available
```

## 🔄 State Management

### Frontend State Variables
- `showOnboardingExplanation`: Controls welcome screen
- `showAccountSetup`: Controls account creation flow
- `showFamilyCodeSetup`: Controls family code generation/entry
- `showContractUpload`: Controls custody agreement upload
- `showFamilyOnboarding`: Controls detailed family profile setup
- `currentUser`: Stores logged-in user data (firstName, lastName, email)
- `familyProfile`: Stores family data (familyName, children, custody, etc.)
- `tempFamilyData`: Stores intermediate data during onboarding

### Data Flow
```
AccountSetup
  ↓ (passes userData: firstName, lastName, email)
Index.tsx (stores in tempFamilyData)
  ↓ (auto-generates familyName and parent1_name)
FamilyCodeSetup (receives familyName, parent1Name)
  ↓ (creates family in backend, returns familyCode)
ContractUpload (optional)
  ↓ (parses contract, stores in family.custodyAgreement)
FamilyOnboarding (completes profile)
  ↓ (returns full FamilyProfile)
Dashboard (displays personalized view)
```

## 🔐 Authentication Flow

### Signup & Auto-Login
```javascript
// In AccountSetup.tsx (final step)
1. await authAPI.signup({ firstName, lastName, email, password })
2. await authAPI.login(email, password)
3. Token stored in localStorage
4. User redirected to next step
```

### Session Persistence
```javascript
// In Index.tsx (on mount)
useEffect(() => {
  const token = localStorage.getItem('authToken');
  if (token) {
    // Fetch current user
    const user = await authAPI.getCurrentUser();
    setCurrentUser(user);
    
    // Fetch family profile
    const family = await familyAPI.getFamily();
    setFamilyProfile(family);
  }
}, []);
```

## 🎯 Key Features Per PRD

### 4.1 Onboarding & Account Management ✅
- [x] Dual-Instance Architecture (each parent has own account)
- [x] Initial Registration (first parent creates + generates code)
- [x] Partner Connection (second parent uses code to link)
- [x] Authentication (JWT tokens + localStorage)
- [x] Personalization (individual user data)

### 4.2 Bridgette AI Assistant ✅
- [x] Welcome & Onboarding (OnboardingExplanation)
- [x] Contract Processing (ContractUpload with AI parsing)
- [x] Personalized greetings (uses actual user name)

### 4.3 Smart Custody Calendar ✅
- [x] Monthly view
- [x] Shared between parents
- [x] Color-coded events

### 4.4 Secure Messaging System ✅
- [x] Communication hub
- [x] Immutable logging

### 4.5 Expense Tracking ✅
- [x] Category tracking
- [x] Automatic split calculation
- [x] Status management

### 4.6 Document Management ✅
- [x] Contract upload
- [x] AI parsing
- [x] Audit trail

## 🚀 Current Implementation Status

### ✅ Completed
1. Full onboarding flow (Explanation → Account → Family Code → Contract → Profile)
2. Backend API endpoints for all features
3. In-memory database fallback for development
4. Authentication with JWT tokens
5. Family Code generation and linking
6. AI contract parsing (simulated)
7. Dynamic user name display on dashboard
8. Family profile fetching and display

### 🔄 Next Steps (Future Enhancements)
1. Real AI integration for contract parsing
2. MongoDB connection for production
3. Real-time sync between parent instances
4. Push notifications for events
5. Advanced calendar conflict resolution
6. Expense dispute resolution workflow
7. Professional network integration

## 📱 Testing the Flow

### Test Scenario: Complete Onboarding
1. **Start**: Click "Create Account" button in header
2. **Onboarding Explanation**: Click "Start My Journey"
3. **Account Setup**: 
   - Enter: John | Doe
   - Enter: john@example.com
   - Enter: password123
   - Click "Create Account!"
4. **Family Code Setup**: Click "Generate Family Code"
   - Copy the 6-character code
5. **Contract Upload**: Upload PDF or click "Skip for Now"
6. **Family Profile**: Fill in all 8 steps
7. **Dashboard**: See "Good morning, John!"

### Test Scenario: Join as Second Parent
1. **Start**: Click "Create Account"
2. **Account Setup**: Complete as Sarah
3. **Family Code Setup**: Click "Already have code?" → Enter John's code
4. **Dashboard**: See same family profile as John

## 🎨 UI/UX Highlights

- **Modern Design**: Gradient cards, smooth animations
- **Bridgette Avatar**: Animated, friendly AI assistant
- **Progress Tracking**: Step indicators throughout onboarding
- **Color Coding**: Blue (primary), Green (success), Yellow (warning), Red (urgent)
- **Responsive**: Works on all screen sizes
- **Accessible**: Clear labels, keyboard navigation

---

**Last Updated**: [Current Date]
**Version**: 1.0
**PRD Reference**: /frontend/PRD.md

