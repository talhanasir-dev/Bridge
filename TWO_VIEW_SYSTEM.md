# Two-View System: Guest vs Logged-In Users

## Overview

Bridge now has two distinct views based on user authentication status:

1. **Guest View (Landing Page)** - For non-authenticated visitors
2. **Dashboard View (Index)** - For authenticated/logged-in users

This document explains how both views work, what features they show, and how users transition between them.

---

## 🌐 Guest View (Landing Page)

### What Guests See

When users visit Bridge without being logged in, they see a beautiful **Landing Page** showcasing all features according to the PRD.

### Landing Page Sections

#### 1. **Hero Section**
- Welcome message with Bridgette avatar
- "Transform Co-Parenting with Bridge" headline
- Two CTA buttons:
  - **"Start Your Journey"** → Triggers onboarding flow
  - **"I Have an Account"** → Navigates to login page

#### 2. **Key Benefits Cards**
- ⚖️ **Fair & Balanced** - Equitable decisions and transparent tracking
- 🛡️ **Court-Ready Docs** - Comprehensive audit logs
- ❤️ **Child-Focused** - Prioritizing children's best interests

#### 3. **Core Features Section**
Detailed feature cards for:

**Smart Custody Calendar**
- Color-coded events (custody days, holidays, school, medical)
- Shared visibility for both parents
- AI-powered conflict resolution

**Secure Messaging System**
- Tone selection (matter-of-fact, friendly, neutral legal)
- Bridgette mediation and message improvements
- Immutable logging for court documentation

**Expense Tracking & Management**
- Automatic split calculation based on custody agreement
- Receipt management with photo upload
- Structured dispute resolution process

**Document Management & Audit Logs**
- AI parsing of custody agreements
- Comprehensive audit trail
- Printable court-ready documentation

#### 4. **Bridgette AI Section**
Highlights Bridgette's capabilities:
- Guides setup with empathy
- Processes custody agreements
- Provides educational resources and emotional support
- Connects with legal/therapeutic professionals

#### 5. **Dual-Instance Architecture**
Explains how each parent has their own account:
- Parent 1: Creates family, generates Family Code
- Parent 2: Uses code to link and access shared data

#### 6. **Educational Resources**
- Co-parenting tips and legal guidance
- Child psychology resources
- Professional network connections

#### 7. **Footer**
- Links to features, resources, and company info
- Privacy policy and terms

### Landing Page Actions

| Button | Action |
|--------|--------|
| **Get Started Free** | Triggers onboarding flow |
| **Log In** | Navigate to `/login` page |
| **I Have an Account** | Navigate to `/login` page |

---

## 👤 Logged-In View (Dashboard)

### What Authenticated Users See

Once logged in, users see the full **Dashboard** with personalized content and all platform features.

### Header for Logged-In Users

```
┌─────────────────────────────────────────────────────────┐
│ Bridge | Fair & Balanced Co-Parenting                   │
│                                                           │
│ [Right side]                                              │
│  Welcome, John | [Manage Children (2)] | [Settings] | [Logout] │
└─────────────────────────────────────────────────────────┘
```

**Key Differences from Guest View:**
- ✅ Shows personalized greeting: "Welcome, **John**"
- ✅ **Manage Children** button (if family profile exists)
- ✅ **Logout** button (red, clearly visible)
- ❌ No "Create Account" button (already logged in)

### Dashboard Content

1. **Personalized Greeting**
   - "Good morning, **[FirstName]**!" (dynamically fetched from backend)
   - Bridgette's daily message

2. **Family Profile Summary**
   - Family name
   - Number of children
   - Custody arrangement type
   - Special accommodations (e.g., different time zones)

3. **Main Tabs**
   - 📅 **Calendar** - Shared custody calendar
   - 💬 **Messages** - Secure messaging
   - 💰 **Expenses** - Expense tracking
   - 📄 **Documents** - Document management
   - 📚 **Resources** - Educational content

4. **Quick Actions**
   - Schedule Event
   - Send Message
   - Review Expense (with urgent badge)
   - View Documents

5. **Recent Activity**
   - Real-time updates from co-parent
   - Pending approvals
   - Calendar changes

6. **Progress Tracking**
   - Co-parenting balance score
   - Monthly setup completion

---

## 🔄 User Flow: Guest → Logged-In

### Complete Journey

```
┌─────────────────────────────────────────────────────────┐
│  1. GUEST USER                                           │
├─────────────────────────────────────────────────────────┤
│  • Visits website                                        │
│  • Sees Landing Page with all features                  │
│  • Reads about Bridgette, calendar, messaging, etc.     │
│  • Clicks "Get Started Free" or "Start Your Journey"    │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  2. ONBOARDING FLOW (Not yet authenticated)             │
├─────────────────────────────────────────────────────────┤
│  Step 1: Onboarding Explanation                         │
│    → "Start My Journey" or "Skip Preview"               │
│                                                          │
│  Step 2: Account Setup (4 steps)                        │
│    → Basic Info, Contact, Security, Review              │
│    → Backend creates account + auto-login ✅            │
│    → User is NOW AUTHENTICATED                          │
│                                                          │
│  Step 3: Family Code Setup                              │
│    → Generate or Enter Family Code                      │
│                                                          │
│  Step 4: Contract Upload (optional)                     │
│    → Upload custody agreement or skip                   │
│                                                          │
│  Step 5: Family Profile (8 steps)                       │
│    → Family info, parents, children, custody            │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  3. AUTHENTICATED USER                                   │
├─────────────────────────────────────────────────────────┤
│  • Sees Dashboard with personalized greeting            │
│  • "Good morning, John!"                                │
│  • Full access to all features                          │
│  • Logout button visible in header                      │
│  • Can manage children, view calendar, send messages    │
└─────────────────────────────────────────────────────────┘
```

### Returning User Flow

```
┌─────────────────────────────────────────────────────────┐
│  RETURNING USER (Has authToken in localStorage)         │
├─────────────────────────────────────────────────────────┤
│  1. Visits website                                       │
│  2. App checks localStorage for authToken                │
│  3. Token found → setIsAuthenticated(true)              │
│  4. Fetch user profile from backend                     │
│  5. Shows Dashboard directly (NO Landing Page)          │
│  6. Displays: "Good morning, [FirstName]!"              │
└─────────────────────────────────────────────────────────┘
```

---

## 🔐 Authentication Logic

### App.tsx State Management

```javascript
const [isAuthenticated, setIsAuthenticated] = useState(false);
const [showOnboarding, setShowOnboarding] = useState(false);

// On mount: Check for existing token
useEffect(() => {
  const token = localStorage.getItem('authToken');
  if (token) {
    setIsAuthenticated(true);  // Show Dashboard
  }
}, []);

// Routing logic
if (isAuthenticated) {
  return <Index onLogout={handleLogout} />;  // Dashboard
} else if (showOnboarding) {
  return <Index startOnboarding={true} />;   // Onboarding flow
} else {
  return <LandingPage onGetStarted={handleGetStarted} />;  // Guest view
}
```

### Token Management

| Action | localStorage | State | View |
|--------|--------------|-------|------|
| First Visit | No token | `isAuthenticated: false` | Landing Page |
| Click "Get Started" | No token | `showOnboarding: true` | Onboarding |
| Complete Signup | Token stored ✅ | `isAuthenticated: true` | Dashboard |
| Logout | Token removed ❌ | `isAuthenticated: false` | Landing Page |
| Return Visit (logged in) | Token exists ✅ | `isAuthenticated: true` | Dashboard |

---

## 🎨 UI/UX Differences

### Header Comparison

| Element | Guest View | Logged-In View |
|---------|-----------|----------------|
| Logo | ✅ Bridge | ✅ Bridge |
| Tagline | ✅ Fair & Balanced Co-Parenting | ✅ Fair & Balanced Co-Parenting |
| Welcome Message | ❌ | ✅ "Welcome, John" |
| Create Account | ❌ (on Landing) | ❌ |
| Manage Children | ❌ | ✅ (if profile exists) |
| Settings | ❌ | ✅ |
| Login Button | ✅ (top right) | ❌ |
| Get Started Button | ✅ (top right) | ❌ |
| Logout Button | ❌ | ✅ (red, prominent) |

### Content Comparison

| Section | Guest View | Logged-In View |
|---------|-----------|----------------|
| Hero | ✅ Feature showcase | ❌ |
| Bridgette Intro | ✅ AI capabilities | ✅ Daily greeting |
| Features List | ✅ Detailed cards | ❌ |
| Benefits | ✅ 3 key benefits | ❌ |
| Architecture | ✅ Dual-instance explanation | ❌ |
| CTA Buttons | ✅ Get Started, Log In | ❌ |
| Family Profile | ❌ | ✅ Summary card |
| Dashboard Tabs | ❌ | ✅ Full navigation |
| Quick Actions | ❌ | ✅ Interactive cards |
| Recent Activity | ❌ | ✅ Real-time feed |
| Progress Bars | ❌ | ✅ Tracking metrics |

---

## 🧪 Testing the Two-View System

### Test Case 1: Guest User Journey

1. **Open browser in incognito mode** (no saved tokens)
2. **Navigate to** `http://localhost:5137`
3. **Expected**: See Landing Page with:
   - Hero section with Bridgette
   - "Get Started Free" and "Log In" buttons
   - Feature cards (Calendar, Messaging, Expenses, Documents)
   - Bridgette AI section
   - Dual-instance architecture explanation
   - Footer
4. **Action**: Click "Get Started Free"
5. **Expected**: See Onboarding Explanation page
6. **Action**: Complete entire onboarding flow
7. **Expected**: Redirected to Dashboard with personalized greeting

### Test Case 2: Logged-In User

1. **Prerequisites**: Already have an account and logged in
2. **Navigate to** `http://localhost:5137`
3. **Expected**: See Dashboard directly (NOT Landing Page)
4. **Expected**: Header shows:
   - "Welcome, [YourName]"
   - Manage Children button
   - Settings button
   - Logout button (red)
5. **Action**: Click through tabs (Calendar, Messages, Expenses)
6. **Expected**: All features accessible

### Test Case 3: Logout

1. **Prerequisites**: Logged in and on Dashboard
2. **Action**: Click "Logout" button (red, in header)
3. **Expected**: 
   - Toast notification: "Logged out successfully"
   - Redirected to Landing Page
   - authToken removed from localStorage
   - Header shows "Log In" and "Get Started" buttons again

### Test Case 4: Return Visit

1. **Prerequisites**: Previously logged in (token in localStorage)
2. **Close browser and reopen**
3. **Navigate to** `http://localhost:5137`
4. **Expected**: 
   - App checks for token
   - Finds token → auto-login
   - Shows Dashboard directly (skip Landing Page)
   - Fetches and displays user's real name

---

## 📊 PRD Compliance

This two-view system fully complies with the PRD requirements:

### Section 4.1: Onboarding & Account Management ✅
- ✅ Clear entry point for new users (Landing Page)
- ✅ Onboarding flow accessible to guests
- ✅ Dual-instance architecture explained upfront
- ✅ Authentication with token persistence

### Section 5.2: Navigation Flow ✅
- ✅ Welcome Screen (Landing Page) → Account Creation
- ✅ All onboarding steps implemented
- ✅ Dashboard as final destination

### Section 5.3: Key Interface Elements ✅
- ✅ Dashboard for logged-in users
- ✅ Quick Actions (one-tap access)
- ✅ Bridgette presence (both views)
- ✅ Status indicators
- ✅ Progress tracking

---

## 🚀 Key Benefits of Two-View System

### For Bridge

1. **Better Marketing**: Landing Page acts as a marketing tool
2. **Clear Value Prop**: Showcases all features before signup
3. **Reduced Friction**: Users see what they're signing up for
4. **Professional Image**: Modern, polished first impression
5. **SEO Friendly**: Content-rich landing page for search engines

### For Users

1. **Informed Decision**: See all features before committing
2. **Clear Journey**: Understand the onboarding process
3. **No Surprises**: Know what to expect from the platform
4. **Easy Access**: Quick "Get Started" from landing page
5. **Persistent Session**: Stay logged in across visits

### For Guest Users (Non-Authenticated)

1. **Full Feature Overview**: See everything Bridge offers
2. **Educational**: Learn about co-parenting best practices
3. **No Commitment**: Explore without creating account
4. **Social Proof**: See benefits, testimonials, use cases
5. **Multiple Entry Points**: "Get Started" or "Log In"

### For Logged-In Users

1. **Personalized Experience**: Greeted by name
2. **Direct Access**: No landing page friction
3. **Quick Actions**: Immediately access important features
4. **Clear Logout**: Always know how to sign out
5. **Real Data**: See actual family profile and children

---

## 🔧 Technical Implementation

### File Structure

```
frontend/src/
├── App.tsx                    # Routing logic
├── pages/
│   ├── LandingPage.tsx       # Guest view (NEW)
│   ├── Index.tsx             # Dashboard (Updated)
│   ├── Login.tsx             # Login page
│   └── Signup.tsx            # Signup page
└── components/
    ├── OnboardingExplanation.tsx
    ├── AccountSetup.tsx
    ├── FamilyCodeSetup.tsx
    └── ... (other components)
```

### State Flow

```
App.tsx (Top Level)
  ├─ isAuthenticated: boolean
  ├─ showOnboarding: boolean
  ├─ handleLogin() → setIsAuthenticated(true)
  ├─ handleLogout() → setIsAuthenticated(false), remove token
  └─ handleGetStarted() → setShowOnboarding(true)

Index.tsx (Dashboard)
  ├─ Props: onLogout, startOnboarding
  ├─ currentUser: { firstName, lastName, email } | null
  ├─ familyProfile: FamilyProfile | null
  └─ useEffect: Fetch user + family data on mount

LandingPage.tsx (Guest View)
  ├─ Props: onGetStarted
  └─ Showcase all features from PRD
```

---

## 📝 Summary

The two-view system provides:

1. **Guest View (Landing Page)**
   - Feature showcase
   - Educational content
   - Clear CTAs
   - Professional first impression

2. **Logged-In View (Dashboard)**
   - Personalized greeting
   - Full feature access
   - Family data
   - Clear logout option

This architecture creates a professional, user-friendly experience that guides users from discovery → onboarding → daily use, exactly as specified in the PRD.

---

**Last Updated**: Current Date
**Version**: 2.0 (Two-View System)
**PRD Reference**: /frontend/PRD.md

