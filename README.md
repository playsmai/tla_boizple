# TLa Boizple - Masked Email Web App

Built by **@playsmai** 💻

TLa Boizple lets users create masked email aliases like `queenbee@plaboi.st` that auto-forward to their real address.  
It uses **FastAPI** for the backend and a beautiful, Apple-style HTML frontend.

---

## 🌐 Features

- ✅ Email verification via 5-digit code
- ✅ Fastmail-ready alias logic (mocked for now)
- ✅ Slack notification support (optional)
- ✅ Mobile-first responsive UI
- ✅ Ready to deploy on **Render** and **Vercel**

---

## 🚀 Deployment Guide

### 1. Backend (Render)

1. Go to [https://render.com](https://render.com)
2. Create a new **Web Service**
3. Use this repo as the source
4. Start command:  
   ```
   uvicorn main:app --host=0.0.0.0 --port=10000
   ```

### 2. Frontend (Vercel)

1. Go to [https://vercel.com](https://vercel.com)
2. Upload the `frontend/` folder or connect it to this repo
3. Set the deploy output to `index.html`

---

## 👋 Author

Built by `@playsmai` with assistance from OpenAI GPT.