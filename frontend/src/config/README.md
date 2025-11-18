# Theme Configuration

## Quick Start

**To update application colors, edit:** `theme.ts`

All colors are defined in HSL format. After updating `theme.ts`, update the corresponding CSS variables in `globals.css` to match.

## Files

- **`theme.ts`** - Centralized color definitions (EDIT THIS)
- **`THEME_GUIDE.md`** - Detailed guide on how to update colors
- **`globals.css`** - CSS variables (update after changing theme.ts)

## Example: Change Primary Color

1. Open `theme.ts`
2. Find `primary.DEFAULT` and change the value:
   ```typescript
   primary: {
     DEFAULT: "220 100% 50%",  // Change to your desired color
   }
   ```
3. Update `globals.css`:
   ```css
   --primary: 220 100% 50%;
   ```
4. Restart dev server

See `THEME_GUIDE.md` for complete documentation.

