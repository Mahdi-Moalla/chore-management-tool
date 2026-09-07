# Chore Management Tool - Task Backlog

## 1. Set up empty project with passing tests
**Goal:** Initialize Django + HTMX project with SQLite, uv, and basic test suite  
**Description:** Create a new Django project using uv, configure settings for SQLite database, set up project structure for HTMX views, create the first minimal test file, and run initial tests to verify everything works.

## 2. Create User model and authentication
**Goal:** Implement user registration, login/logout functionality  
**Description:** Define a User model (extending Django's built-in auth system), create login/register views with HTMX support, implement password hashing and validation, and handle session management for multi-device access.

## 3. Create Chore model basic structure
**Goal:** Define chore data model with core fields  
**Description:** Create the Chore model with fields for title, description, assigned_user_link, completion_status (enum), due_date, created_at, updated_at. Set up initial migration and create test data for manual testing.

## 4. Implement one-time chore CRUD views
**Goal:** Allow users to create, read, update, delete one-time chores  
**Description:** Build HTMX-enabled views for creating new one-time chores, listing all assigned chores, updating chore details, and deleting chores with proper permissions checks for the assigned user.

## 5. Implement recurring chore model
**Goal:** Define recurring chore structure with period-specific assignments  
**Description:** Create a SeparateModel or linked table approach for recurring chores: base record (title, frequency) + PeriodAssignment records (user_assignment_per_period, start/end_date). Include status tracking for each assignment instance.

## 6. Build recurring chore list view
**Goal:** Display upcoming recurring chore instances  
**Description:** Create HTMX endpoint to fetch and display pending/upcoming periodic assignments from current period forward, filter by user or show all chores with assignee information in a paginated or infinite-scroll format.

## 7. Create chore assignment form for recurring tasks
**Goal:** Allow manual per-period user assignment for recurring chores  
**Description:** Build a dynamic HTMX form that fetches available recurring chores and periods needing assignment, lets user select both periodic date range and assigned person via dropdown/combobox, saves as individual PeriodAssignment records.

## 8. Add chore status transition logic
**Goal:** Handle state changes between not started → in progress → completed  
**Description:** Create view functions that process transitions with timestamp logging (start_time, completion_time), prevent invalid state transitions (like going back to not started after completion), and optionally allow admin override for corrections.

## 9. Build shared dashboard home view
**Goal:** Display overview of assigned chores for authenticated users  
**Description:** Show all chores assigned to the logged-in user across one-time and recurring instances, grouped by due date or priority, with quick-status actions (mark complete) directly in the UI using HTMX patches.

## 10. Add completion statistics per user
**Goal:** Visualize individual compliance and progress  
**Description:** Compute counts/completion rates per user within a configured time window, present as simple bars/progress text, show overdue items vs on-track chores, and display overall team stats for motivation.
