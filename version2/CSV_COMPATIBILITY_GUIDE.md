# Compatible CSV Guide

Create a `.csv` file with a header row. These columns are recommended:

```csv
Layer,Day,Order,Name,Address,Type,Priority,Approx_Km,Approx_Time,Notes
```

## Important Columns

`Name`

Display name for the stop.

`Address`

Used to locate known places. For new or custom places, include coordinates instead.

`Latitude`, `Longitude`

Best for reliable placement. Use decimal degrees, for example:

```csv
Latitude,Longitude
60.3913,5.3221
```

`Layer`

Group name, such as `Route Day 1`, `Accommodation`, `EV Hubs`, or `Must-See Points`.

`Day`

Trip day or timing, such as `Day 1`, `Day 5`, or `Night 1-2`.

`Order`

Number used to connect route stops in sequence. Route lines are drawn only when ordered route stops exist.

`Type`

Stop category, such as `Route Stop`, `Viewpoint`, `Ferry`, `Accommodation`, or `EV / Services`.

`Priority`

Used for marker colors. Good values include `Must`, `Recommended`, `Optional`, `Alternative`, `Safest`, and `Weather dependent`.

`Approx_Km`

Optional planned distance, such as `170-190` or `220-280 total day`.

`Approx_Time`

Optional timing note.

`Notes`

Any extra planning detail.

## Example

```csv
Layer,Day,Order,Name,Address,Type,Priority,Approx_Km,Approx_Time,Notes
Route Day 1,Day 1,1,Bergen,"Bergen, Norway",Route Stop,Must,0,Start,Pick up car
Route Day 1,Day 1,2,Voss,"Voss, Norway",Route Stop / EV,Recommended,100,1.5-2 hr,Charge or groceries
Route Day 1,Day 1,3,Aurland,"Aurland, Norway",Accommodation Area,Must,170-190,3.5-4.5 hr,Night base
```

For best results with new places, add `Latitude` and `Longitude` columns.
