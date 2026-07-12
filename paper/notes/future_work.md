# Future work / parking lot

After the Week 7 experiment freeze, new ideas land HERE, not in code (standing rule,
Week 7). Out of scope for this paper by design:

- Outlier-aware bounds: how much quantization damage does a first-order analysis
  explain, and what does the residual demand?
- Composition with rotations (QuaRot, PolarQuant): allocation *after* variance
  equalization — rotations equalize variance within vectors; allocation exploits
  asymmetry between components. The two compose — the natural sequel.
- Information-theoretic lower bounds for allocation under output distortion.
- Mixed eviction + quantization; residual corrections.
