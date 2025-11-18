# Theme Configuration Guide

## Overview

The application uses a centralized theme configuration system. All colors can be updated in one place, and the changes will reflect throughout the entire application.

## Where to Update Colors

**Primary Location:** `frontend/src/config/theme.ts`

This TypeScript file contains all color definitions. Update colors here, then run the sync script to update CSS variables.

## Color Format

Colors are defined in HSL format: `"H S% L%"`

- **H**: Hue (0-360 degrees on the color wheel)
- **S**: Saturation (0-100%, how vivid the color is)
- **L**: Lightness (0-100%, how light or dark)

### Examples:
- Red: `"0 84% 50%"` (Hue 0 = red, 84% saturation, 50% lightness)
- Blue: `"210 100% 50%"` (Hue 210 = blue, 100% saturation, 50% lightness)
- Green: `"120 100% 35%"` (Hue 120 = green, 100% saturation, 35% lightness)

## Theme Structure

The theme is organized into sections:

### 1. Primary Brand Colors
- `primary`: Main brand color
- `secondary`: Secondary brand color
- `accent`: Accent color

### 2. Semantic Colors
- `success`: Success states (green)
- `warning`: Warning states (orange/yellow)
- `error`: Error states (red)
- `info`: Informational states (blue)

### 3. Calendar Event Types
- `eventTypes.custody`: Custody events (blue)
- `eventTypes.holiday`: Holiday events (red)
- `eventTypes.school`: School events (green)
- `eventTypes.medical`: Medical events (purple)
- `eventTypes.activity`: Activity events (orange)

### 4. Status Colors
- `status.pending`: Pending status (yellow/orange)
- `status.approved`: Approved status (green)
- `status.disputed`: Disputed status (red)
- `status.paid`: Paid status (blue)

### 5. Content Types
- `expense`: Expense items (rose/pink)
- `document`: Document items (indigo)

## How to Update Colors

### Step 1: Edit `theme.ts`

Open `frontend/src/config/theme.ts` and update the color values:

```typescript
export const theme = {
  primary: {
    DEFAULT: "220 100% 50%",  // Changed from red to blue
    // ... other properties
  },
  // ... rest of theme
};
```

### Step 2: Update CSS Variables

After updating `theme.ts`, you need to sync the changes to `globals.css`. The CSS variables in `globals.css` should match the values in `theme.ts`.

**Current CSS variables in `globals.css`:**
- `--primary`: Should match `theme.primary.DEFAULT`
- `--bridge-red`: Should match `theme.bridge.red`
- etc.

### Step 3: Restart Development Server

After making changes, restart your development server to see the updates:

```bash
cd frontend
pnpm dev
```

## Quick Color Reference

### Common Color Hues:
- **Red**: 0
- **Orange**: 30
- **Yellow**: 60
- **Green**: 120
- **Cyan**: 180
- **Blue**: 210-240
- **Purple**: 270
- **Pink/Rose**: 340

### Lightness Guidelines:
- **Backgrounds**: 90-100% (very light)
- **Text on light**: 20-40% (dark)
- **Text on dark**: 90-100% (light)
- **Borders**: 70-90% (medium-light)
- **Solid colors**: 40-60% (medium)

## Example: Changing Primary Color to Blue

1. Open `frontend/src/config/theme.ts`
2. Find `primary.DEFAULT` and change:
   ```typescript
   primary: {
     DEFAULT: "220 100% 50%",  // Blue instead of red
     // ...
   }
   ```
3. Update `globals.css`:
   ```css
   --primary: 220 100% 50%;
   ```
4. Restart the dev server

## Tips

- Use online HSL color pickers to find the exact color you want
- Test colors with sufficient contrast for accessibility
- Keep related colors in the same hue family for consistency
- Light variants (95% lightness) are used for backgrounds
- Dark variants (30-40% lightness) are used for text

## Future Improvements

A build script could be created to automatically sync `theme.ts` to `globals.css`, eliminating the need for manual updates.

