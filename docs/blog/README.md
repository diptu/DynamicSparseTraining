# Blog posts

The **translation layer**: the ideas in this repository told to a general ML audience, without
the proof machinery. A good post is how the work reaches people who won't read an arXiv PDF —
and, not incidentally, how a PhD admissions reader discovers you can explain, not just derive.

> Blog posts also render on the "Live Paper" web platform described in `Requirements.md`
> (Next.js + MDX + KaTeX). Write posts as portable Markdown with front-matter so they drop into
> that pipeline unchanged.

## Layout

```
blog/
├── README.md      this index
├── TEMPLATE.md    front-matter + structure for a new post
├── drafts/        work in progress
└── published/     posts that have shipped (kept for the record)
```

## House style

- **One idea per post.** If it needs two theorems, it's two posts.
- **Lead with the picture, not the proof.** State the punchline in the first two sentences.
- **Every post answers the lens:** *how does this reduce or explain memory in transformers?*
- **Link down, not out.** Point to the report/paper for rigor; keep the post readable start to
  finish without them.

## Posts

| Post | Angle | Status |
|------|-------|--------|
| [drafts/why-keys-need-more-bits.md](drafts/why-keys-need-more-bits.md) | The intuition: why value error is gentle and key error amplifies. | 🌱 outline |
