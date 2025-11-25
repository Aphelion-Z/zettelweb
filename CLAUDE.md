# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ZettelWeb** is a web-based visualization extension for the Zettelkasten system that displays notes (Zettel) as freely movable clusters in a network view. This is a university group project (Group 7, HHN WIN 3, WiSe 2025/26, Software Engineering course) with 7 team members and 125 hours allocated.

**Core Goals:**
- Visualize Zettel in a free-form, drag-and-drop network interface
- Group related Zettel into clusters using tags
- Persist positions and properties in a database
- Provide intuitive interaction with visual connections between Zettel

**Current Status:** Milestone 3 achieved - Basic implementation (v0.1) deployed
- Flask backend operational
- Simple table-based Zettel display
- Direct API integration (no authentication yet)
- 17 updated requirements defined in GitLab issues

## Architecture

### MVC Pattern (Model-View-Controller)

The system follows a strict **MVC architecture** with clear separation of concerns:

**Model Layer:**
- Classes: `Zettel`, `Tag`, `ZettelCluster`
- Responsibilities: Load/save Zettel data, analyze tags, manage clusters, maintain state and relationships
- Methods: `loadZettel()`, `clusterByTags()`, `saveProperties()`

**View Layer:**
- Responsibilities: Visualize data from Model as groups/clusters, respond to Controller events
- Methods: `renderGroups()`, `highlightTag()`, `displayZettelInfo()`, `updateZettelPosition()`

**Controller Layer:**
- Responsibilities: Mediate between User and System, process events, coordinate Model and View
- Methods: `handleInput()`, `loadZettelData()`, `updateView()`

### System Integration (ADR-01)

**Decision: Standalone Web Application**

ZettelWeb operates as an **independent web application** that:
- Uses the Zettelstore REST API to fetch Zettel data
- Maintains its own database for position and connection data
- Runs as a JavaScript application in the browser

**Rationale:**
- No changes to Zettelstore code required
- Independent development from Zettelstore release cycle
- Frontend technology freely selectable
- Team has frontend skills (JavaScript, HTML, CSS) but not Go

**Components:**
```
Browser (View + Controller)
    ↓ HTTPS/JSON
NetzWeb Backend (Model)
    ↓ REST API
Zettelstore Service
    ↓
Database (zettel, coordinates, properties tables)
```

### Database (ADR-02)

**Decision: SQLite**

SQLite was chosen for storing positions, connections, and metadata because:
- File-based, embeds directly in application
- No separate server required
- Simple setup and maintenance
- Portable (single file)
- Ideal for local, single-user development

**Trade-off:** Not suitable for multi-user scenarios (would require migration to server-based DB)

### Data Flow

User → View → Controller → Model → Zettelstore Service → Database
                                ↓
                              View (automatic updates)

## Key Requirements

### Functional Requirements (from Issues)
- **Tags/Clustering:** Users can group Zettel by adding tags
- **Visual Connections:** Display line connections between related Zettel
- **Hover Highlighting:** Highlight Zettel and direct neighbors on mouseover
- **Elastic Animation:** When dragging a Zettel, connected Zettel follow with spring-like animation
- **Position Persistence:** Save Zettel coordinates to database after each drag event
- **Search/Filter:** Filter Zettel by keywords in title, content, or tags
- **Zoom/Pan:** Navigate the view with zoom and pan controls

### Non-Functional Requirements
- **Performance:** Handle 200+ Zettel with smooth interaction (30+ fps, <200ms response time)
- **Save Performance:** Persist position changes within 3 seconds
- **Scalability:** Performance degradation <20% when scaling from 200 to 300 Zettel
- **Customization:** Support color settings and physical adjustments (element size, line thickness, drag behavior)

### Non-Requirements
- Font/font-size customization for Zettel display

## Development Context

### Project Timeline
- Start: 08.10.2025
- End: End of semester
- Milestones:
  1. Requirements analysis & conception
  2. Architecture & UI design
  3. Basic Zettel network functionality
  4. Data management
  5. Advanced user features
  6. QA & polish
  7. Project completion & presentation

### Team Structure
7 developers (see README.md for full list):
- sprachmann (Owner)
- mnowizki, aschockel, mkundoch, agrossu, lsaemann, bngothi (Maintainers)

### Technology Stack (Expected)
- **Frontend:** JavaScript (framework TBD), HTML, CSS
- **Backend:** Minimal backend for API orchestration
- **Database:** SQLite
- **Integration:** Zettelstore REST API
- **Protocol:** HTTPS with JSON requests/responses

## Repository Structure

```
zettelweb-code/
├── app.py                              [v0.1 Implementation]
├── requirements.txt                    [Python dependencies]
├── .gitignore                          [Git ignore patterns]
├── CLAUDE.md                           [This file]
├── README.md                           [Project charter]
├── QUICKSTART.md                       [Quick start guide]
├── templates/                          [Flask templates]
│   └── index.html
├── static/                             [CSS/JS assets]
│   └── style.css
├── docs/                               [Documentation]
│   └── api/                            [Zettelstore API docs - 5 files]
├── Tickets/                            [Requirements tracking]
│   └── requirements-2025-11-25.csv     [17 user stories from GitLab]
├── wiki/                               [Migrated GitLab wiki]
├── tutorials/                          [Step-by-step guides]
├── aufgaben-erklaert/                  [Task explanations]
└── zettel/                             [Zettel storage directory]
```

**Note:** This repository was migrated from GitLab. Milestone 3 (Basic implementation) achieved with Flask backend and table display. The wiki contains all architectural decisions and design documentation.

## Important Documentation

All architectural decisions are documented in `/wiki/Strategischer-Entwurf/`:
- **ADR-01:** System integration approach (standalone app vs. Zettelstore extension)
- **ADR-02:** Database choice (SQLite rationale)
- **Klassendiagramm-von-der-MVC-Architektur.md:** Detailed MVC class structure with diagram
- **Systemaufbau.md:** System component architecture diagram

## API Documentation

Comprehensive Zettelstore API documentation is available in `docs/api/`:

1. **README.md** - Navigation guide and quick reference
2. **01-API-Uebersicht.md** - API basics, URL structure, data formats
3. **02-Authentifizierung-Autorisierung.md** - JWT authentication, token management, authorization
4. **03-Endpunkt-Referenz.md** - Complete endpoint reference with examples
5. **04-Code-Beispiele.md** - Code examples in Python, JavaScript, Bash, Go, Java, C#

### Current API Usage

The current implementation (app.py) uses:
- **Endpoint:** GET /z (list all Zettel)
- **Authentication:** None (open endpoint)
- **Format:** Plain text (ID + title per line)

### Next Steps
- Implement JWT authentication (POST /a)
- Fetch full Zettel data (GET /z/{id})
- Parse metadata and content
- Extract tags and references

## Requirements Tracking

All requirements are tracked in `Tickets/requirements-2025-11-25.csv` with 17 user stories:

### Functional Requirements (Issues 17-27)
1. **#17** - Force-directed graph layout with automatic positioning
2. **#18** - Visual connection lines between Zettel
3. **#19** - Auto-load graph on opening with saved positions
4. **#20** - Click to view Zettel details (read-only)
5. **#21** - Drag & Drop repositioning with persistence
6. **#22** - Zoom and pan navigation with "Fit to View"
7. **#23** - Tag-based filtering with AND logic
8. **#24** - Context preservation (semi-transparent external connections)
9. **#25** - Hover-based connection highlighting
10. **#26** - Persistent manual positions with reset option
11. **#27** - State persistence (zoom, pan, filters)

### Non-Functional Requirements (Issues 28-33)
12. **#28** - Performance: ≥30 fps, <3s render, <100ms interaction (200+ Zettel)
13. **#29** - Browser compatibility: Chrome/Edge, Firefox, Safari
14. **#30** - Usability: ≥70% functions usable within 30 minutes by new users
15. **#31** - Persistence reliability: ≤1s save time, consistent crash recovery
16. **#32** - Loading feedback for operations >3 seconds
17. **#33** - Code maintainability: comprehensive documentation, clear structure

## Current Implementation (v0.1)

### Application Structure
```
zettelweb-code/
├── app.py                    # Flask application (18 lines)
├── templates/index.html      # Zettel table display
├── static/style.css          # Basic styling
├── requirements.txt          # Python dependencies
├── Tickets/                  # Requirements tracking
│   └── requirements-2025-11-25.csv
└── docs/api/                 # API documentation (5 files)
```

### Running the Application

**Prerequisites:**
- Python 3.8+
- Zettelstore running on http://127.0.0.1:23123

**Setup:**
```bash
cd zettelweb-code
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Access:** http://127.0.0.1:5000

### Features Implemented
- ✅ Fetch all Zettel from Zettelstore API (GET /z)
- ✅ Display Zettel ID and title in HTML table
- ✅ Basic Flask routing

### Features Pending (from Requirements CSV)
- ❌ Force-directed graph visualization (Issue #17)
- ❌ Visual connection lines (Issue #18)
- ❌ JWT authentication (Issue #19)
- ❌ Click to view details (Issue #20)
- ❌ Drag & Drop positioning (Issue #21)
- ❌ Zoom/pan navigation (Issue #22)
- ❌ Tag-based filtering (Issue #23-24)
- ❌ Hover highlighting (Issue #25)
- ❌ Position persistence (Issue #26-27)
- ❌ Performance optimization (Issue #28)

## Development Notes

### When Implementing Code
- Maintain strict MVC separation - do not mix responsibilities across layers
- Use Observer/Event pattern for communication between Controller and View
- All Zettelstore communication must go through REST API (no direct database access)
- Position data persistence should be separate from Zettel content
- Ensure drag-and-drop interactions remain responsive even with 200+ Zettel

### Testing Strategy
- Test Model layer independently without UI
- Verify API integration with Zettelstore separately
- Performance testing critical: measure fps and response times under load

### Known Constraints
- Must work with existing Zettelstore API (no server modifications allowed)
- SQLite database structure must support positions, connections, and properties
- Two separate data sources must be kept synchronized (Zettelstore + local DB)
