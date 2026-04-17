# Beofre Promt:

# import random

# import requests

# cats = [
#     "animal",
#     "career",
#     "celebrity",
#     "dev",
#     "explicit",
#     "fashion",
#     "food",
#     "history",
#     "money",
#     "movie",
#     "music",
#     "political",
#     "religion",
#     "science",
#     "sport",
#     "travel"
#     ]

# def getCNJ(number_of_chucknorris_jokes, type_of_chucknorris_jokes): #"animal" "career" "celebrity" "dev" "explicit" "fashion" "food" "history" "money" "movie" "music" "political" "religion" "science""sport" "travel" "random"
    

#     for x in range(number_of_chucknorris_jokes): 
#         if type_of_chucknorris_jokes.lower() == "random":
#             num = random.randint(0, 15)
#             response_1 = requests.get(f"https://api.chucknorris.io/jokes/random?category={cats[num]}")
#         else:
#             response_1 = requests.get(f"https://api.chucknorris.io/jokes/random?category={type_of_chucknorris_jokes.lower()}")
        
#         if response_1.status_code != 200:
#             print("Error fetching data!")
#             return None

#         data_1 = response_1.json()

#         print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
#         print("Joke number " + str(x+1) + ":")
#         print(str(data_1['categories'][0]).capitalize() + " Joke: " + data_1['value'])
#         print("Source Link: " + data_1['url'])
#         if number_of_chucknorris_jokes == x+1:
#             print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")



# def getFact(number_of_facts, type_random_or_today): #random or today


#     for i in range(number_of_facts): 
#         response_2 = requests.get(f"https://uselessfacts.jsph.pl/api/v2/facts/{type_random_or_today.lower()}") 

#         if response_2.status_code != 200:
#             print("Error fetching data!")
#             return None
    
#         data_2 = response_2.json()
#         print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
#         print("Fact number " + str(i+1) + ":")
#         print(type_random_or_today.capitalize() + "'s Fun Fact: " + data_2['text'])
#         print("Source: " + data_2['source'])
#         print("Source Link: " + data_2['source_url'])
#         if  number_of_facts == i+1:
#             print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    

# def getEntertainment(CNJ_or_Fact):
#     if CNJ_or_Fact.lower() == "cnj":
#         number = int(input("How many?"))
#         print("categories")
#         for cat in cats:
#             print(cat)
#         type = str(input("What category?"))
#         getCNJ(number, type) 
#     elif CNJ_or_Fact.lower() == "fact":
#         number = int(input("How many?"))
#         type = str(input("What category? Today or Random?"))    
#         getFact(number, type)

# getEntertainment("FACT")

#After promt #1:

import random
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext
import requests

# ── palette ────────────────────────────────────────────────────────────────────
BG        = "#0f0f13"
PANEL     = "#1a1a24"
CARD      = "#22222f"
ACCENT_C  = "#f5a623"   # Chuck Norris gold
ACCENT_F  = "#4fc3f7"   # Facts cyan
TEXT      = "#e8e8f0"
MUTED     = "#7070a0"
SUCCESS   = "#66bb6a"
ERROR     = "#ef5350"
BORDER    = "#2e2e45"

FONT_TITLE  = ("Georgia", 26, "bold")
FONT_SUB    = ("Georgia", 13, "italic")
FONT_LABEL  = ("Courier New", 11, "bold")
FONT_BODY   = ("Courier New", 10)
FONT_BTN    = ("Georgia", 12, "bold")
FONT_SMALL  = ("Courier New", 9)

CATS = [
    "animal","career","celebrity","dev","explicit",
    "fashion","food","history","money","movie","music",
    "political","religion","science","sport","travel"
]

# ── API helpers ─────────────────────────────────────────────────────────────────

def fetch_cnj(number: int, category: str):
    results = []
    for i in range(number):
        cat = CATS[random.randint(0, 15)] if category == "random" else category
        try:
            r = requests.get(f"https://api.chucknorris.io/jokes/random?category={cat}", timeout=8)
            r.raise_for_status()
            d = r.json()
            results.append({
                "n": i + 1,
                "category": (d["categories"][0] if d["categories"] else cat).capitalize(),
                "joke": d["value"],
                "url": d["url"],
            })
        except Exception as e:
            results.append({"n": i + 1, "error": str(e)})
    return results


def fetch_fact(number: int, kind: str):
    results = []
    seen = set()
    i = 0
    attempts = 0
    while i < number and attempts < number * 4:
        attempts += 1
        try:
            r = requests.get(f"https://uselessfacts.jsph.pl/api/v2/facts/{kind}", timeout=8)
            r.raise_for_status()
            d = r.json()
            if kind == "today" and i > 0:
                # today returns same fact — show once, pad the rest
                results.append({
                    "n": i + 1,
                    "text": "(Today's fact is the same — only one daily fact is available.)",
                    "source": "", "source_url": "",
                })
                i += 1
                continue
            if d["text"] not in seen or kind == "today":
                seen.add(d["text"])
                results.append({
                    "n": i + 1,
                    "text": d["text"],
                    "source": d.get("source", ""),
                    "source_url": d.get("source_url", ""),
                })
                i += 1
        except Exception as e:
            results.append({"n": i + 1, "error": str(e)})
            i += 1
    return results

# ── styled widgets ──────────────────────────────────────────────────────────────

def make_spinbox(parent, **kw):
    sb = tk.Spinbox(
        parent, from_=1, to=20, width=4,
        font=FONT_LABEL, justify="center",
        bg=CARD, fg=ACCENT_C, insertbackground=ACCENT_C,
        buttonbackground=PANEL, relief="flat",
        highlightthickness=1, highlightbackground=BORDER,
        highlightcolor=ACCENT_C,
        **kw
    )
    return sb


def styled_btn(parent, text, command, accent=ACCENT_C, **kw):
    btn = tk.Button(
        parent, text=text, command=command,
        font=FONT_BTN,
        bg=accent, fg=BG,
        activebackground=TEXT, activeforeground=BG,
        relief="flat", cursor="hand2",
        padx=18, pady=8,
        **kw
    )
    return btn


def label(parent, text, font=FONT_LABEL, fg=TEXT, **kw):
    return tk.Label(parent, text=text, font=font, fg=fg, bg=BG if "bg" not in kw else kw.pop("bg"), **kw)

# ── main app ────────────────────────────────────────────────────────────────────

class EntertainmentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Entertainment Hub")
        self.configure(bg=BG)
        self.resizable(False, False)

        self._cnj_category   = tk.StringVar(value="random")
        self._cnj_count      = tk.IntVar(value=1)
        self._fact_kind      = tk.StringVar(value="random")
        self._fact_count     = tk.IntVar(value=1)

        self._build_header()
        self._build_tabs()
        self._build_output()

        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"+{(sw-w)//2}+{(sh-h)//2}")

    # ── header ─────────────────────────────────────────────────────────────────

    def _build_header(self):
        hdr = tk.Frame(self, bg=PANEL, pady=18)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🎭  Entertainment Hub", font=FONT_TITLE,
                 fg=TEXT, bg=PANEL).pack()
        tk.Label(hdr, text="Chuck Norris Jokes  ·  Useless Fun Facts",
                 font=FONT_SUB, fg=MUTED, bg=PANEL).pack(pady=(2, 0))
        tk.Frame(self, bg=BORDER, height=1).pack(fill="x")

    # ── tabs ───────────────────────────────────────────────────────────────────

    def _build_tabs(self):
        self._tab_frame = tk.Frame(self, bg=BG)
        self._tab_frame.pack(fill="x", padx=24, pady=(18, 0))

        self._cnj_tab_btn  = self._tab_btn("🥊  Chuck Norris Jokes", self._show_cnj)
        self._fact_tab_btn = self._tab_btn("💡  Fun Facts", self._show_fact)

        self._cnj_tab_btn.pack(side="left", padx=(0, 6))
        self._fact_tab_btn.pack(side="left")

        self._cnj_panel  = self._build_cnj_panel()
        self._fact_panel = self._build_fact_panel()

        self._show_cnj()

    def _tab_btn(self, text, cmd):
        return tk.Button(
            self._tab_frame, text=text, command=cmd,
            font=FONT_BTN, relief="flat", cursor="hand2",
            padx=16, pady=8,
            bg=PANEL, fg=MUTED,
            activebackground=CARD, activeforeground=TEXT,
        )

    def _show_cnj(self):
        self._fact_panel.pack_forget()
        self._cnj_panel.pack(fill="x", padx=24, pady=10)
        self._cnj_tab_btn.configure(bg=ACCENT_C, fg=BG)
        self._fact_tab_btn.configure(bg=PANEL, fg=MUTED)

    def _show_fact(self):
        self._cnj_panel.pack_forget()
        self._fact_panel.pack(fill="x", padx=24, pady=10)
        self._fact_tab_btn.configure(bg=ACCENT_F, fg=BG)
        self._cnj_tab_btn.configure(bg=PANEL, fg=MUTED)

    # ── Chuck Norris panel ─────────────────────────────────────────────────────

    def _build_cnj_panel(self):
        pnl = tk.Frame(self, bg=CARD, pady=16, padx=18, relief="flat",
                       highlightthickness=1, highlightbackground=BORDER)

        # Category grid
        tk.Label(pnl, text="CATEGORY", font=FONT_SMALL, fg=ACCENT_C, bg=CARD,
                 anchor="w").grid(row=0, column=0, columnspan=9, sticky="w", pady=(0, 6))

        # "random" button first
        self._cat_btns = {}
        cats_with_random = ["random"] + CATS
        cols = 9
        for idx, cat in enumerate(cats_with_random):
            r, c = divmod(idx, cols)
            btn = tk.Radiobutton(
                pnl, text=cat, variable=self._cnj_category, value=cat,
                font=FONT_SMALL,
                bg=CARD, fg=TEXT,
                selectcolor=ACCENT_C,
                activebackground=CARD, activeforeground=ACCENT_C,
                indicatoron=False,
                relief="flat",
                padx=8, pady=4,
                cursor="hand2",
            )
            btn.grid(row=r + 1, column=c, padx=3, pady=2, sticky="ew")
            self._cat_btns[cat] = btn

        # style selected via trace
        def _update_cat_styles(*_):
            sel = self._cnj_category.get()
            for cat, b in self._cat_btns.items():
                if cat == sel:
                    b.configure(bg=ACCENT_C, fg=BG)
                else:
                    b.configure(bg=PANEL, fg=TEXT)

        self._cnj_category.trace_add("write", _update_cat_styles)
        _update_cat_styles()

        # count + go
        ctrl = tk.Frame(pnl, bg=CARD)
        bottom_row = max(1, -(-len(cats_with_random) // cols)) + 1
        ctrl.grid(row=bottom_row + 1, column=0, columnspan=9, sticky="w", pady=(14, 0))

        tk.Label(ctrl, text="How many jokes?", font=FONT_LABEL, fg=TEXT, bg=CARD).pack(side="left")
        sb = make_spinbox(ctrl, textvariable=self._cnj_count)
        sb.pack(side="left", padx=(10, 16))

        styled_btn(ctrl, "Get Jokes  ▶", self._run_cnj, accent=ACCENT_C).pack(side="left")

        return pnl

    # ── Fun Facts panel ────────────────────────────────────────────────────────

    def _build_fact_panel(self):
        pnl = tk.Frame(self, bg=CARD, pady=16, padx=18, relief="flat",
                       highlightthickness=1, highlightbackground=BORDER)

        tk.Label(pnl, text="FACT TYPE", font=FONT_SMALL, fg=ACCENT_F, bg=CARD,
                 anchor="w").pack(anchor="w", pady=(0, 8))

        rb_frame = tk.Frame(pnl, bg=CARD)
        rb_frame.pack(anchor="w")

        self._fact_kind_btns = {}
        for kind, icon in [("today", "📅  Today's Fact"), ("random", "🎲  Random Fact")]:
            btn = tk.Radiobutton(
                rb_frame, text=icon, variable=self._fact_kind, value=kind,
                font=FONT_BTN,
                bg=PANEL, fg=TEXT,
                selectcolor=ACCENT_F,
                activebackground=CARD, activeforeground=ACCENT_F,
                indicatoron=False,
                relief="flat",
                padx=14, pady=8,
                cursor="hand2",
            )
            btn.pack(side="left", padx=(0, 8))
            self._fact_kind_btns[kind] = btn

        def _update_fact_styles(*_):
            sel = self._fact_kind.get()
            for k, b in self._fact_kind_btns.items():
                b.configure(bg=ACCENT_F if k == sel else PANEL,
                            fg=BG if k == sel else TEXT)

        self._fact_kind.trace_add("write", _update_fact_styles)
        _update_fact_styles()

        # today notice
        self._today_note = tk.Label(
            pnl,
            text="ℹ  Today's fact is fixed — only 1 is available per day.",
            font=FONT_SMALL, fg=MUTED, bg=CARD,
        )

        def _toggle_today_note(*_):
            if self._fact_kind.get() == "today":
                self._today_note.pack(anchor="w", pady=(6, 0))
                self._fact_count.set(1)
                self._fact_spin.configure(state="disabled")
            else:
                self._today_note.pack_forget()
                self._fact_spin.configure(state="normal")

        self._fact_kind.trace_add("write", _toggle_today_note)

        ctrl = tk.Frame(pnl, bg=CARD)
        ctrl.pack(anchor="w", pady=(14, 0))

        tk.Label(ctrl, text="How many facts?", font=FONT_LABEL, fg=TEXT, bg=CARD).pack(side="left")
        self._fact_spin = make_spinbox(ctrl, textvariable=self._fact_count)
        self._fact_spin.configure(disabledbackground=PANEL, disabledforeground=MUTED)
        self._fact_spin.pack(side="left", padx=(10, 16))

        styled_btn(ctrl, "Get Facts  ▶", self._run_fact, accent=ACCENT_F).pack(side="left")

        _toggle_today_note()
        return pnl

    # ── output area ────────────────────────────────────────────────────────────

    def _build_output(self):
        tk.Frame(self, bg=BORDER, height=1).pack(fill="x", pady=(10, 0))

        out_frame = tk.Frame(self, bg=BG)
        out_frame.pack(fill="both", expand=True, padx=24, pady=12)

        self._status = tk.Label(out_frame, text="", font=FONT_SMALL, fg=MUTED, bg=BG, anchor="w")
        self._status.pack(fill="x", pady=(0, 6))

        self._output = scrolledtext.ScrolledText(
            out_frame,
            font=FONT_BODY, bg=PANEL, fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            height=18, width=80,
            wrap="word",
            state="disabled",
            highlightthickness=1, highlightbackground=BORDER,
            padx=12, pady=10,
        )
        self._output.pack(fill="both", expand=True)

        # tags for coloring
        self._output.tag_configure("header",  foreground=ACCENT_C, font=("Courier New", 10, "bold"))
        self._output.tag_configure("fact_hdr",foreground=ACCENT_F, font=("Courier New", 10, "bold"))
        self._output.tag_configure("divider", foreground=BORDER)
        self._output.tag_configure("link",    foreground=MUTED, font=("Courier New", 9))
        self._output.tag_configure("error",   foreground=ERROR)
        self._output.tag_configure("muted",   foreground=MUTED)

    # ── write helpers ───────────────────────────────────────────────────────────

    def _clear(self):
        self._output.configure(state="normal")
        self._output.delete("1.0", "end")

    def _write(self, text, tag=None):
        self._output.configure(state="normal")
        if tag:
            self._output.insert("end", text, tag)
        else:
            self._output.insert("end", text)
        self._output.see("end")
        self._output.configure(state="disabled")

    def _set_status(self, msg, color=MUTED):
        self._status.configure(text=msg, fg=color)

    # ── run fetches in threads ──────────────────────────────────────────────────

    def _run_cnj(self):
        n   = self._cnj_count.get()
        cat = self._cnj_category.get()
        self._clear()
        self._set_status(f"⏳  Fetching {n} Chuck Norris joke(s) — category: {cat} …", ACCENT_C)

        def work():
            results = fetch_cnj(n, cat)
            self.after(0, lambda: self._display_cnj(results))

        threading.Thread(target=work, daemon=True).start()

    def _display_cnj(self, results):
        self._clear()
        div = "─" * 72 + "\n"
        for item in results:
            self._write(div, "divider")
            if "error" in item:
                self._write(f"  Joke #{item['n']} — ERROR\n", "error")
                self._write(f"  {item['error']}\n", "error")
            else:
                self._write(f"  Joke #{item['n']}  ·  {item['category']}\n", "header")
                self._write(f"\n  {item['joke']}\n\n", None)
                self._write(f"  🔗 {item['url']}\n", "link")
        self._write(div, "divider")
        self._set_status(f"✔  {len(results)} joke(s) loaded.", SUCCESS)

    def _run_fact(self):
        n    = self._fact_count.get()
        kind = self._fact_kind.get()
        self._clear()
        self._set_status(f"⏳  Fetching {n} fun fact(s) — {kind} …", ACCENT_F)

        def work():
            results = fetch_fact(n, kind)
            self.after(0, lambda: self._display_facts(results, kind))

        threading.Thread(target=work, daemon=True).start()

    def _display_facts(self, results, kind):
        self._clear()
        div = "─" * 72 + "\n"
        label_word = "Today's" if kind == "today" else "Random"
        for item in results:
            self._write(div, "divider")
            if "error" in item:
                self._write(f"  Fact #{item['n']} — ERROR\n", "error")
                self._write(f"  {item['error']}\n", "error")
            else:
                self._write(f"  Fact #{item['n']}  ·  {label_word} Fun Fact\n", "fact_hdr")
                self._write(f"\n  {item['text']}\n\n", None)
                if item.get("source"):
                    self._write(f"  Source: {item['source']}\n", "muted")
                if item.get("source_url"):
                    self._write(f"  🔗 {item['source_url']}\n", "link")
        self._write(div, "divider")
        self._set_status(f"✔  {len(results)} fact(s) loaded.", SUCCESS)


# ── entry point ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = EntertainmentApp()
    app.mainloop()
