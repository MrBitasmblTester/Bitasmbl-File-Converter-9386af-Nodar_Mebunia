# Bitasmbl-File-Converter-9386af-Nodar_Mebunia

## Description
Build a web application that allows users to upload files and convert them between formats, such as PDF to text or images to PNG. The system focuses on simplicity, intuitive UI, and fast conversions without requiring complex setup.

## Tech Stack
- FastAPI
- Tailwind CSS
- React

## Requirements
- Allow users to upload PDF and image files
- Convert PDF documents to text and images to PNG format
- Provide download links for converted files
- Show status updates during conversion (loading/progress)
- Handle unsupported file types and errors gracefully

## Installation
Follow these steps to set up the project locally. The repository owner username is MrBitasmblTester.

1. Clone the repository

   bash
   git clone https://github.com/MrBitasmblTester/Bitasmbl-File-Converter-9386af-Nodar_Mebunia.git
   cd Bitasmbl-File-Converter-9386af-Nodar_Mebunia
   

2. Backend (FastAPI)

   - Create and activate a Python virtual environment

     bash
     python3 -m venv venv
     source venv/bin/activate   # On Windows: venv\Scripts\activate
     

   - Install backend dependencies (expects a requirements.txt in the repo)

     bash
     pip install -r requirements.txt
     

   Typical backend dependencies you will see in requirements.txt for this stack include FastAPI and an ASGI server (uvicorn) plus file handling and conversion libraries. If a requirements.txt is not present, add FastAPI and an ASGI server:

     bash
     pip install fastapi uvicorn python-multipart pillow PyPDF2
     

3. Frontend (React + Tailwind CSS)

   - Change to the frontend directory (commonly named `frontend` or `web`) and install dependencies

     bash
     cd frontend
     npm install
     

   - Tailwind CSS is configured within the React frontend. If the project does not include Tailwind setup, install Tailwind per its documentation inside the frontend directory.

4. Project structure notes

   - Backend root: contains FastAPI app, endpoints for upload, status and download, and conversion logic.
   - Frontend root (frontend/): React app with UI for file upload, progress/status display, and download links.

## Usage
Start the backend and frontend services locally.

1. Start the backend (from the project root or backend directory):

   bash
   # from project root or backend folder
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   

   This command serves the FastAPI backend on http://localhost:8000.

   - The backend provides endpoints for uploading files, checking conversion status, and downloading converted files.
   - Use FastAPI BackgroundTasks or a task queue to perform conversions asynchronously so status can be polled.

2. Start the frontend (from the frontend directory):

   bash
   cd frontend
   npm start
   

   - The React UI allows users to select/upload PDF or image files, shows conversion progress/loading states, and displays download links for converted files.

3. Typical workflow

   - Open the React app in your browser (usually http://localhost:3000).
   - Upload a PDF or image file.
   - The UI should POST the file to the backend upload endpoint and show progress/loading.
   - Poll or query the status endpoint to receive progress updates.
   - When conversion completes, the UI shows a download link to retrieve the converted file (text for PDFs, PNG for images).

## Implementation Steps
1. Initialize repository structure
   - Create backend/ (FastAPI) and frontend/ (React) directories.
   - Add README, .gitignore, and basic package/dependency files (requirements.txt, package.json).

2. Backend: basic FastAPI app
   - Create app/main.py and mount API router(s).
   - Add CORS middleware to allow requests from the React frontend domain.

3. Backend: upload endpoint
   - Implement an endpoint that accepts file uploads (multipart/form-data).
   - Validate file MIME type and extension to allow only PDF and common image formats (e.g., image/png, image/jpeg).
   - On invalid/unsupported file types, return a clear error response.

4. Backend: asynchronous conversion handling
   - Use FastAPI BackgroundTasks (or a lightweight task mechanism) to perform conversion without blocking the request thread.
   - When an upload request is accepted, return a task identifier and initial status.

5. Backend: status endpoint
   - Implement a GET endpoint that returns the conversion status for a given task id (e.g., queued, processing, complete, error), and any progress information.

6. Backend: conversion logic
   - For PDFs: extract text from the uploaded PDF and save as a .txt file. Use a Python PDF parsing library available in the environment.
   - For images: convert uploaded images to PNG and save the converted PNG file. Use Pillow (PIL).
   - Ensure file output locations are accessible for download and are cleaned up per project policy.

7. Backend: download endpoint
   - Implement a secure endpoint to serve converted files (by filename or task id) with appropriate Content-Type and Content-Disposition headers.

8. Frontend: React UI
   - Build a simple upload form that accepts PDF and image files, posts to the backend upload endpoint, and displays immediate UI feedback.
   - Show a loading/progress indicator while conversion is processing.
   - Poll the status endpoint or use server-sent updates to refresh progress state in the UI.
   - When conversion completes, display a download link that points to the backend download endpoint.

9. Frontend: Tailwind styling
   - Integrate Tailwind CSS into the React app to style the upload form, progress indicators, and buttons with a simple and intuitive layout.

10. Error handling and edge cases
   - Gracefully handle unsupported formats and return user-friendly error messages.
   - Validate file sizes and implement limits if needed.
   - Handle backend failures by returning clear error states to the frontend.

11. Testing and local verification
   - Upload representative sample PDFs and images via the UI and verify the text extraction and PNG conversion outputs.
   - Confirm progress updates and download links work as expected.

## API Endpoints
- POST /api/upload
  - Accepts a multipart file upload (PDF or image). Starts conversion and returns a task id.

- GET /api/status/{task_id}
  - Returns current conversion status and optional progress metadata for the given task id.

- GET /api/download/{file_name}
  - Serves the converted file for download (text files for PDFs, PNGs for images).