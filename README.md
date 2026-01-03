# autonomous-web-agent
Autonomous multi-agent web search system using Python and Playwright


📌 Project Overview

This project is an autonomous multi-agent web search system built using Python and Playwright, designed to accept natural language user queries and execute them automatically in a real browser.

The system follows agentic AI principles, where different agents are responsible for understanding user intent, planning actions, and executing tasks in a digital environment.

The focus of this project is agent architecture, workflow execution, browser automation, and developer experience, rather than simple scripting.

🎯 Project Motivation

Most automation scripts:

Require fixed commands

Break easily

Do not scale well

Are hard to debug

This project was built to explore how AI agents can autonomously act on the web, starting from a high-level goal and translating it into real browser actions.

🧠 System Architecture

The system uses a lightweight multi-agent design:

User Input
   ↓
Intent Agent
   ↓
Planner Agent
   ↓
Executor Agent
   ↓
Browser (Playwright)

Agent Responsibilities
1️⃣ Intent Agent

Understands what the user wants to do

Detects search-related intent from free-form text

2️⃣ Planner Agent

Converts user intent into executable steps

Designed to be LLM-ready, but currently uses a mock planner for cost-free local execution

3️⃣ Executor Agent

Controls the browser using Playwright

Navigates search engines

Executes actions reliably in real web environments

🛠️ Tech Stack
Category	Technology
Language	Python 3
Browser Automation	Playwright (Async)
Agent Design	Multi-Agent Architecture
Environment	Virtual Environment (venv)
Search Engine	DuckDuckGo (CAPTCHA-safe)
IDE	Visual Studio Code
