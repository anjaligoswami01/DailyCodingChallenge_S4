# Day 37/60 – Frontend Deployment and API Integration

## Overview

This project focuses on deploying a production-ready AI application by connecting a Next.js frontend hosted on Vercel with a FastAPI backend deployed on Railway. The goal was to make the application accessible over the public internet and verify the complete user experience across desktop and mobile devices.

## Objectives

* Deploy Next.js frontend to Vercel
* Connect frontend to Railway-hosted FastAPI backend
* Replace hardcoded localhost URLs with environment variables
* Configure CORS for secure frontend-backend communication
* Verify streaming responses and source citations
* Test responsiveness on mobile devices
* Measure browser-to-first-token latency

## Technologies Used

* Next.js
* React
* FastAPI
* Railway
* Vercel
* GitHub

## Implementation

### Frontend Deployment

* Connected GitHub repository to Vercel
* Configured automatic deployments on every push to the main branch
* Added environment variables for backend API connectivity

### Backend Configuration

* Added CORS middleware in FastAPI
* Allowed requests from the deployed Vercel frontend
* Verified successful communication between services

### Testing & Validation

* Tested the complete user journey from a live browser
* Verified streaming AI responses
* Confirmed source citations displayed correctly
* Performed mobile responsiveness testing
* Fixed at least one UI issue identified during testing

## Key Learnings

* Environment variables make applications portable across environments.
* CORS configuration is essential when frontend and backend are hosted separately.
* Automated deployments simplify the development workflow.
* Mobile testing helps uncover usability issues missed on desktop.
* Production latency differs from local development and should be measured and monitored.

## Outcome

Successfully deployed a full-stack AI application with:

* Live Vercel frontend
* Live Railway backend
* Working API integration
* Streaming responses
* Mobile-friendly interface
* End-to-end functionality verified

## Challenge

Day 37/60 – AI Challenge by ABTalksOnAI

Focused on Frontend Deployment and API Integration to deliver a fully accessible AI application experience.
