# Custody Pattern Verification - December 2025

## 2-2-3 Schedule Pattern

### Pattern Definition
The 2-2-3 schedule follows a 14-day repeating pattern:
- **Days 0-1**: Parent 1 (2 days)
- **Days 2-3**: Parent 2 (2 days)
- **Days 4-6**: Parent 1 (3 days)
- **Days 7-8**: Parent 2 (2 days)
- **Days 9-10**: Parent 1 (2 days)
- **Days 11-13**: Parent 2 (3 days)

Pattern Array: `[P1, P1, P2, P2, P1, P1, P1, P2, P2, P1, P1, P2, P2, P2]`

### Reference Date
- **January 1, 2025** is used as the reference date (Day 0)
- This ensures consistent patterns across frontend and backend

---

## December 2025 Expected Pattern

Calculating from January 1, 2025 to December 2025:

### Day Calculations
- Dec 1, 2025 = Day 334 from Jan 1
- 334 % 14 = 12 → Pattern[12] = **Parent 2**

- Dec 2, 2025 = Day 335 from Jan 1
- 335 % 14 = 13 → Pattern[13] = **Parent 2**

- Dec 3, 2025 = Day 336 from Jan 1
- 336 % 14 = 0 → Pattern[0] = **Parent 1**

- Dec 4, 2025 = Day 337 from Jan 1
- 337 % 14 = 1 → Pattern[1] = **Parent 1**

... and so on.

### Full December 2025 Calendar

```
December 2025 - Expected 2-2-3 Pattern
═══════════════════════════════════════════════════════════

Mon      Tue      Wed      Thu      Fri      Sat      Sun
────────────────────────────────────────────────────────────
 1 P2     2 P2     3 P1     4 P1     5 P2     6 P2     7 P2
         (Day 12) (Day 13) (Day 0)  (Day 1)  (Day 2)  (Day 3) (Day 4)

 8 P1     9 P1    10 P1    11 P2    12 P2    13 P1    14 P1
(Day 5)  (Day 6)  (Day 7)  (Day 8)  (Day 9)  (Day 10) (Day 11)

15 P2    16 P2    17 P2    18 P1    19 P1    20 P2    21 P2
(Day 12) (Day 13) (Day 0)  (Day 1)  (Day 2)  (Day 3)  (Day 4)

22 P1    23 P1    24 P1    25 P2    26 P2    27 P1    28 P1
(Day 5)  (Day 6)  (Day 7)  (Day 8)  (Day 9)  (Day 10) (Day 11)

29 P2    30 P2    31 P2
(Day 12) (Day 13) (Day 0)

Legend:
P1 = Parent 1 (mom) - Blue background with dark blue border
P2 = Parent 2 (dad) - Yellow background with bright yellow border
```

### Pattern Verification

**Week 1 (Dec 1-7):**
- Dec 1-2: Parent 2 (last 2 days of previous cycle)
- Dec 3-4: Parent 1 (2 days) ✓
- Dec 5-7: Parent 2 (3 days) ✓

**Week 2 (Dec 8-14):**
- Dec 8-10: Parent 1 (3 days) ✓
- Dec 11-12: Parent 2 (2 days) ✓
- Dec 13-14: Parent 1 (2 days) ✓

**Week 3 (Dec 15-21):**
- Dec 15-17: Parent 2 (3 days) ✓
- Dec 18-19: Parent 1 (2 days) ✓
- Dec 20-21: Parent 2 (2 days) ✓

**Week 4 (Dec 22-28):**
- Dec 22-24: Parent 1 (3 days) ✓
- Dec 25-26: Parent 2 (2 days) ✓
- Dec 27-28: Parent 1 (2 days) ✓

**Week 5 (Dec 29-31):**
- Dec 29-31: Parent 2 (3 days) ✓

---

## Color Coding on Calendar

After the fix, the calendar should show:

### Visual Representation
```
     Mon   Tue   Wed   Thu   Fri   Sat   Sun
    ─────────────────────────────────────────
W1:  🟡    🟡    🔵    🔵    🟡    🟡    🟡
W2:  🔵    🔵    🔵    🟡    🟡    🔵    🔵
W3:  🟡    🟡    🟡    🔵    🔵    🟡    🟡
W4:  🔵    🔵    🔵    🟡    🟡    🔵    🔵
W5:  🟡    🟡    🟡

🔵 = Parent 1 (Light blue background, dark blue border #002f6c)
🟡 = Parent 2 (Light yellow background, bright yellow border #ffc800)
```

---

## Week-on/Week-off Pattern (for comparison)

If the schedule was week-on/week-off instead:

```
December 2025 - Week-on/Week-off Pattern
═══════════════════════════════════════════════════════════

Mon      Tue      Wed      Thu      Fri      Sat      Sun
────────────────────────────────────────────────────────────
 1        2        3        4        5        6        7
Week 48 - Parent 2 (even/odd depends on Jan 1)

 8        9       10       11       12       13       14
Week 49 - Parent 1 (alternates)

15       16       17       18       19       20       21
Week 50 - Parent 2 (alternates)

22       23       24       25       26       27       28
Week 51 - Parent 1 (alternates)

29       30       31
Week 52 - Parent 2 (alternates)
```

---

## Testing Checklist

After the fix, verify:

- [ ] December 1-2 shows Parent 2 (yellow)
- [ ] December 3-4 shows Parent 1 (blue)
- [ ] December 5-7 shows Parent 2 (yellow)
- [ ] December 8-10 shows Parent 1 (blue)
- [ ] December 11-12 shows Parent 2 (yellow)
- [ ] December 13-14 shows Parent 1 (blue)
- [ ] December 15-17 shows Parent 2 (yellow)
- [ ] December 18-19 shows Parent 1 (blue)
- [ ] December 20-21 shows Parent 2 (yellow)
- [ ] December 22-24 shows Parent 1 (blue)
- [ ] December 25-26 shows Parent 2 (yellow)
- [ ] December 27-28 shows Parent 1 (blue)
- [ ] December 29-31 shows Parent 2 (yellow)

### Pattern Check
The 2-2-3 pattern should repeat every 14 days:
- [ ] Days with same position in 14-day cycle show same parent
- [ ] Pattern: 2 days P1, 2 days P2, 3 days P1, 2 days P2, 2 days P1, 3 days P2
- [ ] No "both parents" days (that's not part of 2-2-3)

---

## How to Test

1. **Restart Backend Server**
   ```bash
   cd backend
   .venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Clear Browser Cache** (or hard refresh)
   - Chrome/Edge: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
   - Firefox: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

3. **Delete and Re-create Custody Agreement**
   - Go to Settings → Family
   - Delete existing agreement
   - Create new manual entry with 2-2-3 schedule
   - Save

4. **View Calendar**
   - Navigate to Calendar page
   - Check December 2025
   - Verify pattern matches table above

5. **Navigate Months**
   - Check previous/next months
   - Verify pattern continues consistently
   - Every 14 days should show same pattern

---

## Common Issues & Solutions

### Issue: Pattern doesn't match
**Cause**: Backend events generated before the fix
**Solution**: Delete and recreate the custody agreement

### Issue: Some days show "both" parents
**Cause**: Old 2-2-3 logic marked weekends as "both"
**Solution**: Frontend fix now removes this. Refresh page.

### Issue: Pattern shifts when viewing different months
**Cause**: Reference date not consistent
**Solution**: Now uses Jan 1st as reference for entire year

### Issue: Backend and frontend show different colors
**Cause**: Different calculation methods
**Solution**: Both now use same pattern array and reference date

---

**Fix Applied**: December 1, 2025
**Status**: ✅ Ready for Testing
**Next Step**: Restart servers and test the calendar!

