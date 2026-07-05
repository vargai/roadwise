# Roadwise AI Trip Planner

Open the MVP through the local server:

```powershell
cd C:\Users\varga\Documents\norvegia\version2
python server.py
```

Then open:

```text
http://127.0.0.1:4174
```

The app is a static AI-style road trip planner. It can:

- generate a Norway road trip from a prompt
- accept later conversational adjustments
- review the itinerary day by day
- lock, skip, and reorder stops
- show a route map for the selected day
- switch into a simplified drive mode

The current MVP uses local planning rules and a curated Norway stop library. It is ready to connect to a real AI backend later by replacing the prompt and adjustment functions in `app.js`.
