"""Hand-laid SVG figures for the publication rows. 600x400, one idea each.
Every coordinate is explicit; arcs are true SVG arcs; connectors are cubic Beziers.
"""
import csv, math, pathlib, sys
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)

FONT = "Inter, Helvetica, Arial, sans-serif"
INK, MUTED, RULE, PAPER = "#1b1b1b", "#6b655b", "#d6d2ca", "#fbfaf7"
BLUE, BLUE_T, BLUE_M = "#1f77b4", "#d7e5f1", "#8db4d6"
ORANGE, ORANGE_T = "#d9690b", "#f7dfcb"
PURPLE, PURPLE_T = "#7a1f8f", "#e6d4ea"
GRAY, GRAY_T, GRAY_M = "#9a948a", "#ebe8e1", "#cfcac0"
W, H = 600, 400

def t(x, y, s, size=13, fill=INK, anchor="start", weight=400, rotate=None, baseline="middle", ls=None):
    tr = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
    lsp = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" dominant-baseline="{baseline}"{tr}{lsp}>{s}</text>')

def line(x1, y1, x2, y2, stroke=RULE, w=1, cap="round", dash=None, opacity=1):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}" stroke-linecap="{cap}"{d} opacity="{opacity}"/>'

def arrow(x1, y, x2, stroke=MUTED, w=1.8):
    # straight horizontal arrow with a small filled head
    return (line(x1, y, x2 - 7, y, stroke, w) +
            f'<path d="M{x2 - 9},{y - 5} L{x2},{y} L{x2 - 9},{y + 5} Z" fill="{stroke}"/>')

def arc(x1, x2, y, ry_ratio=0.5, stroke=GRAY, w=1.6, opacity=1):
    rx = (x2 - x1) / 2; ry = rx * ry_ratio
    return f'<path d="M{x1},{y} A{rx},{ry} 0 0,1 {x2},{y}" fill="none" stroke="{stroke}" stroke-width="{w}" stroke-linecap="round" opacity="{opacity}"/>'

def dot(cx, cy, r, fill, ring=PAPER, rw=1.6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{ring}" stroke-width="{rw}"/>'

def svg(body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>')

def write(name, body, title):
    (OUT / f"{name}.svg").write_text(svg(body, title)); print("wrote", name)

# ------------------------------------------------------------------ 1. SUMMIT: LD along the genome
def fig_summit():
    b = []
    x0, x1 = 172, 568
    n = 16
    xs = [x0 + 6 + i * (x1 - x0 - 12) / (n - 1) for i in range(n)]
    # window of standard LD scores
    wx0, wx1 = xs[6] - 14, xs[8] + 14
    b.append(f'<rect x="{wx0}" y="62" width="{wx1 - wx0}" height="276" rx="5" fill="{ORANGE_T}" opacity="0.55"/>')
    b.append(f'<rect x="{wx0}" y="62" width="{wx1 - wx0}" height="276" rx="5" fill="none" stroke="{ORANGE}" stroke-width="1.4" stroke-dasharray="4 4"/>')
    b.append(t((wx0 + wx1) / 2, 46, "window of standard LD scores", 12.5, MUTED, "middle"))
    short = [(0, 1), (2, 3), (5, 6), (7, 8), (10, 11), (13, 14)]
    longp = [(1, 9), (4, 12), (7, 15)]
    for label, y, long_arcs in (("Single ancestry", 150, False), ("Admixed", 300, True)):
        b.append(f'<rect x="{x0}" y="{y - 5}" width="{x1 - x0}" height="10" rx="5" fill="{GRAY_T}"/>')
        for x in xs:
            b.append(f'<circle cx="{x:.1f}" cy="{y}" r="2.6" fill="{INK}"/>')
        for i, j in short:
            b.append(arc(xs[i], xs[j], y - 6, 0.9, GRAY, 1.6))
        if long_arcs:
            for i, j in longp:
                b.append(arc(xs[i], xs[j], y - 6, 0.42, BLUE, 2.4, 0.95))
        b.append(t(x0 - 14, y, label, 13.5, INK, "end", 500))
    b.append(t(x0 - 14, 171, "local LD only", 11.5, MUTED, "end"))
    b.append(t(x0 - 14, 321, "long-range LD too", 11.5, MUTED, "end"))
    b.append(line(172, 372, 198, 372, BLUE, 2.4))
    b.append(t(206, 372, "correlation captured only by genome-wide LD scores", 12.5, MUTED))
    write("fig_summit", "".join(b), "Genome-wide versus windowed LD scores in single-ancestry and admixed genomes")

# ------------------------------------------------------------------ 2. ML4H: recognition curves (real data)
def fig_recognition(path):
    rows = [r for r in csv.DictReader(open(path), delimiter="\t") if r["scope"] == "linked" and r["endpoint"] == "coverage_end"]
    series = [("diabetes", "Diabetes", BLUE), ("ckd_confirmed", "Kidney disease", ORANGE), ("anaemia", "Anemia", PURPLE)]
    px0, px1, py0, py1 = 92, 468, 62, 330     # plot box: y0 = 100 %, y1 = 0 %
    def X(yr): return px0 + (px1 - px0) * yr / 5.0
    def Y(p): return py1 - (py1 - py0) * p
    b = []
    for pct in (25, 50, 75, 100):
        b.append(line(px0, Y(pct / 100), px1, Y(pct / 100), RULE, 1))
    b.append(line(px0, py1, px1, py1, GRAY_M, 1.2, "butt"))
    for pct, lab in ((0, "0"), (25, "25"), (50, "50"), (75, "75"), (100, "100%")):
        b.append(t(px0 - 10, Y(pct / 100), lab, 12, MUTED, "end"))
    for yr in range(6):
        b.append(t(X(yr), py1 + 16, str(yr), 12, MUTED, "middle"))
    b.append(t(px0, 34, "Share with a diagnosis on record", 13.5, INK, "start", 600))
    b.append(t((px0 + px1) / 2, 372, "Years after a blood test in the disease range", 13, INK, "middle"))
    for key, label, col in series:
        pts = sorted(((float(r["years"]), float(r["ci"])) for r in rows if r["condition"] == key and float(r["years"]) <= 5.0001))
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(yr):.1f},{Y(p):.1f}" for i, (yr, p) in enumerate(pts))
        b.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>')
        yr, p = pts[-1]
        b.append(dot(X(yr), Y(p), 4.6, col, PAPER, 2))
        b.append(t(X(yr) + 14, Y(p), f"{label} {p * 100:.0f}%", 13, INK))
    write("fig_recognition", "".join(b), "Share of people with a diagnosis on record in the five years after a blood test in the disease range")

# ------------------------------------------------------------------ 3. RAPTOR: pipeline
def fig_raptor():
    b = ['<g transform="translate(0,-26)">']
    cy = 196
    # 3D scan: six slices receding up-right, soft anatomy blob on the front slice
    for i in range(5, -1, -1):
        x, y = 44 + i * 7, 154 - i * 7
        fill = GRAY_T if i else "#f4f1ea"
        b.append(f'<rect x="{x}" y="{y}" width="92" height="104" rx="3" fill="{fill}" stroke="{INK}" stroke-width="1.1"/>')
    b.append(f'<ellipse cx="90" cy="206" rx="30" ry="36" fill="{BLUE_T}"/>')
    b.append(f'<ellipse cx="82" cy="200" rx="12" ry="16" fill="{BLUE_M}" opacity="0.55"/>')
    b.append(t(97, 290, "3D scan", 13.5, INK, "middle", 500))
    b.append(arrow(152, cy, 190))
    # frozen model
    b.append(f'<rect x="198" y="156" width="134" height="80" rx="10" fill="none" stroke="{BLUE}" stroke-width="2"/>')
    b.append(t(265, 187, "frozen 2D", 14, INK, "middle", 600))
    b.append(t(265, 208, "image model", 12.5, MUTED, "middle"))
    b.append(t(265, 290, "no training", 13.5, INK, "middle", 500))
    b.append(arrow(340, cy, 378))
    # random projection: 6 x 7 dots, fixed two-tone pattern
    pat = "100101011010110011010100101101011010100110"
    k = 0
    for r in range(7):
        for c in range(6):
            fill = INK if pat[k % len(pat)] == "1" else GRAY_M; k += 1
            b.append(f'<circle cx="{386 + c * 11.6:.1f}" cy="{162 + r * 11.6:.1f}" r="3.1" fill="{fill}"/>')
    b.append(t(415, 290, "random projection", 13.5, INK, "middle", 500))
    b.append(arrow(462, cy, 508))
    # embedding: vertical strip of nine cells in blue tints
    tints = [BLUE, BLUE_M, BLUE, BLUE_T, BLUE_M, BLUE, BLUE_T, BLUE, BLUE_M]
    for i, c in enumerate(tints):
        b.append(f'<rect x="520" y="{158 + i * 9}" width="26" height="8" rx="1.5" fill="{c}"/>')
    b.append(t(533, 290, "embedding", 13.5, INK, "middle", 500))
    b.append(line(44, 326, 568, 326, RULE, 1))
    b.append(t(306, 352, "one consumer graphics card  ·  about 6.5 seconds per scan", 13, MUTED, "middle"))
    b.append("</g>")
    write("fig_raptor", "".join(b), "RAPTOR pipeline: 3D scan, frozen 2D image model, random projection, compact embedding")

# ------------------------------------------------------------------ 4. ENGINE: many exposures, one learned combination
def fig_engine():
    b = []
    exposures = [("age", 1.0), ("body mass index", 0.82), ("smoking", 0.38), ("alcohol", 0.22), ("diet", 0.15), ("sleep", 0.11), ("activity", 0.08)]
    nx, ny = 338, 192
    b.append(t(214, 46, "learned weight", 12, MUTED, "middle"))
    for i, (name, w) in enumerate(exposures):
        y = 72 + i * 40
        bw = 96 * w
        b.append(t(150, y, name, 13, INK, "end"))
        b.append(f'<rect x="162" y="{y - 5}" width="{bw:.1f}" height="10" rx="2" fill="{BLUE if w > 0.3 else BLUE_T}"/>')
        xs = 162 + bw + 8
        sw = 0.8 + 3.0 * w
        b.append(f'<path d="M{xs:.1f},{y} C{xs + 50:.1f},{y} {nx - 60},{ny} {nx - 15},{ny}" fill="none" stroke="{GRAY_M}" stroke-width="{sw:.1f}" stroke-linecap="round" opacity="0.9"/>')
    b.append(dot(nx, ny, 13, PAPER, INK, 2))
    b.append(t(nx, 304, "one learned", 12.5, MUTED, "middle"))
    b.append(t(nx, 320, "combination", 12.5, MUTED, "middle"))
    b.append(line(nx, 207, nx, 290, RULE, 1))
    b.append(arrow(354, ny, 400))
    # small effect chart
    ax0, ax1, ay0, ay1 = 404, 560, 100, 286
    b.append(line(ax0, ay0, ax0, ay1, GRAY_M, 1.2, "butt"))
    b.append(line(ax0, ay1, ax1, ay1, GRAY_M, 1.2, "butt"))
    b.append(line(412, 240, 552, 240, GRAY, 2.2))
    b.append(line(412, 236, 552, 118, ORANGE, 2.4))
    b.append(t(552, 102, "with interaction", 12, INK, "end"))
    b.append(t(552, 258, "no interaction", 12, MUTED, "end"))
    b.append(t(ax0, 84, "genetic effect", 12, MUTED, "start"))
    b.append(t(482, 306, "exposure combination", 12, MUTED, "middle"))
    write("fig_engine", "".join(b), "ENGINE learns one weighted combination of exposures along which genetic effects change")

# ------------------------------------------------------------------ 5. SUM-RHE: same estimates without individual data
def fig_sumrhe():
    b = []
    px0, px1, py0, py1 = 150, 450, 42, 342
    b.append(line(px0, py0, px0, py1, GRAY_M, 1.2, "butt"))
    b.append(line(px0, py1, px1, py1, GRAY_M, 1.2, "butt"))
    b.append(line(px0, py1, px1, py0, RULE, 1.2))
    vals = [0.06, 0.09, 0.13, 0.17, 0.2, 0.24, 0.27, 0.31, 0.35, 0.38, 0.42, 0.46, 0.5, 0.53, 0.57, 0.62, 0.66, 0.7, 0.75, 0.8, 0.86, 0.9]
    jit = [0.01, -0.008, 0.012, -0.011, 0.006, 0.013, -0.012, 0.004, -0.009, 0.011, -0.006, 0.009, -0.013, 0.005, 0.012, -0.01, 0.007, -0.005, 0.01, -0.012, 0.006, -0.008]
    for v, j in zip(vals, jit):
        x = px0 + (px1 - px0) * v; y = py1 - (py1 - py0) * (v + j)
        b.append(dot(x, y, 5.2, BLUE, PAPER, 1.6))
    b.append(t(300, 376, "heritability from individual genomes", 13, INK, "middle"))
    b.append(t(124, 192, "heritability from summary tables", 13, INK, "middle", rotate=-90))
    b.append(t(442, 296, "same estimates", 13, INK, "end", 500))
    b.append(t(442, 314, "no individual-level data required", 11.5, MUTED, "end"))
    write("fig_sumrhe", "".join(b), "Heritability from summary tables matches heritability from individual genomes")

# ------------------------------------------------------------------ 6. REGENA: three readings of a GxE signal
def fig_regena():
    b = []
    panels = [("Scale artefact", "gone after rescaling the trait", GRAY), ("Amplification", "same effects, larger in one group", ORANGE), ("Effect heterogeneity", "different effects in each group", PURPLE)]
    xs_rel = [-0.85, -0.7, -0.58, -0.44, -0.33, -0.2, -0.1, 0.02, 0.12, 0.23, 0.35, 0.47, 0.58, 0.7, 0.82]
    noise = [0.05, -0.04, 0.03, -0.06, 0.02, 0.05, -0.03, 0.04, -0.05, 0.02, -0.04, 0.05, -0.02, 0.03, -0.05]
    het = [0.55, -0.4, 0.2, -0.6, 0.45, -0.25, 0.6, -0.5, 0.3, -0.35, 0.5, -0.45, 0.25, -0.3, 0.4]
    for k, (title, cap, col) in enumerate(panels):
        x0 = 48 + k * 178; y0, size = 96, 160
        b.append(line(x0, y0, x0, y0 + size, GRAY_M, 1.2, "butt"))
        b.append(line(x0, y0 + size, x0 + size, y0 + size, GRAY_M, 1.2, "butt"))
        b.append(line(x0, y0 + size, x0 + size, y0, RULE, 1.2))
        b.append(t(x0 + size / 2, 72, title, 14, INK, "middle", 600))
        b.append(t(x0 + size / 2, 282, cap, 12, MUTED, "middle"))
        for xr, nz, hz in zip(xs_rel, noise, het):
            if k == 0:
                yr = math.copysign(abs(xr) ** 1.9, xr) + nz * 0.4
            elif k == 1:
                xr = xr * 0.62; yr = 1.5 * xr + nz * 0.5
            else:
                yr = 0.35 * xr + hz * 0.75
            yr = max(-0.96, min(0.96, yr))
            x = x0 + size / 2 + xr * size / 2 * 0.94; y = y0 + size / 2 - yr * size / 2 * 0.94
            b.append(dot(x, y, 4.3, col, PAPER, 1.5))
    b.append(t(300, 330, "each dot is one genetic variant, its effect in group A across and in group B up", 11.5, MUTED, "middle"))
    write("fig_regena", "".join(b), "Three readings of a gene-environment interaction signal: scale artefact, amplification, effect heterogeneity")

fig_summit()
fig_recognition("/home/bronsonj/ml_4h/ehr_capture/results/recognition/camera_ready_20261029/revision/recognition_curves.tsv")
fig_raptor(); fig_engine(); fig_sumrhe(); fig_regena()
