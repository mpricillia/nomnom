# Nomnom AI 🦖

Nomnom AI is a smart, modern web application for sentiment analysis utilizing Hybrid Models (Google Gemini 1.5 Flash + IndoBERT) and DistilBERT. It offers automated text processing, scalable API quotas, and secure local credential management.

## Features ✨
- **Sentiment Analysis Playground:** Analyze text instantly using multiple AI models.
- **Hybrid & LLM Support:** Leverages Google Gemini 1.5 Flash for advanced batch sentiment processing and aspect extraction.
- **DistilBERT Integration:** 100% free local inference using Hugging Face models.
- **Smart Quota System:** Automated segmented credit policy with a visually pleasing capacity dashboard.
- **Secure Local Sandbox:** API keys are stored securely in your browser's local storage. No sensitive API data is synced to the database.
- **Rich Dashboard:** View usage history, sentiment distribution charts, and daily quotas.
- **Authentication:** Powered by Supabase Auth (Email & Password).

## Tech Stack 💻
- **Frontend:** React 18, TypeScript, Vite
- **Styling:** Tailwind CSS, Lucide Icons, Motion (Framer)
- **Backend/BaaS:** Supabase (PostgreSQL, Authentication)
- **AI Providers:** Google Gemini API (`@google/genai`), Hugging Face API

## Project Structure 📂
```text
📦 FINAL_NLP
 ┣ 📂 api               # Backend API endpoints / Serverless functions
 ┣ 📂 public            # Static assets (Logos, Icons, etc.)
 ┣ 📂 src               
 ┃ ┣ 📂 components      # React UI Components (Dashboard, Profile, Playground, etc.)
 ┃ ┣ 📂 hooks           # Custom React Hooks (e.g., useAuth)
 ┃ ┣ 📂 lib             # Integration configs (Supabase client, Gemini API services)
 ┃ ┣ 📜 App.tsx         # Main Application Layout and Routing
 ┃ ┗ 📜 main.tsx        # React Entry Point
 ┣ 📜 index.html        # Main HTML Template
 ┣ 📜 vite.config.ts    # Vite Configuration
 ┗ 📜 package.json      # Dependencies and Scripts
```

## Running Locally 🚀

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd FINAL_NLP
   ```

2. **Install Dependencies:**
   ```bash
   npm install
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your Supabase credentials:
   ```env
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   ```

4. **Start the Development Server:**
   ```bash
   npm run dev
   ```

## Deployment Guide (Vercel) 🌐

Nomnom AI is optimized to be deployed on Vercel. 

1. **Push your code to GitHub.**
2. Go to [Vercel.com](https://vercel.com/) and log in with your GitHub account.
3. Click **Add New** -> **Project**.
4. Import your newly created GitHub repository.
5. In the **Configure Project** section, Vercel will automatically detect the settings. Ensure they are:
   - Framework Preset: **Vite**
   - Build Command: `npm run build`
   - Output Directory: `dist`
6. Expand the **Environment Variables** section and add:
   - `VITE_SUPABASE_URL` = (your supabase project URL)
   - `VITE_SUPABASE_ANON_KEY` = (your supabase anon public key)
7. Click **Deploy**. Vercel will build and publish your project!
