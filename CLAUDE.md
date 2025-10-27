# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ZettelWeb** is a web-based visualization extension for the Zettelkasten system that displays notes (Zettel) as freely movable clusters in a network view. This is a university group project (Group 7, HHN WIN 3, WiSe 2025/26, Software Engineering course) with 7 team members and 125 hours allocated.

**Core Goals:**
- Visualize Zettel in a free-form, drag-and-drop network interface
- Group related Zettel into clusters using tags
- Persist positions and properties in a database
- Provide intuitive interaction with visual connections between Zettel

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
/wiki/                  # Migrated GitLab wiki documentation
  /Strategischer-Entwurf/  # Architecture Decision Records (ADRs)
  /uploads/             # Screenshots and diagrams
/zettel/                # Zettel directory (placeholder)
README.md               # Project charter and goals
```

**Note:** This repository was migrated from GitLab. The codebase is in early planning/documentation phase - implementation has not yet begun. The wiki contains all architectural decisions and design documentation.

## Important Documentation

All architectural decisions are documented in `/wiki/Strategischer-Entwurf/`:
- **ADR-01:** System integration approach (standalone app vs. Zettelstore extension)
- **ADR-02:** Database choice (SQLite rationale)
- **Klassendiagramm-von-der-MVC-Architektur.md:** Detailed MVC class structure with diagram
- **Systemaufbau.md:** System component architecture diagram

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
