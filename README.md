# Joniis bike trip app

Based on the task related to Solita Dev Academy. (See `TASK_DESCRIPTION_SOLITA.md`)

This project essentially acts as a frontend/backend combo to interface with a .csv file.

This is somewhat different from the spirit of the assignment, where the idea is to be more generic trip data database,
with database one can update. I find databases at least this early in development to be quite problematic, CSV interface
idea allows the design to approximate functional paradigm better without persisting state. Maybe eventually.

Features trip data viewer, with filtering based on time, API for fetching trips, and API for fetching data of trip aggregate data.

### Running the project

Navigate to folder "city-bike", and run `npm run dev -- --open`. This launches server running the frontend, and opens browser on the main page.

Navigate to "backend", and run `pip install -r requirements.txt`, then `uvicorn app.app:app`

You can now upload CSV of your choice to the server using the frontend.