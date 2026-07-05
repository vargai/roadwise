const PLACE_LIBRARY = [
  { id: "bergen-airport", name: "Bergen Airport", coords: [60.2934, 5.2181], type: "arrival", tags: ["start", "ev"], note: "Pick up the car and start with a full charge." },
  { id: "bergen-airport-ev", name: "Bergen Airport EV Hub", coords: [60.2934, 5.2181], type: "service", tags: ["ev", "airport"], note: "Useful for rental return charge requirements." },
  { id: "bergen", name: "Bergen", coords: [60.3913, 5.3221], type: "city", tags: ["food", "walk"], note: "Compact city stop for dinner, groceries, or a harbor walk." },
  { id: "bergen-ev", name: "Bergen EV Hub", coords: [60.3913, 5.3221], type: "service", tags: ["ev", "food"], note: "Start with a full charge before leaving Bergen." },
  { id: "wergeland-cozy-apartment", name: "Wergeland Cozy Apartment", coords: [60.365833, 5.340383], type: "overnight", tags: ["sleep", "confirmed"], note: "Confirmed Night 1 accommodation in Bergen." },
  { id: "voss", name: "Voss", coords: [60.6297, 6.4147], type: "service", tags: ["ev", "food"], note: "Practical coffee, grocery, and EV charging break." },
  { id: "voss-ev", name: "Voss EV Hub", coords: [60.6297, 6.4147], type: "service", tags: ["ev", "food"], note: "Useful charging/services stop both outbound and on return." },
  { id: "tvindefossen", name: "Tvindefossen", coords: [60.7267, 6.4863], type: "waterfall", tags: ["waterfall", "quick"], note: "Easy waterfall stop right off the route." },
  { id: "gudvangen", name: "Gudvangen", coords: [60.8789, 6.8381], type: "fjord", tags: ["fjord", "scenic"], note: "Short Naeroyfjord photo break if timing is good." },
  { id: "flam", name: "Flam", coords: [60.8611, 7.1133], type: "village", tags: ["fjord", "food", "ev"], note: "Busy but useful fjord base with food and charging." },
  { id: "flam-ev", name: "Flam EV Hub", coords: [60.8611, 7.1133], type: "service", tags: ["ev", "fjord"], note: "Popular area; chargers may be busy in July." },
  { id: "aurland", name: "Aurland", coords: [60.9087, 7.1872], type: "fjord", tags: ["fjord", "base"], note: "Good low-stress base for the Aurlandsfjord area." },
  { id: "aurland-ev", name: "Aurland EV Hub", coords: [60.9087, 7.1872], type: "service", tags: ["ev", "fjord"], note: "Useful if lodging or sightseeing near Aurland." },
  { id: "aurlandsfjord", name: "Aurlandsfjord", coords: [60.9382, 7.0937], type: "fjord", tags: ["fjord", "must"], note: "Main fjord experience near Aurland and Flam." },
  { id: "stegastein", name: "Stegastein Viewpoint", coords: [60.9081, 7.2127], type: "viewpoint", tags: ["viewpoint", "must"], note: "Go early or late for the best chance of calmer crowds." },
  { id: "undredal", name: "Undredal", coords: [60.9506, 7.1026], type: "village", tags: ["fjord", "quiet"], note: "Small fjord village detour for a gentler pace." },
  { id: "laerdalsoyri", name: "Laerdalsoyri", coords: [61.1001, 7.4816], type: "overnight", tags: ["base", "sleep"], note: "Quiet overnight base near Aurland and the fjords." },
  { id: "otthon-laerdalsoyri", name: "Otthon, Laerdalsoyri", coords: [61.1001, 7.4816], type: "overnight", tags: ["sleep", "confirmed"], note: "Confirmed Nights 2-3 accommodation at Bergo 5." },
  { id: "fodnes", name: "Fodnes ferry", coords: [61.1536, 7.2892], type: "ferry", tags: ["ferry"], note: "Useful crossing on the route toward Sogndal and Stryn." },
  { id: "fodnes-mannheller-ferry", name: "Fodnes-Mannheller Ferry", coords: [61.1536, 7.2892], type: "ferry", tags: ["ferry"], note: "Day 4 ferry crossing toward Sogndal and Stryn." },
  { id: "sogndal", name: "Sogndal", coords: [61.2296, 7.1018], type: "service", tags: ["ev", "food"], note: "Reliable services and charging between fjord legs." },
  { id: "sogndal-ev", name: "Sogndal EV Hub", coords: [61.2296, 7.1018], type: "service", tags: ["ev", "food"], note: "Recommended charging and grocery stop on transfer days." },
  { id: "boyabreen", name: "Boyabreen Glacier Viewpoint", coords: [61.4787, 6.7597], type: "glacier", tags: ["glacier", "quick"], note: "A short glacier viewpoint stop with minimal walking." },
  { id: "skei", name: "Skei", coords: [61.5713, 6.4816], type: "service", tags: ["food", "ev"], note: "Useful break before continuing into Nordfjord." },
  { id: "skei-ev", name: "Skei EV Hub", coords: [61.5713, 6.4816], type: "service", tags: ["ev", "food"], note: "Useful before or after the Nordfjord area." },
  { id: "stryn", name: "Stryn", coords: [61.9045, 6.7226], type: "overnight", tags: ["base", "sleep", "ev"], note: "Strong base for Loen, Lovatnet, Olden, and Geiranger options." },
  { id: "stryn-ev", name: "Stryn EV Hub", coords: [61.9045, 6.7226], type: "service", tags: ["ev", "food"], note: "Best practical charging/grocery base around Stryn." },
  { id: "lodgen-stryn", name: "Lodgen Stryn", coords: [61.903567, 6.7227], type: "overnight", tags: ["sleep", "confirmed"], note: "Confirmed Nights 4-6 accommodation at 27 Perhusvegen." },
  { id: "loen", name: "Loen", coords: [61.8714, 6.8453], type: "village", tags: ["scenic", "food"], note: "Good base stop near Lovatnet and the Skylift." },
  { id: "loen-ev", name: "Loen EV Hub", coords: [61.8714, 6.8453], type: "service", tags: ["ev", "scenic"], note: "Useful but do not rely on one charger only." },
  { id: "loen-skylift", name: "Loen Skylift", coords: [61.8696, 6.8491], type: "viewpoint", tags: ["viewpoint", "weather"], note: "Weather-dependent viewpoint; only worth it in clear conditions." },
  { id: "lovatnet", name: "Lovatnet", coords: [61.8106, 6.9312], type: "lake", tags: ["scenic", "lake"], note: "Low-stress scenic drive with excellent photo stops." },
  { id: "briksdal", name: "Briksdal Glacier", coords: [61.6647, 6.8178], type: "hike", tags: ["hike", "glacier"], note: "Main easy active stop if weather and energy are good." },
  { id: "olden", name: "Olden", coords: [61.8364, 6.8064], type: "village", tags: ["food", "scenic"], note: "Convenient food and fjord break near Briksdal." },
  { id: "djupvatnet", name: "Djupvatnet", coords: [62.0158, 7.3082], type: "lake", tags: ["scenic", "quick"], note: "Quick scenic stop on the road toward Geiranger." },
  { id: "dalsnibba", name: "Dalsnibba", coords: [62.0489, 7.2709], type: "viewpoint", tags: ["viewpoint", "weather"], note: "Only worth keeping in clear weather." },
  { id: "geiranger", name: "Geiranger", coords: [62.1015, 7.2051], type: "fjord", tags: ["fjord", "must"], note: "Classic fjord village; keep the stop brief in peak season." },
  { id: "geiranger-ev", name: "Geiranger EV Hub", coords: [62.1015, 7.2051], type: "service", tags: ["ev", "backup"], note: "Backup only; small tourist village chargers may be busy." },
  { id: "flydalsjuvet", name: "Flydalsjuvet", coords: [62.0934, 7.2287], type: "viewpoint", tags: ["viewpoint", "must"], note: "Classic Geiranger viewpoint." },
  { id: "geiranger-ferry-pier", name: "Geiranger Ferry Pier", coords: [62.1011, 7.2072], type: "ferry", tags: ["ferry", "fjord"], note: "Vehicle ferry start; arrive with booking buffer." },
  { id: "geiranger-hellesylt-ferry", name: "Geiranger-Hellesylt Ferry", coords: [62.1011, 7.2072], type: "ferry", tags: ["ferry", "fjord"], note: "Classic fjord ferry leg; book in advance in July." },
  { id: "geiranger-hellesylt-ferry-start", name: "Geiranger-Hellesylt Ferry Start", coords: [62.1011, 7.2072], type: "ferry", tags: ["ferry", "fjord"], note: "Start point for the Geiranger-Hellesylt ferry." },
  { id: "hellesylt", name: "Hellesylt", coords: [62.0858, 6.8673], type: "ferry", tags: ["ferry", "waterfall"], note: "Ferry arrival side with a compact waterfall stop." },
  { id: "hellesylt-ferry-arrival", name: "Hellesylt Ferry Arrival", coords: [62.0856, 6.8667], type: "ferry", tags: ["ferry"], note: "Arrival side after the Geiranger-Hellesylt ferry." },
  { id: "hella-ferry-pier", name: "Hella Ferry Pier", coords: [61.1848, 6.6549], type: "ferry", tags: ["ferry"], note: "Hella side of the Hella-Vangsnes ferry." },
  { id: "hella-vangsnes-ferry", name: "Hella-Vangsnes Ferry", coords: [61.1848, 6.6549], type: "ferry", tags: ["ferry"], note: "Preferred scenic return crossing before Vikafjell." },
  { id: "vangsnes-ferry-pier", name: "Vangsnes Ferry Pier", coords: [61.1738, 6.6456], type: "ferry", tags: ["ferry"], note: "Vangsnes arrival side toward Vik." },
  { id: "vangsnes-ferry-arrival", name: "Vangsnes Ferry Arrival", coords: [61.1738, 6.6456], type: "ferry", tags: ["ferry"], note: "Arrival side for the Hella-Vangsnes crossing." },
  { id: "vik-i-sogn", name: "Vik i Sogn", coords: [61.0879, 6.5797], type: "village", tags: ["break", "scenic"], note: "Short break before Vikafjell; skip if running late." },
  { id: "vik-ev", name: "Vik EV Hub", coords: [61.0879, 6.5797], type: "service", tags: ["ev", "backup"], note: "Backup only; plan main Day 7 charging in Sogndal or Voss." },
  { id: "hopperstad-stave-church", name: "Hopperstad Stave Church", coords: [61.0758, 6.5796], type: "viewpoint", tags: ["culture", "optional"], note: "Optional cultural stop near Vik; skip if the return day is late." },
  { id: "vikafjellet", name: "Vikafjellet scenic road", coords: [60.7925, 6.5085], type: "scenic road", tags: ["scenic", "mountain"], note: "Use in good weather for a different return route." },
  { id: "vikafjellsvegen", name: "Vikafjellsvegen (Rv13) / Vikafjellet", coords: [60.7925, 6.5085], type: "scenic road", tags: ["scenic", "mountain"], note: "Scenic mountain road section; use only in good conditions." },
  { id: "forde", name: "Forde", coords: [61.4522, 5.8572], type: "service", tags: ["ev", "food", "backup"], note: "Practical services stop on the E39 backup route." },
  { id: "lavik-ferry-pier", name: "Lavik Ferry Pier", coords: [61.104, 5.5136], type: "ferry", tags: ["ferry", "backup"], note: "E39 backup ferry start toward Oppedal." },
  { id: "lavik-oppedal-ferry", name: "Lavik-Oppedal Ferry", coords: [61.104, 5.5136], type: "ferry", tags: ["ferry", "backup"], note: "Safer E39 backup ferry route toward Vaksdal/Bergen." },
  { id: "oppedal-ferry-pier", name: "Oppedal Ferry Pier", coords: [61.0732, 5.4748], type: "ferry", tags: ["ferry", "backup"], note: "Oppedal arrival side on the E39 backup route." },
  { id: "oppedal-ferry-arrival", name: "Oppedal Ferry Arrival", coords: [61.0732, 5.4748], type: "ferry", tags: ["ferry", "backup"], note: "Arrival side after Lavik-Oppedal ferry." },
  { id: "vaksdal", name: "Vaksdal", coords: [60.4764, 5.7404], type: "overnight", tags: ["sleep", "base"], note: "Easy final overnight within reach of Bergen." },
  { id: "otthon-vaksdal", name: "Otthon, Vaksdal kommune", coords: [60.4764, 5.7404], type: "overnight", tags: ["sleep", "confirmed"], note: "Confirmed final-night accommodation at Tveitane 43." },
];

const COLORS = {
  arrival: "#1f6fb2",
  city: "#455a64",
  service: "#178f77",
  waterfall: "#1f6fb2",
  fjord: "#0b6b63",
  village: "#27864f",
  viewpoint: "#ba3f2f",
  overnight: "#7a5aa6",
  ferry: "#a86d16",
  glacier: "#607d8b",
  hike: "#ba3f2f",
  lake: "#1f8f9d",
  "scenic road": "#0b6b63",
};

const SAMPLE_PROMPT = "Plan a 7 day Norway road trip from Bergen to Bergen with scenic fjord roads, waterfalls, easy hikes, EV charging, cozy overnight bases, and no more than 4 hours driving per day.";

const PLAN_TEMPLATES = [
  ["bergen-airport", "bergen"],
  ["bergen", "voss", "tvindefossen", "gudvangen", "aurland", "laerdalsoyri"],
  ["laerdalsoyri", "stegastein", "aurland", "flam", "undredal", "laerdalsoyri"],
  ["laerdalsoyri", "fodnes", "sogndal", "boyabreen", "skei", "stryn"],
  ["stryn", "loen", "lovatnet", "briksdal", "loen-skylift", "olden", "stryn"],
  ["stryn", "dalsnibba", "flydalsjuvet", "geiranger", "hellesylt", "stryn"],
  ["lodgen-stryn", "skei", "sogndal", "hella-ferry-pier", "vangsnes-ferry-pier", "vik-i-sogn", "vikafjellsvegen", "voss", "otthon-vaksdal"],
  ["vaksdal", "bergen-airport"],
];

const DAY_ALTERNATIVES = {
  7: [
    {
      id: "backup-e39",
      title: "Backup E39 route",
      summary: "Safer, less scenic return if Vikafjell weather or road conditions are poor.",
      stopIds: ["lodgen-stryn", "skei", "forde", "lavik-ferry-pier", "oppedal-ferry-pier", "otthon-vaksdal"],
    },
  ],
};

const STORAGE_KEY = "roadwise-ai-trip-v3";

const state = {
  plan: null,
  editMode: false,
  activeAlternativeId: null,
  selectedDay: 1,
  markers: new Map(),
  routeLines: [],
  routeRenderToken: 0,
};

const roadRouteCache = new Map();

const els = {
  adjustForm: document.querySelector("#adjustForm"),
  adjustInput: document.querySelector("#adjustInput"),
  appShell: document.querySelector("#appShell"),
  backupRouteBar: document.querySelector("#backupRouteBar"),
  chatLog: document.querySelector("#chatLog"),
  dayCount: document.querySelector("#dayCount"),
  dayDetail: document.querySelector("#dayDetail"),
  daySelect: document.querySelector("#daySelect"),
  dayTabs: document.querySelector("#dayTabs"),
  driveCount: document.querySelector("#driveCount"),
  driveMode: document.querySelector("#driveMode"),
  driveModeToggle: document.querySelector("#driveModeToggle"),
  editModeButton: document.querySelector("#editModeButton"),
  fitMapButton: document.querySelector("#fitMapButton"),
  generateButton: document.querySelector("#generateButton"),
  labelsToggle: document.querySelector("#labelsToggle"),
  mapStatus: document.querySelector("#mapStatus"),
  nextStopName: document.querySelector("#nextStopName"),
  replanTodayButton: document.querySelector("#replanTodayButton"),
  routeToggle: document.querySelector("#routeToggle"),
  sampleButton: document.querySelector("#sampleButton"),
  skipNextButton: document.querySelector("#skipNextButton"),
  stopCount: document.querySelector("#stopCount"),
  toast: document.querySelector("#toast"),
  tripPrompt: document.querySelector("#tripPrompt"),
  tripScore: document.querySelector("#tripScore"),
  tripTitle: document.querySelector("#tripTitle"),
};

const map = createMap(document.querySelector("#map"));

try {
  init();
} catch (error) {
  console.error(error);
  localStorage.removeItem(STORAGE_KEY);
  state.plan = generatePlan(SAMPLE_PROMPT);
  renderFallbackError(error);
  render();
}

function init() {
  bindEvents();
  const saved = loadSavedPlan();
  const prompt = els.tripPrompt.value || SAMPLE_PROMPT;
  try {
    state.plan = ensureUsablePlan(saved ? normalizePlan(saved) : generatePlan(prompt), saved?.prompt || prompt);
  } catch (error) {
    console.warn("Saved trip could not be loaded; regenerating default plan.", error);
    localStorage.removeItem(STORAGE_KEY);
    state.plan = generatePlan(prompt);
  }
  addMessage("assistant", saved ? "Loaded your saved trip. Switch to edit mode to adjust it." : "I drafted a Norway road trip from your prompt. Switch to edit mode when you want to change the plan.");
  render();
}

function bindEvents() {
  els.generateButton.addEventListener("click", () => {
    if (!state.editMode) return;
    state.plan = generatePlan(els.tripPrompt.value);
    state.selectedDay = 1;
    state.activeAlternativeId = null;
    addMessage("user", els.tripPrompt.value);
    addMessage("assistant", "Generated a reviewable road trip with day-by-day stops, pacing notes, and route map.");
    persist();
    render();
  });
  els.sampleButton.addEventListener("click", () => {
    if (!state.editMode) return;
    els.tripPrompt.value = SAMPLE_PROMPT;
    showToast("Sample prompt loaded.");
  });
  els.adjustForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!state.editMode) return;
    const text = els.adjustInput.value.trim();
    if (!text) return;
    els.adjustInput.value = "";
    addMessage("user", text);
    const response = applyAdjustment(text);
    addMessage("assistant", response);
    persist();
    render();
  });
  els.editModeButton.addEventListener("click", () => {
    state.editMode = !state.editMode;
    showToast(state.editMode ? "Editing enabled." : "Review-only mode enabled.");
    render();
  });
  els.daySelect.addEventListener("change", () => {
    state.selectedDay = Number(els.daySelect.value) || 1;
    state.activeAlternativeId = null;
    render();
  });
  [els.routeToggle, els.labelsToggle, els.driveModeToggle].forEach((input) => {
    input.addEventListener("change", render);
  });
  els.fitMapButton.addEventListener("click", fitMap);
  els.skipNextButton.addEventListener("click", () => {
    if (!state.editMode) return;
    const day = currentDay();
    if (!day || day.stops.length < 2) return;
    const skipped = day.stops.find((stop) => !stop.locked && stop.kind !== "overnight") || day.stops[1];
    removeStop(day.id, skipped.instanceId);
    addMessage("assistant", `Skipped ${skipped.name} and tightened today's route.`);
    persist();
    render();
  });
  els.replanTodayButton.addEventListener("click", () => {
    if (!state.editMode) return;
    const response = makeDayEasier(state.selectedDay);
    addMessage("assistant", response);
    persist();
    render();
  });
}

function generatePlan(prompt) {
  const preferences = parsePrompt(prompt);
  const templates = PLAN_TEMPLATES.slice(0, clamp(preferences.days, 2, PLAN_TEMPLATES.length));
  const days = templates.map((ids, index) => createDay(ids, index + 1, preferences));
  attachDayAlternatives(days, preferences);
  if (preferences.avoidFerries) removeFerries(days, preferences);
  if (preferences.waterfalls) ensureTaggedStop(days, "waterfall");
  if (preferences.easy || preferences.maxDriveHours <= 3.5) {
    days.forEach((day) => {
      if (day.driveHours > preferences.maxDriveHours) softenDay(day, preferences, preferences.maxDriveHours);
    });
  }

  return {
    title: titleFromPreferences(preferences),
    prompt,
    preferences,
    days,
    createdAt: new Date().toISOString(),
  };
}

function parsePrompt(prompt) {
  const text = prompt.toLowerCase();
  const daysMatch = text.match(/(\d+)\s*(?:day|days)/);
  const maxDriveMatch = text.match(/(?:max|maximum|no more than|under|less than)\s*(\d+(?:\.\d+)?)\s*(?:h|hr|hour|hours)/);
  return {
    days: daysMatch ? Number(daysMatch[1]) : 7,
    maxDriveHours: maxDriveMatch ? Number(maxDriveMatch[1]) : 4,
    waterfalls: /waterfall|waterfalls/.test(text),
    scenic: /scenic|fjord|viewpoint|mountain/.test(text),
    easy: /easy|relaxed|gentle|slow|less intense/.test(text),
    ev: /ev|charging|electric/.test(text),
    avoidFerries: /avoid ferr/.test(text),
    food: /food|restaurant|lunch|dinner|bakery/.test(text),
  };
}

function createDay(ids, dayNumber, preferences) {
  const stops = ids.map((id, index) => makeStop(id, dayNumber, index + 1));
  const driveHours = estimateDriveHours(stops);
  return {
    id: dayNumber,
    title: dayTitle(stops, dayNumber),
    summary: summarizeDay(stops, preferences),
    driveHours,
    stops,
  };
}

function attachDayAlternatives(days, preferences) {
  days.forEach((day) => {
    const alternatives = DAY_ALTERNATIVES[day.id] || [];
    day.alternatives = alternatives.map((alternative) => {
      const stops = alternative.stopIds.map((id, index) => makeStop(id, `${day.id}-${alternative.id}`, index + 1));
      return {
        id: alternative.id,
        title: alternative.title,
        summary: alternative.summary,
        driveHours: estimateDriveHours(stops),
        stops,
      };
    });
    day.summary = summarizeDay(day.stops, preferences);
  });
}

function normalizePlan(plan) {
  const preferences = plan.preferences || parsePrompt(plan.prompt || SAMPLE_PROMPT);
  if (!Array.isArray(plan.days) || plan.days.length === 0) {
    return generatePlan(plan.prompt || SAMPLE_PROMPT);
  }
  plan.preferences = preferences;
  plan.days = (plan.days || []).map((day) => {
    day.stops = (day.stops || []).map((stop, index) => ({
      ...stop,
      order: index + 1,
      instanceId: stop.instanceId || `${day.id}-${index + 1}-${stop.id}`,
      kind: stop.kind || stop.type,
    }));
    recalcDayWithPreferences(day, preferences);
    return day;
  });
  attachDayAlternatives(plan.days, preferences);
  return plan;
}

function ensureUsablePlan(plan, fallbackPrompt = SAMPLE_PROMPT) {
  if (!plan || !Array.isArray(plan.days) || plan.days.length === 0) {
    localStorage.removeItem(STORAGE_KEY);
    return generatePlan(fallbackPrompt || SAMPLE_PROMPT);
  }
  return plan;
}

function makeStop(id, dayNumber, order) {
  const place = PLACE_LIBRARY.find((item) => item.id === id);
  if (!place) {
    return {
      id,
      name: id.replace(/-/g, " "),
      coords: [61.25, 6.65],
      type: "unknown",
      tags: [],
      note: "This stop is missing from the place library.",
      instanceId: `${dayNumber}-${order}-${id}`,
      order,
      locked: false,
      kind: "unknown",
    };
  }
  return {
    ...place,
    instanceId: `${dayNumber}-${order}-${place.id}`,
    order,
    locked: place.tags.includes("sleep") || place.tags.includes("start"),
    kind: place.type,
  };
}

function dayTitle(stops, dayNumber) {
  const first = stops[0]?.name || "Start";
  const last = stops[stops.length - 1]?.name || "Finish";
  if (dayNumber === 1) return "Arrival and settle in";
  if (first === last) return `${first} local loop`;
  return `${first} to ${last}`;
}

function summarizeDay(stops, preferences) {
  const tags = new Set(stops.flatMap((stop) => stop.tags));
  const pieces = [];
  if (tags.has("fjord")) pieces.push("fjord time");
  if (tags.has("waterfall")) pieces.push("waterfall stop");
  if (tags.has("ev") && preferences.ev) pieces.push("charging options");
  if (tags.has("hike")) pieces.push("easy active stop");
  if (tags.has("ferry")) pieces.push("ferry timing");
  return pieces.length ? pieces.join(", ") : "simple transfer day";
}

function titleFromPreferences(preferences) {
  if (preferences.scenic && preferences.easy) return "Relaxed Norway fjord loop";
  if (preferences.scenic) return "Scenic Norway road trip";
  return "AI road trip itinerary";
}

function applyAdjustment(text) {
  const lower = text.toLowerCase();
  if (!state.plan) return "Generate a trip first, then I can adjust it.";
  if (/avoid ferr/.test(lower)) {
    state.plan.preferences.avoidFerries = true;
    removeFerries(state.plan.days);
    return "Removed ferry-dependent stops where possible and kept the route on road-first alternatives.";
  }
  if (/waterfall|falls/.test(lower)) {
    const added = ensureTaggedStop(state.plan.days, "waterfall");
    return added ? `Added ${added.name} as a waterfall stop.` : "The plan already has waterfall coverage.";
  }
  if (/easy|easier|less intense|relax|slow|tired|running late|late/.test(lower)) {
    const dayMatch = lower.match(/day\s*(\d+)/);
    return makeDayEasier(dayMatch ? Number(dayMatch[1]) : state.selectedDay);
  }
  if (/ev|charg/.test(lower)) {
    const added = ensureTaggedStop(state.plan.days, "ev");
    return added ? `Added ${added.name} to improve charging coverage.` : "The trip already includes practical EV charging breaks.";
  }
  if (/food|lunch|dinner|bakery|coffee/.test(lower)) {
    const added = ensureTaggedStop(state.plan.days, "food");
    return added ? `Added ${added.name} as a practical food break.` : "Food-friendly stops are already built into the visible route.";
  }
  if (/scenic|viewpoint|fjord/.test(lower)) {
    const added = ensureTaggedStop(state.plan.days, "viewpoint") || ensureTaggedStop(state.plan.days, "fjord");
    return added ? `Added ${added.name} for more scenic value.` : "The route is already weighted toward fjords and viewpoints.";
  }
  if (/rest day|day off/.test(lower)) {
    const day = currentDay();
    day.stops = day.stops.filter((stop, index) => index === 0 || index === day.stops.length - 1 || stop.locked);
    recalcDay(day);
    return `Converted Day ${day.id} into a lighter rest day around ${day.stops[0].name}.`;
  }
  return "I treated that as a pacing request and made the selected day easier. Try specific edits like add waterfall, avoid ferries, or make day 4 less intense.";
}

function makeDayEasier(dayId) {
  const day = state.plan.days.find((item) => item.id === dayId) || currentDay();
  if (!day) return "Pick a day first.";
  const optional = [...day.stops].reverse().find((stop, index) => {
    const originalIndex = day.stops.length - 1 - index;
    return !stop.locked && originalIndex !== 0 && originalIndex !== day.stops.length - 1;
  });
  if (!optional) return `Day ${day.id} is already trimmed to the essentials.`;
  removeStop(day.id, optional.instanceId);
  return `Removed ${optional.name} from Day ${day.id} to reduce decision load and driving pressure.`;
}

function ensureTaggedStop(days, tag) {
  if (days.some((day) => day.stops.some((stop) => stop.tags.includes(tag)))) return null;
  const candidate = PLACE_LIBRARY.find((place) => place.tags.includes(tag) && !days.some((day) => day.stops.some((stop) => stop.id === place.id)));
  if (!candidate) return null;
  const day = days[Math.min(days.length - 1, Math.max(1, state.selectedDay - 1))];
  const insertAt = Math.max(1, day.stops.length - 1);
  day.stops.splice(insertAt, 0, makeStop(candidate.id, day.id, insertAt + 1));
  reorderStops(day);
  recalcDay(day);
  return candidate;
}

function removeFerries(days, preferences = state.plan?.preferences || parsePrompt(SAMPLE_PROMPT)) {
  days.forEach((day) => {
    day.stops = day.stops.filter((stop) => stop.locked || !stop.tags.includes("ferry"));
    recalcDay(day, preferences);
  });
}

function softenDay(day, preferences = state.plan?.preferences || parsePrompt(SAMPLE_PROMPT), maxDriveHours = preferences.maxDriveHours || 4) {
  while (day.stops.length > 4 && day.driveHours > maxDriveHours) {
    let index = -1;
    for (let stopIndex = day.stops.length - 2; stopIndex > 0; stopIndex -= 1) {
      if (!day.stops[stopIndex].locked) {
        index = stopIndex;
        break;
      }
    }
    if (index < 0) break;
    day.stops.splice(index, 1);
    recalcDay(day, preferences);
  }
}

function removeStop(dayId, instanceId) {
  const day = state.plan.days.find((item) => item.id === dayId);
  if (!day) return;
  day.stops = day.stops.filter((stop) => stop.instanceId !== instanceId || stop.locked);
  reorderStops(day);
  recalcDay(day);
}

function moveStop(dayId, instanceId, direction) {
  const day = state.plan.days.find((item) => item.id === dayId);
  const index = day?.stops.findIndex((stop) => stop.instanceId === instanceId) ?? -1;
  const nextIndex = index + direction;
  if (!day || index < 0 || nextIndex < 0 || nextIndex >= day.stops.length) return;
  const [stop] = day.stops.splice(index, 1);
  day.stops.splice(nextIndex, 0, stop);
  reorderStops(day);
  recalcDay(day);
  persist();
  render();
}

function toggleLock(dayId, instanceId) {
  const stop = state.plan.days.find((day) => day.id === dayId)?.stops.find((item) => item.instanceId === instanceId);
  if (!stop) return;
  stop.locked = !stop.locked;
  persist();
  render();
}

function reorderStops(day) {
  day.stops.forEach((stop, index) => {
    stop.order = index + 1;
    stop.instanceId = `${day.id}-${index + 1}-${stop.id}`;
  });
}

function recalcDay(day, preferences = state.plan?.preferences || parsePrompt(SAMPLE_PROMPT)) {
  recalcDayWithPreferences(day, preferences);
}

function recalcDayWithPreferences(day, preferences) {
  day.driveHours = estimateDriveHours(day.stops);
  day.title = dayTitle(day.stops, day.id);
  day.summary = summarizeDay(day.stops, preferences);
}

function estimateDriveHours(stops) {
  if (stops.length < 2) return 0;
  const km = stops.slice(1).reduce((sum, stop, index) => sum + haversineKm(stops[index].coords, stop.coords), 0);
  return Math.round((km / 58) * 10) / 10;
}

function render() {
  if (!state.plan) return;
  state.plan = ensureUsablePlan(state.plan, els.tripPrompt.value || SAMPLE_PROMPT);
  try {
    renderMode();
    renderSummary();
    renderDayControls();
    renderBackupRouteBar();
    renderDayDetail();
    renderDriveMode();
    renderMap();
  } catch (error) {
    console.error(error);
    renderFallbackError(error);
  }
}

function renderFallbackError(error) {
  els.appShell.classList.remove("read-only");
  els.dayDetail.innerHTML = `
    <article class="day-card">
      <div>
        <p class="eyebrow">Recovery mode</p>
        <h3>The itinerary had trouble loading</h3>
        <p class="day-meta">The app regenerated a clean default plan. Refresh once more if the map is still blank.</p>
      </div>
      <p class="stop-note">${escapeHtml(error?.message || "Unknown rendering error")}</p>
    </article>
  `;
}

function renderMode() {
  els.appShell.classList.toggle("read-only", !state.editMode);
  els.appShell.classList.toggle("edit-mode", state.editMode);
  els.editModeButton.textContent = state.editMode ? "Done" : "Edit trip";
  els.editModeButton.setAttribute("aria-pressed", String(state.editMode));
  els.tripPrompt.disabled = !state.editMode;
  els.adjustInput.disabled = !state.editMode;
  els.generateButton.disabled = !state.editMode;
  els.sampleButton.disabled = !state.editMode;
}

function renderSummary() {
  const days = state.plan.days;
  const stops = days.flatMap((day) => day.stops);
  const avgDrive = days.length ? days.reduce((sum, day) => sum + day.driveHours, 0) / days.length : 0;
  els.tripTitle.textContent = state.plan.title;
  els.dayCount.textContent = String(days.length);
  els.stopCount.textContent = String(stops.length);
  els.driveCount.textContent = `${Math.round(avgDrive * 10) / 10}h`;

  const hardest = Math.max(...days.map((day) => day.driveHours));
  els.tripScore.classList.remove("warning", "alert");
  if (hardest > state.plan.preferences.maxDriveHours + 1) {
    els.tripScore.textContent = "Heavy day";
    els.tripScore.classList.add("alert");
  } else if (hardest > state.plan.preferences.maxDriveHours) {
    els.tripScore.textContent = "Watch pace";
    els.tripScore.classList.add("warning");
  } else {
    els.tripScore.textContent = "Balanced";
  }
}

function renderDayControls() {
  els.dayTabs.innerHTML = "";
  els.daySelect.innerHTML = "";
  state.plan.days.forEach((day) => {
    const tab = document.createElement("button");
    tab.className = `chip-button${day.id === state.selectedDay && !state.activeAlternativeId ? " active" : ""}`;
    tab.type = "button";
    tab.textContent = `Day ${day.id}`;
    tab.addEventListener("click", () => {
      state.selectedDay = day.id;
      state.activeAlternativeId = null;
      render();
    });
    els.dayTabs.append(tab);

    const option = document.createElement("option");
    option.value = day.id;
    option.textContent = `Day ${day.id}: ${day.title}`;
    els.daySelect.append(option);

    getDayAlternatives(day).forEach((alternative) => {
      const alternativeTab = document.createElement("button");
      alternativeTab.className = `chip-button backup-tab${day.id === state.selectedDay && state.activeAlternativeId === alternative.id ? " active" : ""}`;
      alternativeTab.type = "button";
      alternativeTab.textContent = `Day ${day.id} Backup`;
      alternativeTab.addEventListener("click", () => {
        state.selectedDay = day.id;
        state.activeAlternativeId = alternative.id;
        render();
      });
      els.dayTabs.append(alternativeTab);
    });
  });
  els.daySelect.value = String(state.selectedDay);
}

function renderBackupRouteBar() {
  const day = currentDay();
  const alternatives = getDayAlternatives(day);
  if (!day || !alternatives.length) {
    els.backupRouteBar.hidden = true;
    els.backupRouteBar.innerHTML = "";
    return;
  }

  els.backupRouteBar.hidden = false;
  els.backupRouteBar.innerHTML = `
    <div>
      <span>Day ${day.id} route options</span>
      <strong>${state.activeAlternativeId ? "Backup route active" : "Main route active"}</strong>
    </div>
    <button class="quiet-button${state.activeAlternativeId ? "" : " active"}" type="button" data-backup-option="">Main</button>
    ${alternatives.map((alternative) => `
      <button class="quiet-button backup-choice${state.activeAlternativeId === alternative.id ? " active" : ""}" type="button" data-backup-option="${escapeHtml(alternative.id)}">
        ${escapeHtml(alternative.title)}
      </button>
    `).join("")}
  `;

  els.backupRouteBar.querySelectorAll("[data-backup-option]").forEach((button) => {
    button.addEventListener("click", () => {
      state.activeAlternativeId = button.dataset.backupOption || null;
      render();
    });
  });
}

function renderDayDetail() {
  const day = currentDay();
  if (!day) return;
  const alternative = currentAlternative();
  const alternatives = getDayAlternatives(day);
  const displayedStops = alternative?.stops || day.stops;
  const displayedTitle = alternative?.title || day.title;
  const displayedSummary = alternative?.summary || day.summary;
  const displayedDriveHours = alternative?.driveHours ?? day.driveHours;
  els.dayDetail.innerHTML = "";
  const card = document.createElement("article");
  card.className = "day-card";
  card.innerHTML = `
    <div class="day-card-header">
      <div>
        <p class="eyebrow">Day ${day.id}</p>
        <h3>${escapeHtml(displayedTitle)}</h3>
        <p class="day-meta">${escapeHtml(displayedSummary)} / estimated ${displayedDriveHours}h driving</p>
      </div>
      ${state.editMode && !alternative ? '<button class="quiet-button" type="button" data-easy>Ease day</button>' : ""}
    </div>
    ${alternatives.length ? renderAlternativeSelector(day, alternatives) : ""}
    <div class="stop-list"></div>
  `;
  const easyButton = card.querySelector("[data-easy]");
  if (easyButton) {
    easyButton.addEventListener("click", () => {
      addMessage("assistant", makeDayEasier(day.id));
      persist();
      render();
    });
  }
  const list = card.querySelector(".stop-list");
  const alternativeButtons = card.querySelectorAll("[data-route-option]");
  alternativeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      state.activeAlternativeId = button.dataset.routeOption || null;
      render();
    });
  });
  displayedStops.forEach((stop, index) => {
    const row = document.createElement("div");
    row.className = `stop-row${state.editMode ? "" : " read-only-stop"}`;
    row.style.borderLeftColor = colorForStop(stop);
    row.innerHTML = `
      <div class="stop-main">
        <strong>${index + 1}. ${escapeHtml(stop.name)}</strong>
        <p class="stop-note">${escapeHtml(stop.type)} / ${escapeHtml(stop.note)}</p>
      </div>
      ${state.editMode && !alternative ? `
        <div class="stop-actions">
          <button class="chip-button lock-button${stop.locked ? " locked" : ""}" type="button" title="Lock stop">${stop.locked ? "Locked" : "Lock"}</button>
          <button class="chip-button" type="button" title="Move earlier">^</button>
          <button class="chip-button" type="button" title="Move later">v</button>
          <button class="chip-button" type="button" title="Remove stop">Skip</button>
        </div>
      ` : ""}
    `;
    const [lockButton, upButton, downButton, skipButton] = row.querySelectorAll("button");
    if (lockButton) {
      lockButton.addEventListener("click", () => toggleLock(day.id, stop.instanceId));
      upButton.addEventListener("click", () => moveStop(day.id, stop.instanceId, -1));
      downButton.addEventListener("click", () => moveStop(day.id, stop.instanceId, 1));
      skipButton.addEventListener("click", () => {
        removeStop(day.id, stop.instanceId);
        persist();
        render();
      });
    }
    row.addEventListener("click", (event) => {
      if (event.target.closest("button")) return;
      const marker = state.markers.get(stop.instanceId);
      if (!marker) return;
      map.setView(stop.coords, 11);
      marker.openPopup();
    });
    list.append(row);
  });
  els.dayDetail.append(card);
}

function renderDriveMode() {
  const enabled = state.editMode && els.driveModeToggle.checked;
  els.driveMode.hidden = !enabled;
  if (!enabled) return;
  const day = currentDay();
  const nextStop = day?.stops[1] || day?.stops[0];
  els.nextStopName.textContent = nextStop ? nextStop.name : "Choose a day";
}

function renderMap() {
  map.clearMarkers();
  map.clearRoutes();
  state.markers.clear();
  state.routeLines = [];

  const day = currentDay();
  const alternative = currentAlternative();
  const stops = alternative?.stops || (day ? day.stops : state.plan.days.flatMap((item) => item.stops));
  const stopsWithCoords = stops.filter((stop) => Array.isArray(stop.coords) && stop.coords.length === 2);
  els.mapStatus.textContent = `${stopsWithCoords.length} point${stopsWithCoords.length === 1 ? "" : "s"}`;
  stopsWithCoords.forEach((stop) => {
    const marker = map.addMarker(stop, els.labelsToggle.checked);
    state.markers.set(stop.instanceId, marker);
  });

  if (els.routeToggle.checked && stopsWithCoords.length > 1) {
    const renderToken = ++state.routeRenderToken;
    const fallbackDistance = routeDistanceLabel(stopsWithCoords);
    const routeLabel = alternative ? `Day ${day.id} backup` : `Day ${day?.id || ""}`;
    const line = map.addRoute(stopsWithCoords.map((stop) => stop.coords), colorForDay(day?.id || 0), `${routeLabel} routing...`, "loading");
    state.routeLines.push(line);
    roadRoute(stopsWithCoords).then((route) => {
      if (renderToken !== state.routeRenderToken) return;
      if (route) line.update(route.coords, `${routeLabel} / ${formatKm(route.distanceKm)} km`, "road");
      else line.update(stopsWithCoords.map((stop) => stop.coords), `${routeLabel} / ${fallbackDistance}`, "fallback");
    });
  }

  fitMap();
  window.setTimeout(() => fitMap(), 60);
}

function currentDay() {
  return state.plan?.days.find((day) => day.id === state.selectedDay) || state.plan?.days[0];
}

function currentAlternative() {
  const day = currentDay();
  if (!day || !state.activeAlternativeId) return null;
  return getDayAlternatives(day).find((alternative) => alternative.id === state.activeAlternativeId) || null;
}

function getDayAlternatives(day) {
  if (!day) return [];
  if (day.alternatives?.length) return day.alternatives;
  const alternatives = DAY_ALTERNATIVES[day.id] || [];
  return alternatives.map((alternative) => {
    const stops = alternative.stopIds.map((id, index) => makeStop(id, `${day.id}-${alternative.id}`, index + 1));
    return {
      id: alternative.id,
      title: alternative.title,
      summary: alternative.summary,
      driveHours: estimateDriveHours(stops),
      stops,
    };
  });
}

function renderAlternativeSelector(day, alternatives = getDayAlternatives(day)) {
  const options = [
    { id: "", title: "Main route", summary: day.summary, active: !state.activeAlternativeId },
    ...alternatives.map((alternative) => ({
      id: alternative.id,
      title: alternative.title,
      summary: alternative.summary,
      active: state.activeAlternativeId === alternative.id,
    })),
  ];
  return `
    <div class="route-options" aria-label="Route options">
      ${options.map((option) => `
        <button class="route-option${option.active ? " active" : ""}" type="button" data-route-option="${escapeHtml(option.id)}">
          <strong>${escapeHtml(option.title)}</strong>
          <span>${escapeHtml(option.summary)}</span>
        </button>
      `).join("")}
    </div>
  `;
}

function addMessage(author, text) {
  const message = document.createElement("div");
  message.className = `message ${author}`;
  message.textContent = text;
  els.chatLog.append(message);
  els.chatLog.scrollTop = els.chatLog.scrollHeight;
}

function persist() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.plan));
}

function loadSavedPlan() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

async function roadRoute(stops) {
  const coords = stops.map((stop) => stop.coords).filter(Boolean);
  if (coords.length < 2) return null;
  const cacheKey = coords.map((coord) => coord.map((value) => value.toFixed(5)).join(",")).join(";");
  if (roadRouteCache.has(cacheKey)) return roadRouteCache.get(cacheKey);
  const request = fetchRoadRoute(coords).catch(() => null);
  roadRouteCache.set(cacheKey, request);
  return request;
}

async function fetchRoadRoute(coords) {
  const osrmCoords = coords.map(([lat, lng]) => `${lng},${lat}`).join(";");
  const url = `https://router.project-osrm.org/route/v1/driving/${osrmCoords}?overview=full&geometries=geojson&steps=false`;
  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), 8000);
  try {
    const response = await fetch(url, { signal: controller.signal });
    if (!response.ok) return null;
    const data = await response.json();
    const route = data.routes?.[0];
    if (!route?.geometry?.coordinates?.length) return null;
    return {
      coords: route.geometry.coordinates.map(([lng, lat]) => [lat, lng]),
      distanceKm: route.distance / 1000,
    };
  } finally {
    window.clearTimeout(timeout);
  }
}

function fitMap() {
  const day = currentDay();
  const alternative = currentAlternative();
  const coords = (alternative?.stops || (day ? day.stops : state.plan.days.flatMap((item) => item.stops)))
    .map((stop) => stop.coords)
    .filter((coords) => Array.isArray(coords) && coords.length === 2);
  if (!coords.length) return;
  map.fitBounds(coords, { maxZoom: 11 });
}

function routeDistanceLabel(stops) {
  const total = stops.slice(1).reduce((sum, stop, index) => sum + haversineKm(stops[index].coords, stop.coords), 0);
  return `~${formatKm(total)} km`;
}

function formatKm(value) {
  if (!Number.isFinite(value)) return "?";
  return value >= 100 ? String(Math.round(value)) : String(Math.round(value * 10) / 10);
}

function haversineKm(from, to) {
  const earthKm = 6371;
  const dLat = degreesToRadians(to[0] - from[0]);
  const dLng = degreesToRadians(to[1] - from[1]);
  const lat1 = degreesToRadians(from[0]);
  const lat2 = degreesToRadians(to[0]);
  const a = Math.sin(dLat / 2) ** 2
    + Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLng / 2) ** 2;
  return earthKm * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}

function degreesToRadians(value) {
  return (value * Math.PI) / 180;
}

function colorForStop(stop) {
  return COLORS[stop.type] || COLORS[stop.kind] || "#0b6b63";
}

function colorForDay(dayId) {
  const palette = ["#0b6b63", "#1f6fb2", "#ba3f2f", "#7a5aa6", "#27864f", "#a86d16"];
  return palette[Math.abs(dayId) % palette.length];
}

function createMap(root) {
  const tileLayer = document.createElement("div");
  const routeLayer = document.createElement("div");
  const markerLayer = document.createElement("div");
  const popup = document.createElement("div");
  const controls = document.createElement("div");
  tileLayer.className = "tile-layer";
  routeLayer.className = "route-layer";
  markerLayer.className = "marker-layer";
  popup.className = "map-popup";
  popup.hidden = true;
  controls.className = "map-controls";
  controls.innerHTML = '<button type="button" aria-label="Zoom in">+</button><button type="button" aria-label="Zoom out">-</button>';
  root.append(tileLayer, routeLayer, markerLayer, popup, controls);

  const mapState = {
    center: [61.25, 6.65],
    zoom: 7,
    markers: [],
    routes: [],
    dragging: false,
    dragStart: null,
  };

  const api = {
    setView(coords, zoom = mapState.zoom) {
      mapState.center = coords;
      mapState.zoom = clamp(Math.round(zoom), 4, 15);
      popup.hidden = true;
      draw();
    },
    fitBounds(coords, options = {}) {
      if (!coords.length) return;
      const lats = coords.map((coord) => coord[0]);
      const lngs = coords.map((coord) => coord[1]);
      const minLat = Math.min(...lats);
      const maxLat = Math.max(...lats);
      const minLng = Math.min(...lngs);
      const maxLng = Math.max(...lngs);
      mapState.center = [(minLat + maxLat) / 2, (minLng + maxLng) / 2];
      const size = root.getBoundingClientRect();
      let chosenZoom = options.maxZoom || 11;
      for (let zoom = chosenZoom; zoom >= 4; zoom -= 1) {
        const nw = project([maxLat, minLng], zoom);
        const se = project([minLat, maxLng], zoom);
        if (Math.abs(se.x - nw.x) <= Math.max(120, size.width - 72) && Math.abs(se.y - nw.y) <= Math.max(120, size.height - 72)) {
          chosenZoom = zoom;
          break;
        }
      }
      mapState.zoom = clamp(chosenZoom, 4, options.maxZoom || 11);
      popup.hidden = true;
      draw();
    },
    clearMarkers() {
      mapState.markers = [];
      markerLayer.innerHTML = "";
      popup.hidden = true;
    },
    clearRoutes() {
      mapState.routes = [];
      routeLayer.innerHTML = "";
    },
    addMarker(stop, showLabel) {
      const marker = { stop, showLabel };
      mapState.markers.push(marker);
      drawMarkers();
      return {
        openPopup: () => openPopup(marker),
      };
    },
    addRoute(coords, color, label, mode = "road") {
      const route = { coords, color, label, mode };
      mapState.routes.push(route);
      drawRoutes();
      return {
        update(nextCoords, nextLabel, nextMode = mode) {
          route.coords = nextCoords;
          route.label = nextLabel;
          route.mode = nextMode;
          drawRoutes();
        },
      };
    },
  };

  controls.children[0].addEventListener("click", () => api.setView(mapState.center, mapState.zoom + 1));
  controls.children[1].addEventListener("click", () => api.setView(mapState.center, mapState.zoom - 1));
  root.addEventListener("pointerdown", (event) => {
    if (event.button !== 0 || event.target.closest(".map-controls, button")) return;
    root.setPointerCapture?.(event.pointerId);
    mapState.dragging = true;
    mapState.dragStart = { x: event.clientX, y: event.clientY, center: project(mapState.center, mapState.zoom) };
    root.classList.add("dragging");
  });
  root.addEventListener("pointermove", (event) => {
    if (!mapState.dragging) return;
    event.preventDefault();
    const deltaX = event.clientX - mapState.dragStart.x;
    const deltaY = event.clientY - mapState.dragStart.y;
    mapState.center = unproject({
      x: mapState.dragStart.center.x - deltaX,
      y: mapState.dragStart.center.y - deltaY,
    }, mapState.zoom);
    popup.hidden = true;
    draw();
  });
  root.addEventListener("pointerup", endDrag);
  root.addEventListener("pointercancel", endDrag);
  window.addEventListener("blur", endDrag);
  function endDrag(event) {
    if (event?.pointerId != null) root.releasePointerCapture?.(event.pointerId);
    mapState.dragging = false;
    root.classList.remove("dragging");
  }
  root.addEventListener("wheel", (event) => {
    event.preventDefault();
    api.setView(mapState.center, mapState.zoom + (event.deltaY < 0 ? 1 : -1));
  }, { passive: false });
  window.addEventListener("resize", draw);

  draw();
  return api;

  function draw() {
    drawTiles();
    drawRoutes();
    drawMarkers();
  }

  function drawTiles() {
    const size = root.getBoundingClientRect();
    const centerPx = project(mapState.center, mapState.zoom);
    const startX = centerPx.x - size.width / 2;
    const startY = centerPx.y - size.height / 2;
    const minTileX = Math.floor(startX / 256);
    const maxTileX = Math.floor((startX + size.width) / 256);
    const minTileY = Math.floor(startY / 256);
    const maxTileY = Math.floor((startY + size.height) / 256);
    const tileCount = 2 ** mapState.zoom;
    tileLayer.innerHTML = "";
    for (let x = minTileX; x <= maxTileX; x += 1) {
      for (let y = minTileY; y <= maxTileY; y += 1) {
        if (y < 0 || y >= tileCount) continue;
        const wrappedX = ((x % tileCount) + tileCount) % tileCount;
        const img = document.createElement("img");
        img.alt = "";
        img.draggable = false;
        img.src = `https://tile.openstreetmap.org/${mapState.zoom}/${wrappedX}/${y}.png`;
        img.style.left = `${Math.round(x * 256 - startX)}px`;
        img.style.top = `${Math.round(y * 256 - startY)}px`;
        tileLayer.append(img);
      }
    }
  }

  function drawRoutes() {
    const size = root.getBoundingClientRect();
    const centerPx = project(mapState.center, mapState.zoom);
    const startX = centerPx.x - size.width / 2;
    const startY = centerPx.y - size.height / 2;
    const paths = mapState.routes.map((route) => {
      const projected = route.coords.map((coord) => {
        const point = project(coord, mapState.zoom);
        return { x: Math.round(point.x - startX), y: Math.round(point.y - startY) };
      });
      const points = projected.map((point) => `${point.x},${point.y}`).join(" ");
      const labelPoint = routeLabelPoint(projected);
      const text = labelPoint
        ? `<text class="route-distance-label" x="${labelPoint.x}" y="${labelPoint.y}" text-anchor="middle">${escapeHtml(route.label)}</text>`
        : "";
      const dash = route.mode === "fallback" || route.mode === "loading" ? ' stroke-dasharray="8 8"' : "";
      const width = route.mode === "loading" ? 3 : 5;
      return `<polyline points="${points}" fill="none" stroke="${route.color}" stroke-width="${width}" stroke-linecap="round" stroke-linejoin="round" opacity="0.82"${dash} />${text}`;
    }).join("");
    routeLayer.innerHTML = `<svg viewBox="0 0 ${size.width} ${size.height}" aria-hidden="true">${paths}</svg>`;
  }

  function routeLabelPoint(points) {
    if (!points.length) return null;
    if (points.length === 1) return points[0];
    let total = 0;
    const segments = points.slice(1).map((point, index) => {
      const previous = points[index];
      const length = Math.hypot(point.x - previous.x, point.y - previous.y);
      total += length;
      return { from: previous, to: point, length };
    });
    let cursor = 0;
    const target = total / 2;
    for (const segment of segments) {
      if (cursor + segment.length >= target) {
        const ratio = segment.length ? (target - cursor) / segment.length : 0;
        return {
          x: Math.round(segment.from.x + (segment.to.x - segment.from.x) * ratio),
          y: Math.round(segment.from.y + (segment.to.y - segment.from.y) * ratio) - 10,
        };
      }
      cursor += segment.length;
    }
    return points[Math.floor(points.length / 2)];
  }

  function drawMarkers() {
    const size = root.getBoundingClientRect();
    const centerPx = project(mapState.center, mapState.zoom);
    const startX = centerPx.x - size.width / 2;
    const startY = centerPx.y - size.height / 2;
    markerLayer.innerHTML = "";
    for (const marker of mapState.markers) {
      const point = project(marker.stop.coords, mapState.zoom);
      const markerEl = document.createElement("div");
      markerEl.className = "marker";
      markerEl.style.left = `${Math.round(point.x - startX)}px`;
      markerEl.style.top = `${Math.round(point.y - startY)}px`;
      markerEl.innerHTML = `
        <button type="button" title="${escapeHtml(marker.stop.name)}">
          ${marker.showLabel ? `<span class="map-label">${escapeHtml(marker.stop.name)}</span>` : ""}
          <span class="marker-pin" style="background:${colorForStop(marker.stop)}">${escapeHtml(String(marker.stop.order))}</span>
        </button>
      `;
      markerEl.querySelector("button").addEventListener("click", () => openPopup(marker));
      markerLayer.append(markerEl);
    }
  }

  function openPopup(marker) {
    const size = root.getBoundingClientRect();
    const centerPx = project(mapState.center, mapState.zoom);
    const point = project(marker.stop.coords, mapState.zoom);
    const x = point.x - (centerPx.x - size.width / 2);
    const y = point.y - (centerPx.y - size.height / 2);
    popup.innerHTML = popupHtml(marker.stop);
    popup.hidden = false;
    popup.style.left = `${clamp(x + 14, 12, Math.max(12, size.width - 340))}px`;
    popup.style.top = `${clamp(y - 20, 12, Math.max(12, size.height - 330))}px`;
  }
}

function popupHtml(stop) {
  return `
    <div class="popup">
      <h3>${escapeHtml(stop.name)}</h3>
      <p><strong>Type:</strong> ${escapeHtml(stop.type)}</p>
      <p><strong>Why:</strong> ${escapeHtml(stop.note)}</p>
      <p><strong>Status:</strong> ${stop.locked ? "Locked into the plan" : "Flexible stop"}</p>
    </div>
  `;
}

function project([lat, lng], zoom) {
  const sinLat = Math.sin((lat * Math.PI) / 180);
  const scale = 256 * 2 ** zoom;
  return {
    x: ((lng + 180) / 360) * scale,
    y: (0.5 - Math.log((1 + sinLat) / (1 - sinLat)) / (4 * Math.PI)) * scale,
  };
}

function unproject(point, zoom) {
  const scale = 256 * 2 ** zoom;
  const lng = (point.x / scale) * 360 - 180;
  const n = Math.PI - (2 * Math.PI * point.y) / scale;
  const lat = (180 / Math.PI) * Math.atan(0.5 * (Math.exp(n) - Math.exp(-n)));
  return [lat, lng];
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function showToast(message) {
  els.toast.textContent = message;
  els.toast.hidden = false;
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => {
    els.toast.hidden = true;
  }, 3600);
}
