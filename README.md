# 🚗 Fuel Optimizer

A full-stack web application that helps users find the most cost-efficient gas stations along a route by balancing fuel price and detour distance.

---

## 🔥 Features

- 📍 Route-based input (Start → Destination)
- ⛽ Gas station comparison (price + detour)
- ⭐ Smart recommendation system:
  - Best Value (lowest total cost)
  - Cheapest
  - Most Convenient (lowest detour)
- 📊 Total fuel cost calculation
- 🌐 Full-stack architecture (FastAPI + HTML/JS)

---

## 🛠 Tech Stack

### Backend
- FastAPI (Python)
- REST APIs
- Custom optimization logic

### Frontend
- HTML, CSS, JavaScript
- Fetch API for backend communication

---

## 🧠 How It Works

1. User enters start and destination
2. Backend fetches gas station data (API / fallback)
3. Calculates:
   - Fuel cost
   - Detour impact
   - Total trip cost
4. Returns optimized recommendations
5. UI displays results in card format

---

## 🚀 Run Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

## 📸 Screenshots

![App UI](frontend/screenshot.png)