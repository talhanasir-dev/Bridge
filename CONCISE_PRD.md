# Bridge - Concise Product Requirements Document

## 1. Functional Requirements

### 1.1 Calendar Management (High Priority)
- **Live Sync:** Real-time shared calendar showing custody schedule, events, and availability.
- **Smart Swaps:** AI-suggested schedule changes based on availability and fairness.
- **Conflict Detection:** Auto-identification of overlaps (e.g., travel vs. custody time) with resolution prompts.
- **Multi-Device:** Seamless sync across web and mobile.

### 1.2 AI Assistant - "Bridgitte" (High Priority)
- **Proactive Suggestions:** Alerts for conflicts and optimization opportunities before they become issues.
- **Tone Mediation:** "Tone Tuner" to rewrite messages (Matter-of-fact, Friendly, Neutral/Legal).
- **Education:** Context-aware legal and emotional guidance (e.g., "What is a custody violation?").
- **Persona:** Neutral, justice-symbol avatar (scales, covered eyes); supportive and non-judgmental.

### 1.3 Expense Management (Medium Priority)
- **Receipt Scanning:** Auto-categorization of child-related expenses.
- **Flexible Splitting:** Configurable rules (e.g., 60/40, 50/50) based on agreement.
- **Reimbursement:** Tracking of pending, approved, and paid expenses.
- **Reporting:** Exportable history for legal/tax purposes.

### 1.4 Communication Tools (Low Priority)
- **Structured Messaging:** Templates for common interactions (swaps, updates).
- **Immutable Logs:** Tamper-proof record of all messages and actions for court use.
- **Tone Checks:** Warnings for hostile language with "Tone Tuner" options.

### 1.5 Documents & Compliance
- **Agreement Parsing:** AI extracts rules (holidays, rotations) from uploaded custody contracts.
- **Manual Entry:** Option to manually input custody schedules, holidays, and rules if no document is available.
- **Audit Logs:** Court-admissible exports of calendar changes, messages, and expenses.

### 1.6 Dashboard
- **Overview:** Immediate view of "Today," pending requests, and alerts.
- **Insights:** Summary of coparenting patterns and upcoming duties.

## 2. Non-Functional Requirements

- **Security:** SOC2 compliance, end-to-end encryption for messages, immutable audit trails.
- **Performance:** Real-time updates for calendar and messaging.
- **Usability:** Emotionally intelligent design (calming colors, low cognitive load).
- **Reliability:** High availability for critical coordination features.
- **Privacy:** Strict data controls, especially for child data.

## 3. User Flows

### 3.1 Onboarding
1.  **Registration:** Parent 1 creates account -> Generates **Family Code**.
2.  **Linking:** Parent 2 downloads app -> Enters Family Code -> Joins family.
3.  **Setup:**
    *   **Bridgitte Intro:** Explains role and features.
    *   **Personalization:** Role, children's details, tone preferences.
    *   **Contract:** Upload PDF/Image -> AI parses rules -> User verifies.
4.  **Completion:** Dashboard opens with populated schedule.

### 3.2 Daily Management (Core Loop)
1.  **Check Dashboard:** View today's custody status and alerts.
2.  **Action:**
    *   *If Conflict:* Click AI suggestion -> Send Swap Request.
    *   *If Expense:* Snap photo of receipt -> Assign category -> Send for approval.
    *   *If Message:* Type draft -> AI reviews tone -> Send.
3.  **Response:** Co-parent receives notification -> Approves/Declines/Replies.

### 3.3 Conflict Resolution
1.  **Trigger:** System detects potential conflict (e.g., holiday overlap).
2.  **Notification:** "Upcoming weekend overlaps with ex's trip. Propose trade?"
3.  **Proposal:** User selects "Propose Trade" -> AI drafts neutral message.
4.  **Resolution:** Co-parent accepts -> Calendar updates -> Action logged.
