# Manual Custody Entry Feature Guide

## Overview
This feature allows users to manually enter custody agreement information instead of uploading a document. The system provides a user-friendly interface for configuring custody schedules, holiday arrangements, decision-making rules, and expense splits.

## Features Implemented

### 1. **Entry Mode Selection**
- Users can choose between **Upload Document** or **Enter Manually**
- Both options are available from the Family Settings tab

### 2. **Custody Schedule Types**
Users can select from three schedule types:

#### a) **Week-on/Week-off**
- Parents alternate full weeks with the children
- Automatically generates alternating weekly custody events

#### b) **2-2-3 Schedule**
- Parent 1: 2 days, then 2 days later 3 days
- Parent 2: 2 days, then 2 days later 3 days
- 14-day repeating cycle

#### c) **Custom Schedule**
- Select specific days of the week for each parent
- Interactive day-of-week selector with checkboxes
- Mon, Tue, Wed, Thu, Fri, Sat, Sun selection
- Days can overlap if custody is shared

### 3. **Holiday Schedule** (Optional)
- Text area to describe holiday arrangements
- Example: "Thanksgiving alternates yearly. Parent 1 has Christmas Eve."

### 4. **Decision Making** (Optional)
- Text area to describe how major decisions are made
- Example: "Joint decision-making for medical and educational matters."

### 5. **Expense Split Configuration**
Four preset options plus custom:
- **50/50** - Equal split
- **60/40** - One parent pays 60%, other pays 40%
- **70/30** - One parent pays 70%, other pays 30%
- **Custom** - Enter custom percentages for each parent (must total 100%)

### 6. **Edit Existing Agreements**
- Users can edit custody information even after initial setup
- "Edit Info" button available on existing agreements
- Works for both uploaded and manually entered agreements

## User Interface Components

### Location
**Settings → Family Tab → Custody Agreement Section**

### Entry Points
1. **First-time setup**: Two buttons appear:
   - "Upload Agreement" (with upload icon)
   - "Enter Manually" (with edit icon)

2. **Existing agreement**: Action buttons include:
   - "View" (for uploaded documents only)
   - "Edit Info" (for manual updates)
   - "Re-upload" (for document-based agreements)
   - "Delete" (to remove agreement)

### Form Layout
The manual entry form includes:
- **Schedule Type dropdown** - Select custody pattern
- **Custom Days Selector** - Checkboxes for each day (appears for custom schedules)
- **Holiday Schedule** - Multi-line text input
- **Decision Making** - Multi-line text input
- **Expense Split** - Dropdown with presets
- **Custom Split Inputs** - Percentage fields (appears for custom split)
- **Save/Cancel buttons** - Bottom action buttons

### Visual Design
- Clean, modern UI with gradient buttons
- Blue color scheme matching the app's brand
- Helpful tooltips and descriptions
- Validation messages for incorrect inputs
- Loading states during save operations

## Backend Integration

### API Endpoint
```
POST /api/v1/family/custody-manual
```

### Request Body
```json
{
  "custodySchedule": "string",
  "holidaySchedule": "string (optional)",
  "decisionMaking": "string (optional)",
  "expenseSplitRatio": "50-50",
  "expenseParent1": 50,
  "expenseParent2": 50
}
```

### Response
```json
{
  "message": "Custody information saved successfully",
  "custodyAgreement": {
    "uploadDate": "2025-12-01T...",
    "fileName": "Manual Entry",
    "fileType": "manual",
    "custodySchedule": "...",
    "holidaySchedule": "...",
    "decisionMaking": "...",
    "expenseSplit": {...}
  }
}
```

## Automatic Calendar Generation

When custody information is saved (either via upload or manual entry), the system:
1. Stores the agreement in the family profile
2. Generates custody events on the calendar for the next 365 days
3. Colors calendar days based on which parent has custody:
   - **Light Blue** - Parent 1 (Dark Blue border #002f6c)
   - **Light Yellow** - Parent 2 (Bright Yellow border #ffc800)
   - **Light Teal** - Both parents (shared custody days)

## Validation Rules

### Custody Schedule
- For custom schedules: At least one day must be selected
- Week-on/week-off and 2-2-3 don't require additional input

### Expense Split
- Custom splits must total exactly 100%
- Validation error shown if percentages don't add up
- Each parent must have 0-100%

### Optional Fields
- Holiday schedule can be left empty
- Decision making can be left empty

## How to Use

### For Users Creating New Agreement
1. Go to **Settings → Family tab**
2. Scroll to **Custody Agreement** section
3. Click **"Enter Manually"** button
4. Select your custody schedule type
5. If custom, select days for each parent
6. Optionally fill in holiday schedule and decision-making
7. Select expense split ratio
8. Click **"Save Custody Information"**
9. View generated calendar events on the Calendar page

### For Users Updating Existing Agreement
1. Go to **Settings → Family tab**
2. Find the existing **Custody Agreement** card
3. Click **"Edit Info"** button
4. Make desired changes
5. Click **"Save Custody Information"**
6. Calendar events will be regenerated

## Technical Details

### Frontend Files Modified
- `frontend/src/components/UserSettings.tsx` - Added manual entry UI and handlers
- `frontend/src/lib/api.ts` - Already had `saveManualCustody` method

### Backend Files
- `backend/routers/family.py` - Endpoint `/api/v1/family/custody-manual`
- `backend/models.py` - `CustodyManualData` model
- `backend/services/calendar_generator.py` - Generates custody events

### State Management
- `entryMode`: Tracks whether user is uploading or entering manually
- `showManualEntry`: Controls visibility of manual entry form
- `manualData`: Stores form values
- `savingManualEntry`: Loading state during save

## Benefits

1. **Accessibility**: Not everyone has a digital copy of their divorce agreement
2. **Simplicity**: Quick setup without document scanning/uploading
3. **Flexibility**: Easy to update as custody arrangements change
4. **Privacy**: No need to upload sensitive legal documents
5. **Immediate Results**: Calendar events generated instantly

## Future Enhancements (Suggestions)

1. **Schedule Preview**: Show a sample week/month before saving
2. **Import from Calendar**: Parse custody events from existing calendar entries
3. **Multiple Schedules**: Support different schedules for different children
4. **Seasonal Variations**: Different schedules for school year vs. summer
5. **Recurring Exceptions**: Define regular exceptions to the schedule
6. **Template Library**: Pre-built templates for common custody arrangements

## Troubleshooting

### Issue: "Validation Error - Must add up to 100%"
**Solution**: Check custom expense split percentages total exactly 100%

### Issue: Calendar not updating
**Solution**: 
1. Refresh the calendar page
2. Check that custody arrangement is set in Family Profile
3. Verify the agreement saved successfully (look for success toast)

### Issue: No days showing on calendar
**Solution**: 
1. Ensure custody schedule type is selected
2. For custom schedules, make sure days are checked
3. Check that the custody agreement exists in Family Settings

## Testing Checklist

- [ ] Can create new manual custody entry
- [ ] Week-on/week-off schedule generates alternating weeks
- [ ] 2-2-3 schedule follows correct pattern
- [ ] Custom schedule respects selected days
- [ ] Holiday schedule saves and displays correctly
- [ ] Decision-making saves and displays correctly
- [ ] Expense split 50-50 works
- [ ] Expense split 60-40 works
- [ ] Custom expense split validates correctly
- [ ] Edit existing agreement updates data
- [ ] Calendar shows colored custody days
- [ ] Delete agreement removes calendar events
- [ ] Manual entry marked as "Manual Entry" in agreement card
- [ ] Can switch between upload and manual entry modes
- [ ] Form validation shows helpful error messages
- [ ] Loading states display during save operations
- [ ] Success/error toasts appear appropriately

---

**Last Updated**: December 1, 2025
**Feature Status**: ✅ Complete and Ready for Testing

