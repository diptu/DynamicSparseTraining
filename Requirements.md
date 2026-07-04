# Functional Specification: Interactive Research Platform
## GOAL:
I am essentially building a "Live Paper." Instead of just publishing the PDF or Markdown file, I am creating a digital environment where the reader can "run" the math you have derived.

## 1. System Overview
The platform serves as a "Living Document" system, evolving the `theoretical-kv-cache` research repository into an interactive, high-fidelity web experience. It renders academic-grade research while embedding stateful, reactive simulations.

---

## 2. Core Functional Requirements

### A. The "Research Narrative" Engine
* **Dynamic Markdown (MDX) Rendering:** Parse local `.md` research notes and convert them into interactive web pages.
* **Mathematical LaTeX Rendering:** Integration of **KaTeX** for high-performance rendering of linear algebra and machine learning derivations.
* **Reference Management:** Auto-generate citations and cross-reference links between papers, definitions, and derivations.

### B. The "Reactive Visualization" Sandbox
* **Stateful Simulation Environment:**
    * **Interactive Inputs:** Provide sliders, dropdowns, and input fields to manipulate variables (e.g., sequence length, compression ratio).
    * **Real-time Computation:** Use **Math.js** or **TensorFlow.js** in-browser to re-compute results instantly upon input change.
* **Synchronization Store (Zustand):** Synchronize multiple charts and formulas so that updating a single parameter propagates changes across the entire document.

### C. Researcher Productivity Tools
* **Version-Controlled Publishing:** Deployment tied directly to GitHub repository pushes via Vercel/GitHub integration.
* **Global Search (Fuse.js):** Searchable index for papers, definitions, and personal research notes.
* **Print-to-PDF Mode:** Layout toggle that strips interactive components and optimizes CSS for academic, A4-ready paper exports.

---

## 3. Data Flow Specification

1.  **Input:** Developer pushes Markdown/MDX to `/research/` folder.
2.  **Processing (Build Time):**
    * Next.js fetches MDX.
    * KaTeX converts LaTeX strings to static HTML/CSS.
    * Content cached via Incremental Static Regeneration (ISR).
3.  **Client-Side (Run Time):**
    * Browser loads the page.
    * React hydrates interactive components (`KVCacheViz`, `AttentionMatrix`).
    * Web Workers handle heavy matrix computations to maintain 60fps performance.

---

## 4. Proposed Feature Roadmap

| Phase | Feature | Tech Focus |
| :--- | :--- | :--- |
| **Phase 1** | **The Research Portal** | Next.js, MDX, KaTeX, Vercel |
| **Phase 2** | **The Interactive Sandbox** | D3.js, Framer Motion, Zustand |
| **Phase 3** | **Computational Layer** | TensorFlow.js, Web Workers |
| **Phase 4** | **Export/Print Mode** | CSS Print Media Queries |

---

## 5. Technical Stack Summary

* **Framework:** [Next.js (App Router)](https://nextjs.org/)
* **Styling:** [Tailwind CSS](https://tailwindcss.com/)
* **Math:** [KaTeX](https://katex.org/)
* **Visuals:** [D3.js](https://d3js.org/)
* **Animation:** [Framer Motion](https://www.framer.com/motion/)
* **State:** [Zustand](https://docs.pmnd.rs/zustand/getting-started/introduction)

---

> "Every mathematical concept learned should answer one question: How does this reduce or explain memory in transformers?"
