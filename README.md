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

### Overall retrospective

Overall I'd like to mention that the guiding principle for the project, during the short bursts I worked on it, was to satisfy all my known users, which is this case unfortunately spanned only me. This means that I took some liberties to make a page that I would find interesting to use, prioritizing features I found interesting. It is slightly unfortunate since for example data persistence is a fairly important aspect of development, but in the context of this app, I just didn't find any angle that would make me interested in it, not without imagining a whole bunch of extra features I knew I wouldn't have time to implement, like user authentication etc, which was firmly outside the scope of the project.

*Data Import* got done pretty much completely as instructed, with the caveat that there's no persistent storage. This was pretty straightforward, with the use of Polars, another library I had been wanting to learn(sorta replacement of Pandas), processing CSV's was quite fast, even if they were fairly large. I was actually initially expecting I would need databases as the CSV sizes were quite large, but turns out Polars is really efficient enough to effortlessly allow crunching them as part of spinning up a server.

*Journey List View* was something I struggled with, since I couldn't really come up with any real use case for it, but it seemed like a central feature. It exists, I practiced some of the Svelte component stuff with it. It lacks pagination but also I couldn't really come up with good mental model of what trips even should be paginated. The unfiltered list of all trips seems as interesting as paginating the entire Internet, so I was playing with time-based selection methods(see my LogSlider detour if curious), but ultimately I still can't really say why someone would actually look at the Journey List View. My best bet was that they want to see trips made at some specific time, so I have trips starting at specific minute listed, requiring no pagination as length of the list is probabl the information the user wants from this search anyway. I was considering other search lengths  here, like 5min, to reduce variance in this one detail I was interested in(length of list), but UI challenge of communicating to user which time span you are actually looking at seemed too significant, and overall it added more trips to the view, and as stated, I just didn't find those individual trips interesting.

*Station List* wasn't implemented. The endpoints for it exist, but as there's only a few more hours left for the project deadline, it's probably not part of the project.

*Single Station View* was the last bit to get implemented. I wanted to play with map, but it seemed like it would've taken a bit too much time to get this working. Station view is quite barren, it only has the basic information about a station, and the next feature I might squeeze in before deadline is adding trip statistics to this page, which already has API endpoint for it.

Testing is something I couldn't fit into this project. I usually go for TDD, but a notable guideline I follow is that APIs and user interfaces are not reasonably testable by TDD, and this project really didn't seem to have much that would exist outside of APIs and user interfaces. 